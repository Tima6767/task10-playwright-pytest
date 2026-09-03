from playwright.sync_api import expect
import allure

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.name_input = page.locator('[placeholder="Name"]')
        self.email_input = page.locator('[data-qa="signup-email"]')
        self.password = page.locator('[data-qa="login-password"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')
        self.signup_heading = page.get_by_text('Enter Account Information')
        self.login_button = page.locator('[data-qa="login-button"]')
        self.login_email_input = page.locator('[data-qa="login-email"]')
        self.your_email_or_password_is_incorrect = page.get_by_text('Your email or password is incorrect!')
        self.error_message = page.get_by_text('Email Address already exist')

    @allure.step("Verify New User Signup is visible")
    def verify_new_user_signup_is_visible(self):
        expect(self.page.get_by_text('New User Signup!')).to_be_visible()

    @allure.step("Signup with '{name}' and '{email}'")
    def signup(self, name, email):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()

    @allure.step("Verify Login to Your Account is visible")
    def verify_login_to_your_account_is_visible(self):
        expect(self.page.get_by_text('Login to your account')).to_be_visible()

    @allure.step("Login with email and password")
    def login(self, email, password):
        self.password.fill(password)
        self.login_email_input.fill(email)
        self.login_button.click()

    

    