## Plan: Add backend FastAPI tests in a separate tests directory

TL;DR - Create a root-level `tests/` directory with FastAPI backend tests that exercise `src/app.py` through the app instance, and ensure `pytest` is available for running the suite.

**Steps**
1. Create a new `tests/` directory at the repository root.
2. Add `tests/test_app.py` with `fastapi.testclient.TestClient` tests for the backend API.
   - Use the Arrange-Act-Assert pattern in each test.
   - Import `app` from `src.app`.
   - Cover root redirect, activity listing, signup, duplicate signup, non-existent activity, remove participant, and missing participant cases.
3. Add `pytest` to `requirements.txt` if it is not already present, so the project can run the new tests in a standard Python environment.
4. Optionally add `tests/conftest.py` with a reusable `client` fixture if the suite will expand later.

**Relevant files**
- `/workspaces/skills-getting-started-with-github-copilot/src/app.py` — backend API implementation to test.
- `/workspaces/skills-getting-started-with-github-copilot/requirements.txt` — may need `pytest` added.
- `/workspaces/skills-getting-started-with-github-copilot/pytest.ini` — already configures `pythonpath = .` for importing `src.app`.

**Verification**
1. Run `pytest` from the repository root and confirm the new tests pass.
2. Confirm `tests/test_app.py` is discovered and executed by `pytest`.
3. Verify the tests actually hit `src/app.py` by using the app instance and response status/assertions.

**Decisions**
- Use `fastapi.testclient.TestClient` for straightforward synchronous tests of the existing FastAPI app.
- Keep backend tests separated from any frontend or static file tests by locating them under `tests/`.

**Further Considerations**
1. If you want more isolation, we can also add `tests/conftest.py` now with a reusable `client` fixture.
2. If you prefer async HTTP tests instead, we can use `httpx.AsyncClient` and add `pytest-asyncio` to requirements.
