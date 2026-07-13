Automated Tests for Rostelecom ID (b2c.passport.rt.ru)

Project Description

Automated tests for verifying the functionality of the Rostelecom authorization page.

What's covered:


Opening the authorization page
Password login form (all 4 tabs: Phone, Email, Login, Account Number)
One-time code login form
Login with invalid credentials
Registration and password recovery links
Social media login buttons


Project Structure

rostelecom_tests/
  pages/
    base_page.py       - base page class
    auth_page.py        - authorization page class
    register_page.py   - registration page class
    recovery_page.py   - password recovery page class
  tests/
    test_auth.py        - 20 automated tests
  conftest.py           - browser setup
  requirements.txt      - dependencies
  README.md             - project description

Installation and Running

1. Requirements


Python 3.8+
Google Chrome
ChromeDriver (matching version)


2. Install Dependencies

pip install -r requirements.txt

3. Configure Test Data

In tests/test_auth.py, replace:

VALID_EMAIL = "your_email@gmail.com"
VALID_PASSWORD = "YourPassword123"

4. Run Tests

# All tests
pytest tests/ -v

# A specific test
pytest tests/test_auth.py::test_tk001_auth_page_opens -v

# With an HTML report
pytest tests/ -v --html=report.html

Tools


Selenium WebDriver — browser automation
PyTest — test runner
Page Object pattern — test architecture
SelectorsHub — locator discovery


Note

The site is only accessible from Russia. If testing from another country, use a VPN with a Russian server.
