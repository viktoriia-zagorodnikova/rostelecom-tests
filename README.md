# 🔐 Automated Tests for Rostelecom ID (b2c.passport.rt.ru)

> ⚠️ **Note:** This is a personal pet project built to practice test automation skills. It is not affiliated with or endorsed by Rostelecom.

## 📋 Project Description

Automated test suite for verifying the functionality of the Rostelecom authorization page, built using Selenium WebDriver, Pytest, and the Page Object pattern.

## ✅ What's Covered

- Opening the authorization page
- Password login form (all 4 tabs: Phone, Email, Login, Account Number)
- One-time code login form
- Login with invalid credentials
- Registration and password recovery links
- Social media login buttons

## 🗂 Project Structure

```
rostelecom_tests/
├── pages/
│   ├── base_page.py        # base page class
│   ├── auth_page.py        # authorization page class
│   ├── register_page.py    # registration page class
│   └── recovery_page.py    # password recovery page class
├── tests/
│   └── test_auth.py        # 20 automated tests
├── conftest.py              # browser setup
├── requirements.txt         # dependencies
└── README.md                # project description
```

## 🚀 Installation and Running

### 1. Requirements
- Python 3.8+
- Google Chrome
- ChromeDriver (matching version)

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure test data
In `tests/test_auth.py`, replace:
```python
VALID_EMAIL = "your_email@gmail.com"
VALID_PASSWORD = "YourPassword123"
```

### 4. Run tests
```bash
# All tests
pytest tests/ -v

# A specific test
pytest tests/test_auth.py::test_tk001_auth_page_opens -v

# With an HTML report
pytest tests/ -v --html=report.html
```

## 🛠 Tools

| Tool | Purpose |
|---|---|
| Selenium WebDriver | Browser automation |
| PyTest | Test runner |
| Page Object pattern | Test architecture |
| SelectorsHub | Locator discovery |

## 📝 Note

The site is only accessible from Russia. If testing from another country, use a VPN with a Russian server.
