import pytest
from datetime import date, timedelta
from decimal import Decimal
from library_loan import (
    Service,
    Book,
    Loan,
    User,
    BookUnavailable,
    LoanLimitReached,
    LoanNotFound,
    DuplicateBook,
    DuplicateUser,
    UserNotFound,
)


class TestBook:
    def test_book_creation(self):
        book = Book(id="B001", title="Python Programming", copies_total=3)
        assert book.id == "B001"
        assert book.title == "Python Programming"
        assert book.copies_total == 3

    def test_book_copies_total_must_be_at_least_one(self):
        with pytest.raises(ValueError):
            Book(id="B002", title="Invalid Book", copies_total=0)


class TestUser:
    def test_user_creation(self):
        user = User(id="U001")
        assert user.id == "U001"


class TestLoan:
    def test_loan_creation(self):
        borrowed_on = date(2024, 1, 1)
        due_on = date(2024, 1, 15)
        loan = Loan(
            book_id="B001", user_id="U001", borrowed_on=borrowed_on, due_on=due_on
        )
        assert loan.book_id == "B001"
        assert loan.user_id == "U001"
        assert loan.borrowed_on == borrowed_on
        assert loan.due_on == due_on
        assert loan.returned_on is None

    def test_loan_with_return_date(self):
        borrowed_on = date(2024, 1, 1)
        due_on = date(2024, 1, 15)
        returned_on = date(2024, 1, 10)
        loan = Loan(
            book_id="B001",
            user_id="U001",
            borrowed_on=borrowed_on,
            due_on=due_on,
            returned_on=returned_on,
        )
        assert loan.returned_on == returned_on


class TestServiceCatalog:
    def test_add_book_registers_book(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=2)
        service.add_book(book)
        books = service.list_books()
        assert len(books) == 1
        assert books[0].id == "B001"

    def test_add_book_duplicate_raises_error(self):
        service = Service()
        book1 = Book(id="B001", title="Test Book", copies_total=2)
        book2 = Book(id="B001", title="Another Title", copies_total=3)
        service.add_book(book1)
        with pytest.raises(DuplicateBook):
            service.add_book(book2)

    def test_add_user_registers_user(self):
        service = Service()
        user = User(id="U001")
        service.add_user(user)
        users = service.list_users()
        assert len(users) == 1
        assert users[0].id == "U001"

    def test_add_user_duplicate_raises_error(self):
        service = Service()
        user1 = User(id="U001")
        user2 = User(id="U001")
        service.add_user(user1)
        with pytest.raises(DuplicateUser):
            service.add_user(user2)


class TestBorrowBook:
    def test_borrow_book_success(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=2)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        assert loan_id is not None

        loan = service.get_loan(loan_id)
        assert loan.book_id == "B001"
        assert loan.user_id == "U001"
        assert loan.borrowed_on == date(2024, 1, 1)
        expected_due = date(2024, 1, 1) + timedelta(days=14)
        assert loan.due_on == expected_due
        assert loan.returned_on is None

    def test_borrow_book_unregistered_book_raises_error(self):
        service = Service()
        user = User(id="U001")
        service.add_user(user)
        with pytest.raises(BookUnavailable):
            service.borrow("B001", "U001", date(2024, 1, 1))

    def test_borrow_book_unregistered_user_raises_error(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=2)
        service.add_book(book)
        with pytest.raises(UserNotFound):
            service.borrow("B001", "U001", date(2024, 1, 1))

    def test_borrow_book_no_copies_available_raises_error(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user1 = User(id="U001")
        user2 = User(id="U002")
        service.add_book(book)
        service.add_user(user1)
        service.add_user(user2)

        service.borrow("B001", "U001", date(2024, 1, 1))
        with pytest.raises(BookUnavailable):
            service.borrow("B001", "U002", date(2024, 1, 1))

    def test_borrow_book_all_copies_on_loan_raises_error(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=2)
        user1 = User(id="U001")
        user2 = User(id="U002")
        user3 = User(id="U003")
        service.add_book(book)
        service.add_user(user1)
        service.add_user(user2)
        service.add_user(user3)

        service.borrow("B001", "U001", date(2024, 1, 1))
        service.borrow("B001", "U002", date(2024, 1, 1))
        with pytest.raises(BookUnavailable):
            service.borrow("B001", "U003", date(2024, 1, 1))

    def test_borrow_returned_copy_becomes_available(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user1 = User(id="U001")
        user2 = User(id="U002")
        service.add_book(book)
        service.add_user(user1)
        service.add_user(user2)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        service.return_book(loan_id, date(2024, 1, 5))

        loan_id2 = service.borrow("B001", "U002", date(2024, 1, 6))
        assert loan_id2 is not None

    def test_borrow_user_has_three_active_loans_raises_error(self):
        service = Service()
        book1 = Book(id="B001", title="Book 1", copies_total=1)
        book2 = Book(id="B002", title="Book 2", copies_total=1)
        book3 = Book(id="B003", title="Book 3", copies_total=1)
        book4 = Book(id="B004", title="Book 4", copies_total=1)
        user = User(id="U001")
        service.add_book(book1)
        service.add_book(book2)
        service.add_book(book3)
        service.add_book(book4)
        service.add_user(user)

        service.borrow("B001", "U001", date(2024, 1, 1))
        service.borrow("B002", "U001", date(2024, 1, 1))
        service.borrow("B003", "U001", date(2024, 1, 1))
        with pytest.raises(LoanLimitReached):
            service.borrow("B004", "U001", date(2024, 1, 1))

    def test_borrow_after_returning_allows_new_loan(self):
        service = Service()
        book1 = Book(id="B001", title="Book 1", copies_total=1)
        book2 = Book(id="B002", title="Book 2", copies_total=1)
        book3 = Book(id="B003", title="Book 3", copies_total=1)
        book4 = Book(id="B004", title="Book 4", copies_total=1)
        user = User(id="U001")
        service.add_book(book1)
        service.add_book(book2)
        service.add_book(book3)
        service.add_book(book4)
        service.add_user(user)

        loan1 = service.borrow("B001", "U001", date(2024, 1, 1))
        service.borrow("B002", "U001", date(2024, 1, 1))
        service.borrow("B003", "U001", date(2024, 1, 1))

        service.return_book(loan1, date(2024, 1, 5))

        loan4 = service.borrow("B004", "U001", date(2024, 1, 6))
        assert loan4 is not None

    def test_loan_duration_is_14_days(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        borrowed_on = date(2024, 1, 1)
        loan_id = service.borrow("B001", "U001", borrowed_on)
        loan = service.get_loan(loan_id)

        expected_due = borrowed_on + timedelta(days=14)
        assert loan.due_on == expected_due


class TestReturnBook:
    def test_return_book_success(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        service.return_book(loan_id, date(2024, 1, 10))

        loan = service.get_loan(loan_id)
        assert loan.returned_on == date(2024, 1, 10)

    def test_return_book_idempotent(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        service.return_book(loan_id, date(2024, 1, 10))
        service.return_book(loan_id, date(2024, 1, 12))

        loan = service.get_loan(loan_id)
        assert loan.returned_on == date(2024, 1, 10)

    def test_return_book_unknown_loan_raises_error(self):
        service = Service()
        with pytest.raises(LoanNotFound):
            service.return_book("NONEXISTENT", date(2024, 1, 10))

    def test_return_book_before_borrow_date_sets_to_borrow_date(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 10))
        with pytest.raises(ValueError):
            service.return_book(loan_id, date(2024, 1, 5))


class TestLateFee:
    def test_late_fee_not_late_no_fee(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        fee = service.late_fee(loan_id, date(2024, 1, 15))
        assert fee == Decimal("0.00")

    def test_late_fee_one_day_late(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        service.return_book(loan_id, date(2024, 1, 16))
        fee = service.late_fee(loan_id, date(2024, 1, 16))
        assert fee == Decimal("0.25")

    def test_late_fee_multiple_days_late(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        service.return_book(loan_id, date(2024, 1, 20))
        fee = service.late_fee(loan_id, date(2024, 1, 20))
        assert fee == Decimal("1.25")

    def test_late_fee_max_cap_20_dollars(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        service.return_book(loan_id, date(2024, 4, 15))
        fee = service.late_fee(loan_id, date(2024, 4, 15))
        assert fee == Decimal("20.00")

    def test_late_fee_active_loan_overdue(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        fee = service.late_fee(loan_id, date(2024, 1, 20))
        assert fee == Decimal("1.25")

    def test_late_fee_on_time_return_no_fee(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        service.return_book(loan_id, date(2024, 1, 14))
        fee = service.late_fee(loan_id, date(2024, 1, 20))
        assert fee == Decimal("0.00")

    def test_late_fee_returns_decimal_with_two_places(self):
        service = Service()
        book = Book(id="B001", title="Test Book", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        service.return_book(loan_id, date(2024, 1, 16))
        fee = service.late_fee(loan_id, date(2024, 1, 16))
        assert isinstance(fee, Decimal)
        assert fee == Decimal("0.25")


class TestActiveLoans:
    def test_active_loans_returns_only_active_loans(self):
        service = Service()
        book1 = Book(id="B001", title="Book 1", copies_total=1)
        book2 = Book(id="B002", title="Book 2", copies_total=1)
        user = User(id="U001")
        service.add_book(book1)
        service.add_book(book2)
        service.add_user(user)

        loan1 = service.borrow("B001", "U001", date(2024, 1, 1))
        loan2 = service.borrow("B002", "U001", date(2024, 1, 5))

        service.return_book(loan1, date(2024, 1, 10))

        active = service.active_loans("U001")
        assert len(active) == 1
        assert active[0].book_id == "B002"

    def test_active_loans_ordered_by_due_on_ascending(self):
        service = Service()
        book1 = Book(id="B001", title="Book 1", copies_total=1)
        book2 = Book(id="B002", title="Book 2", copies_total=1)
        book3 = Book(id="B003", title="Book 3", copies_total=1)
        user = User(id="U001")
        service.add_book(book1)
        service.add_book(book2)
        service.add_book(book3)
        service.add_user(user)

        service.borrow("B001", "U001", date(2024, 1, 1))
        service.borrow("B002", "U001", date(2024, 1, 10))
        service.borrow("B003", "U001", date(2024, 1, 5))

        active = service.active_loans("U001")
        assert active[0].book_id == "B001"
        assert active[1].book_id == "B003"
        assert active[2].book_id == "B002"

    def test_active_loans_empty_for_user_with_no_loans(self):
        service = Service()
        user = User(id="U001")
        service.add_user(user)

        active = service.active_loans("U001")
        assert len(active) == 0

    def test_active_loans_only_for_specific_user(self):
        service = Service()
        book1 = Book(id="B001", title="Book 1", copies_total=1)
        book2 = Book(id="B002", title="Book 2", copies_total=1)
        user1 = User(id="U001")
        user2 = User(id="U002")
        service.add_book(book1)
        service.add_book(book2)
        service.add_user(user1)
        service.add_user(user2)

        service.borrow("B001", "U001", date(2024, 1, 1))
        service.borrow("B002", "U002", date(2024, 1, 1))

        active = service.active_loans("U001")
        assert len(active) == 1
        assert active[0].book_id == "B001"


class TestOverdueLoans:
    def test_overdue_loans_returns_loans_past_due(self):
        service = Service()
        book = Book(id="B001", title="Book 1", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        service.borrow("B001", "U001", date(2024, 1, 1))
        overdue = service.overdue_loans(date(2024, 1, 20))
        assert len(overdue) == 1

    def test_overdue_loans_excludes_on_time_loans(self):
        service = Service()
        book = Book(id="B001", title="Book 1", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        service.borrow("B001", "U001", date(2024, 1, 1))
        overdue = service.overdue_loans(date(2024, 1, 15))
        assert len(overdue) == 0

    def test_overdue_loans_excludes_returned_loans(self):
        service = Service()
        book = Book(id="B001", title="Book 1", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        loan_id = service.borrow("B001", "U001", date(2024, 1, 1))
        service.return_book(loan_id, date(2024, 1, 20))
        overdue = service.overdue_loans(date(2024, 1, 20))
        assert len(overdue) == 0

    def test_overdue_loans_ordered_by_user_id_then_due_on(self):
        service = Service()
        book1 = Book(id="B001", title="Book 1", copies_total=1)
        book2 = Book(id="B002", title="Book 2", copies_total=1)
        book3 = Book(id="B003", title="Book 3", copies_total=1)
        user1 = User(id="U001")
        user2 = User(id="U002")
        service.add_book(book1)
        service.add_book(book2)
        service.add_book(book3)
        service.add_user(user1)
        service.add_user(user2)

        service.borrow("B001", "U002", date(2024, 1, 1))
        service.borrow("B002", "U001", date(2024, 1, 1))
        service.borrow("B003", "U001", date(2024, 1, 5))

        overdue = service.overdue_loans(date(2024, 1, 20))
        assert len(overdue) == 3
        assert overdue[0].user_id == "U001"
        assert overdue[0].book_id == "B002"
        assert overdue[1].user_id == "U001"
        assert overdue[1].book_id == "B003"
        assert overdue[2].user_id == "U002"
        assert overdue[2].book_id == "B001"

    def test_overdue_loans_empty_when_none_overdue(self):
        service = Service()
        book = Book(id="B001", title="Book 1", copies_total=1)
        user = User(id="U001")
        service.add_book(book)
        service.add_user(user)

        service.borrow("B001", "U001", date(2024, 1, 1))
        overdue = service.overdue_loans(date(2024, 1, 10))
        assert len(overdue) == 0


class TestIntegration:
    def test_multiple_users_borrowing_same_book_over_time(self):
        service = Service()
        book = Book(id="B001", title="Popular Book", copies_total=2)
        user1 = User(id="U001")
        user2 = User(id="U002")
        user3 = User(id="U003")
        service.add_book(book)
        service.add_user(user1)
        service.add_user(user2)
        service.add_user(user3)

        loan1 = service.borrow("B001", "U001", date(2024, 1, 1))
        loan2 = service.borrow("B001", "U002", date(2024, 1, 2))
        with pytest.raises(BookUnavailable):
            service.borrow("B001", "U003", date(2024, 1, 3))

        service.return_book(loan1, date(2024, 1, 10))
        loan3 = service.borrow("B001", "U003", date(2024, 1, 11))
        assert loan3 is not None

        service.return_book(loan2, date(2024, 1, 12))
        service.return_book(loan3, date(2024, 1, 13))

        active = service.active_loans("U001") + service.active_loans("U002") + service.active_loans("U003")
        assert len(active) == 0

    def test_user_borrowing_multiple_books(self):
        service = Service()
        book1 = Book(id="B001", title="Book 1", copies_total=1)
        book2 = Book(id="B002", title="Book 2", copies_total=1)
        book3 = Book(id="B003", title="Book 3", copies_total=1)
        user = User(id="U001")
        service.add_book(book1)
        service.add_book(book2)
        service.add_book(book3)
        service.add_user(user)

        service.borrow("B001", "U001", date(2024, 1, 1))
        service.borrow("B002", "U001", date(2024, 1, 2))
        service.borrow("B003", "U001", date(2024, 1, 3))

        active = service.active_loans("U001")
        assert len(active) == 3
