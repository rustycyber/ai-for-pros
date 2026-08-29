## Task 1: The Vague Prompt (Copy & Paste)
"Help me debug this API endpoint. It keeps returning a 500 internal server error."

---

## Task 2: The CRISP Spec Prompt (Copy & Paste)
- **Context:** Flask app returning 500 on /api/users/<user_id> when requesting non-existent IDs.
- **Role:** Senior Python Backend Engineer.
- **Instructions:** Find the root cause of the missing key error, propose a safe fix using `.get()`, and provide verification steps.
- **Style:** Markdown with: 1. Root Cause, 2. Code Diff/Fix, 3. Verification Steps.
- **Parameters:** Python 3.11, handle 404 cleanly, no database schema changes.
