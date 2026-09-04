# AutomationExercise - Playwright + Pytest

Automated UI tests for [AutomationExercise](https://www.automationexercise.com/) using Playwright and Pytest.

The project follows the Page Object Model (POM) pattern and currently covers 10 test cases from the AutomationExercise test suite.

## Project Description

This project was created as part of a QA Automation training task.

The tests are implemented using:

- Python
- Pytest
- Playwright
- Page Object Model (POM)
- Faker
- Allure
- Pytest-xdist

The automated tests cover user registration, login, logout, contact form, test cases page, products, product search, and subscription functionality.

## Requirements

- Python 3.10+
- Git
- Node.js and npm
- Java 8+
- Playwright
- Pytest
- Allure Commandline

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd task10-playwright-pytest
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.\.venv\Scripts\activate
```

Install the project dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Install Playwright browsers:

```powershell
.\.venv\Scripts\python.exe -m playwright install
```

## Run Tests

Run all tests:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v
```

Run a specific test:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v -k "test_name"
```

## Run Tests in Different Browsers

Run tests in Chromium:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v --browser chromium
```

Run tests in Firefox:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v --browser firefox
```

Run tests in WebKit:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v --browser webkit
```

Run tests in multiple browsers:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v --browser chromium --browser firefox --browser webkit
```

## Run Tests in Parallel

Run tests in parallel using all available CPU cores:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v --numprocesses auto
```

Parallel execution can also be combined with multiple browsers:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v --numprocesses auto --browser chromium --browser firefox --browser webkit
```

## Allure Report

Run tests and generate Allure results:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v --alluredir=allure-results
```

Open the Allure report locally:

```powershell
npx allure serve allure-results
```

Generate a static Allure report:

```powershell
npx allure generate allure-results -o allure-report --clean
```

The latest Allure report is also published to GitHub Pages:

https://tima6767.github.io/task10-playwright-pytest/

## Project Structure

```text
task10-playwright-pytest/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── pages/
│   ├── account_created_page.py
│   ├── cases_page.py
│   ├── contact_us_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── signup_page.py
│
├── tests/
│   ├── allure_helpers.py
│   ├── test_data.py
│   └── test_main.py
│
├── .gitignore
├── conftest.py
├── package.json
├── package-lock.json
├── README.md
└── requirements.txt
```

## Test Cases

The project currently automates the following test cases:

1. Register User
2. Login User with correct credentials
3. Login User with incorrect credentials
4. Logout User
5. Register User with existing email
6. Contact Us Form
7. Verify Test Cases Page
8. Verify All Products and Product Detail Page
9. Search Product
10. Verify Subscription in Home Page

## Test Data

Test data is generated dynamically using Faker where appropriate.

Randomly generated data helps prevent tests from relying on fixed values and reduces conflicts caused by previously created accounts or reused test data.

## Page Object Model

The project uses the Page Object Model pattern.

Page-specific locators and UI interactions are stored inside the corresponding page classes, while test cases contain the test flow and high-level verification.

This approach improves:

- Code reusability
- Test readability
- Maintainability
- Locator organization

## Reporting

Allure is used for test reporting.

The report includes:

- Test execution results
- Test steps
- Screenshots of important test milestones
- Test status
- Additional test execution information

## CI/CD

GitHub Actions is used to run the automated tests in a CI environment.

The pipeline:

- Installs project dependencies
- Installs Playwright browsers
- Runs automated tests
- Generates Allure results
- Generates a static Allure report
- Uploads Allure results and the generated report as workflow artifacts
- Publishes the Allure report to GitHub Pages
- Sends the test execution status to Slack

The workflow file is located at:

```text
.github/workflows/tests.yml
```

The pipeline runs automatically on pushes to `main`/`master`, on pull requests, and can also be started manually from the GitHub Actions tab.

Because the tested website can be unstable and may apply anti-bot verification in CI environments, the pipeline generates and publishes the Allure report even when tests fail. The workflow still finishes with a failed status if pytest fails.

The Allure report is available on GitHub Pages:

https://tima6767.github.io/task10-playwright-pytest/

## Notifications

Slack notifications are integrated into the GitHub Actions workflow.

After each push to `main`/`master`, the workflow sends a notification to Slack containing:

- Test execution status
- Pass/fail state
- Link to the Allure report

Example notification:

```text
Playwright tests: FAILED ❌
Allure Report: https://tima6767.github.io/task10-playwright-pytest/
```

The Slack webhook URL is stored securely as a GitHub repository secret named:

```text
SLACK_WEBHOOK_URL
```
