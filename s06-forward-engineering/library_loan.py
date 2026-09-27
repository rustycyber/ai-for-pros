from dataclasses import dataclass, field
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from typing import Optional
import uuid


@dataclass
class Book:
    id: str
    title: str
    copies_total: int

    def __post_init__(self):
        if self.copies_total < 1:
            raise ValueError("copies_total must be at least 1")


@dataclass
class User:
    id: str


@dataclass
class Loan:
    book_id: str
    user_id: str
    borrowed_on: date
    due_on: date
    returned_on: Optional[date] = None
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


class BookUnavailable(Exception):
    pass


class LoanLimitReached(Exception):
    pass


class LoanNotFound(Exception):
    pass


class DuplicateBook(Exception):
    pass


class DuplicateUser(Exception):
    pass


class UserNotFound(Exception):
    pass


class Service:
    def __init__(self):
        self._books: dict[str, Book] = {}
        self._users: dict[str, User] = {}
        self._loans: dict[str, Loan] = {}

    def add_book(self, book: Book) -> None:
        if book.id in self._books:
            raise DuplicateBook(f"Book with id '{book.id}' already exists")
        self._books[book.id] = book

    def add_user(self, user: User) -> None:
        if user.id in self._users:
            raise DuplicateUser(f"User with id '{user.id}' already exists")
        self._users[user.id] = user

    def list_books(self) -> list[Book]:
        return list(self._books.values())

    def list_users(self) -> list[User]:
        return list(self._users.values())

    def borrow(self, book_id: str, user_id: str, borrowed_on: date) -> str:
        if book_id not in self._books:
            raise BookUnavailable(f"Book with id '{book_id}' not found")
        if user_id not in self._users:
            raise UserNotFound(f"User with id '{user_id}' not found")

        book = self._books[book_id]
        active_loans_count = self._count_active_loans(user_id)
        if active_loans_count >= 3:
            raise LoanLimitReached(f"User '{user_id}' has reached the loan limit of 3")

        available_copies = self._count_available_copies(book_id)
        if available_copies <= 0:
            raise BookUnavailable(f"No copies of book '{book_id}' available")

        due_on = borrowed_on + timedelta(days=14)
        loan = Loan(
            book_id=book_id,
            user_id=user_id,
            borrowed_on=borrowed_on,
            due_on=due_on,
        )
        self._loans[loan.id] = loan
        return loan.id

    def return_book(self, loan_id: str, returned_on: date) -> None:
        if loan_id not in self._loans:
            raise LoanNotFound(f"Loan with id '{loan_id}' not found")

        loan = self._loans[loan_id]
        if loan.returned_on is not None:
            return

        if returned_on < loan.borrowed_on:
            raise ValueError("returned_on cannot be before borrowed_on")

        loan.returned_on = returned_on

    def get_loan(self, loan_id: str) -> Loan:
        if loan_id not in self._loans:
            raise LoanNotFound(f"Loan with id '{loan_id}' not found")
        return self._loans[loan_id]

    def late_fee(self, loan_id: str, today: date) -> Decimal:
        loan = self.get_loan(loan_id)

        if loan.returned_on is not None:
            if loan.returned_on <= loan.due_on:
                return Decimal("0.00")
            days_late = (loan.returned_on - loan.due_on).days
        else:
            if today <= loan.due_on:
                return Decimal("0.00")
            days_late = (today - loan.due_on).days

        fee = Decimal(days_late) * Decimal("0.25")
        max_fee = Decimal("20.00")
        fee = min(fee, max_fee)
        return fee.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def active_loans(self, user_id: str) -> list[Loan]:
        user_loans = [
            loan for loan in self._loans.values()
            if loan.user_id == user_id and loan.returned_on is None
        ]
        return sorted(user_loans, key=lambda l: l.due_on)

    def overdue_loans(self, today: date) -> list[Loan]:
        overdue = [
            loan for loan in self._loans.values()
            if loan.returned_on is None and today > loan.due_on
        ]
        return sorted(overdue, key=lambda l: (l.user_id, l.due_on))

    def _count_active_loans(self, user_id: str) -> int:
        return sum(
            1 for loan in self._loans.values()
            if loan.user_id == user_id and loan.returned_on is None
        )

    def _count_available_copies(self, book_id: str) -> int:
        book = self._books[book_id]
        active_loans = sum(
            1 for loan in self._loans.values()
            if loan.book_id == book_id and loan.returned_on is None
        )
        return book.copies_total - active_loans
