# Library Loan Service - Spec v1

A small in-memory service for tracking book loans.

## Domain
- `Book`: id (str), title (str), copies_total (int >= 1).
- `Loan`: book_id (str), user_id (str), borrowed_on (date), due_on
  (date). `returned_on` (date | None).
- `User`: id (str).

## Rules

### R1 - Borrow a book
- A user MAY borrow a book if (a) the book has >=1 copy currently
  available (copies_total minus active loans), AND (b) the user has
  fewer than 3 active loans.
- Loan duration is 14 days from `borrowed_on`.
- Raises `BookUnavailable` if no copy available.
- Raises `LoanLimitReached` if user already has 3 active loans.

### R2 - Return a book
- Setting `returned_on` to a date >= `borrowed_on` releases the copy.
- Returning a loan that is already returned is a no-op (idempotent).
- Raises `LoanNotFound` if the loan id is unknown.

### R3 - Late fees
- A loan is late if `returned_on > due_on` OR (`returned_on` is None
  AND today > due_on).
- Fee = $0.25 per day late (clipped at $20.00 max).
- `Service.late_fee(loan_id, today)` returns the fee in dollars
  (Decimal with 2-place rounding).

### R4 - Listing
- `Service.active_loans(user_id)` returns loans where `returned_on`
  is None, ordered by `due_on` ascending.
- `Service.overdue_loans(today)` returns all active loans where
  `today > due_on`, ordered by user_id then due_on.

### R5 - Catalog
- `Service.add_book(book)` registers a book. Duplicate book_id raises
  `DuplicateBook`.
- `Service.add_user(user)` registers a user. Duplicate user_id raises
  `DuplicateUser`.
- Borrowing requires the book and user to be registered, else raises
  `BookUnavailable` / `UserNotFound`.

## Out of scope (v1)
- Persistence. Service is in-memory.
- Multi-branch. Single library.
- Reservations / holds.
- Money other than USD.
