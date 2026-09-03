from playwright.sync_api import expect
import allure 

class HomePage:

    def __init__(self, page):
        self.page = page
        self.login_button = page.locator('[href="/login"]')
        self.delete_account_button = page.get_by_text(' Delete Account')
        self.loggedin_as_username = page.get_by_text('Logged in as')
        self.logout = page.get_by_text(' Logout')
        self.contact_us_button = page.get_by_text(' Contact us')
        self.subscription_email_input = page.locator('#susbscribe_email')
        self.subscription_button = page.locator('#subscribe')
        self.subscription_success_message = page.get_by_text('You have been successfully subscribed!')

    @allure.step("Open home page")
    def open(self):
        self.page.goto('https://automationexercise.com/')


    @allure.step("Verify home page is visible")
    def verify_home_page_is_visible(self):
        expect(self.page.locator('#header')).to_be_visible()
        expect(self.page.locator('#slider-carousel')).to_be_visible()

    @allure.step("Navigate to login page")
    def login_button_click(self):
        expect(self.page.locator('[href="/login"]')).to_be_visible()
        self.page.locator('[href="/login"]').click()

    @allure.step("Delete account")
    def delete_account(self):
        self.delete_account_button.click()
        expect(self.page.get_by_text('Account Deleted!')).to_be_visible()
        self.page.locator('[data-qa="continue-button"]').click()

    @allure.step("logged in as {name}")
    def logged_in_as(self, name):
        expect(self.page.locator('a').filter(has_text='Logged in as')).to_contain_text(name)

    @allure.step("Navigate to Contact Us page")
    def click_contact_us_button(self):
        self.contact_us_button.click()

    @allure.step("Navigate to Test Cases page")
    def click_test_cases_button(self):
        self.page.get_by_role("link", name="Test Cases", exact=True).click()

    @allure.step("Navigate to Products page")
    def click_products_button(self):
        self.page.locator('[class="nav navbar-nav"]').get_by_role("link", name="Products",).click()
        
    @allure.step("Verify subscription is visible")
    def verify_subscription_is_visible(self):
        self.page.get_by_text('Subscription').scroll_into_view_if_needed()
        expect(self.page.get_by_text('Subscription')).to_be_visible()
        
    @allure.step("Subscribe {email}")
    def subscribe(self, email):
        self.subscription_email_input.fill(email)
        self.subscription_button.click()
        