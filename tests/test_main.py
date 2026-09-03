from playwright.sync_api import Page
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests.test_data import generate_user
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.contact_us_page import ContactUsPage
from pathlib import Path
from pages.products_page import ProductsPage
from allure_helpers import attach_screenshot
from pages.test_case_page import TestCasePage



def test_register_user(page: Page):

    user = generate_user()

    home_page = HomePage(page)

    login_page = LoginPage(page)

    signup_page = SignupPage(page)

    account_created_page = AccountCreatedPage(page)

    home_page.open()
    attach_screenshot(page, "Home Page")

    home_page.verify_home_page_is_visible()

    expect(home_page.login_button).to_be_visible()

    home_page.login_button_click()
    attach_screenshot(page, 'Login Page')

    login_page.verify_new_user_signup_is_visible()

    login_page.signup(user['name'], user['email'])
    attach_screenshot(page, 'Signup Page')

    expect(login_page.signup_heading).to_be_visible() 

    signup_page.fill_account_information(user['password'])

    signup_page.fill_address_information(
    user["first_name"],
    user["last_name"],
    user["company"],
    user["address"],
    user["address2"],
    user["state"],
    user["city"],
    user["zipcode"],
    user["mobile_number"],
)
    signup_page.create_account_button.click()
    attach_screenshot(page, 'Account Created Page')

    expect(account_created_page.account_created).to_be_visible()

    account_created_page.continue_button.click()
    attach_screenshot(page, 'Home Page After Account Creation')

    expect(home_page.loggedin_as_username).to_be_visible()

    home_page.delete_account()


def test_login_user_with_correct_email_and_password(page: Page):

    user = generate_user()
    
    home_page = HomePage(page)

    login_page = LoginPage(page)

    signup_page = SignupPage(page)

    account_created_page = AccountCreatedPage(page)

    home_page.open()
    home_page.verify_home_page_is_visible()
    attach_screenshot(page, "Home Page")

    expect(home_page.login_button).to_be_visible()

    home_page.login_button_click()

    attach_screenshot(page, 'Login Page')
    login_page.verify_login_to_your_account_is_visible()

    login_page.signup(user['name'], user['email'])

    signup_page.fill_account_information(user['password'])

    signup_page.fill_address_information(
    user["first_name"],
    user["last_name"],
    user["company"],
    user["address"],
    user["address2"],
    user["state"],
    user["city"],
    user["zipcode"],
    user["mobile_number"],
)
    signup_page.create_account_button.click()
    attach_screenshot(page, 'Account Created Page')

    account_created_page.continue_button.click()
    attach_screenshot(page, 'Home Page After Account Creation')

    home_page.logout.click()

    home_page.login_button_click()

    login_page.login(user['email'], user['password'])
    attach_screenshot(page, 'Home Page After Login')

    home_page.logged_in_as(user['name'])

    home_page.delete_account()

def test_login_user_with_incorrect_email_and_password(page: Page):

    user = generate_user()
    
    home_page = HomePage(page)

    login_page = LoginPage(page)

    home_page.open()
    home_page.verify_home_page_is_visible()
    attach_screenshot(page, "Home Page")

    home_page.login_button_click()
    attach_screenshot(page, 'Login Page')

    login_page.verify_login_to_your_account_is_visible()

    login_page.login(user['email'], user['password'])

    expect(login_page.your_email_or_password_is_incorrect).to_be_visible()

def test_logout_user(page: Page):

    user = generate_user()

    home_page = HomePage(page)

    login_page = LoginPage(page)

    signup_page = SignupPage(page)

    account_created_page = AccountCreatedPage(page)

    home_page.open()
    home_page.verify_home_page_is_visible()

    attach_screenshot(page, "Home Page")
    home_page.login_button_click()

    attach_screenshot(page, 'Login Page')
    login_page.verify_login_to_your_account_is_visible()

    login_page.signup(user['name'], user['email'])
    attach_screenshot(page, 'Signup Page')

    signup_page.fill_account_information(user['password'])

    signup_page.fill_address_information(
    user["first_name"],
    user["last_name"],
    user["company"],
    user["address"],
    user["address2"],
    user["state"],
    user["city"],
    user["zipcode"],
    user["mobile_number"],
)
    signup_page.create_account_button.click()

    account_created_page.continue_button.click()
    attach_screenshot(page, 'Home Page After Account Creation')

    home_page.logout.click()

    home_page.login_button_click()

    login_page.login(user['email'], user['password'])
    attach_screenshot(page, 'Home Page After Login')

    home_page.logged_in_as(user['name'])

    home_page.logout.click()

    expect(page).to_have_url('https://automationexercise.com/login')


def test_register_user_with_existing_email(page: Page):

    user = generate_user()

    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    account_created_page = AccountCreatedPage(page)

    home_page.open()
    home_page.verify_home_page_is_visible()

    attach_screenshot(page, "Home Page")

    home_page.login_button_click()
    login_page.verify_new_user_signup_is_visible()

    login_page.signup(user['name'], user['email'])

    signup_page.register_user(user)  

    account_created_page.continue_button.click()
    attach_screenshot(page, 'Home Page After Account Creation')

    home_page.logout.click()

    attach_screenshot(page, "Home Page")

    login_page.signup(user['name'], user['email'])

    expect(login_page.error_message).to_be_visible()
    attach_screenshot(page, 'Error Message')

def test_contact_us_form(page: Page):
    user = generate_user()
    file_path = Path(__file__).resolve().parents[1] / "requirements.txt"

    home_page = HomePage(page)
    contact_us_page = ContactUsPage(page)

    page.route(
        "**/*",
        lambda route: (
            route.abort()
            if (
                "googleads" in route.request.url
                or "googlesyndication" in route.request.url
                or "doubleclick.net" in route.request.url
                or "fonts.googleapis.com" in route.request.url
            )
            else route.continue_()
        )
    )

    home_page.open()
    home_page.verify_home_page_is_visible()

    attach_screenshot(page, "Home Page")

    home_page.click_contact_us_button()

    attach_screenshot(page, "Contact Us Page")
    expect(contact_us_page.get_in_touch).to_be_visible()

    contact_us_page.fill_contact_us_form(
        user["name"],
        user["email"],
        user["subject"],
        user["message"]
    )

    contact_us_page.upload_file(file_path)
    page.once("dialog", lambda dialog: dialog.accept())

    contact_us_page.submit()

    expect(contact_us_page.success_message).to_be_visible()
    attach_screenshot(page, "Success Message")

    contact_us_page.home_button.click()
    home_page.verify_home_page_is_visible()

def test_verify_test_cases_page(page: Page):

    home_page = HomePage(page)
    test_case_page = TestCasePage(page)

    home_page.open()
    home_page.verify_home_page_is_visible()

    attach_screenshot(page, "Home Page")

    home_page.click_test_cases_button()

    attach_screenshot(page, 'Test Cases Page')
    expect(test_case_page.test_cases_title).to_be_visible()


def test_verify_all_products_and_product_detail_page(page: Page):

    home_page = HomePage(page)

    products_page = ProductsPage(page)

    home_page.open()
    home_page.verify_home_page_is_visible()

    attach_screenshot(page, "Home Page")
    home_page.click_products_button() 

    products_page.verify_all_products_page_is_visible() 
    attach_screenshot(page, 'All Products Page')

    products_page.click_blue_top_view_product()

    expect(page).to_have_url('https://automationexercise.com/product_details/1')

    products_page.verify_product_details_is_visible()
    attach_screenshot(page, 'Product Details Page')

def test_search_product(page: Page):

    home_page = HomePage(page)

    products_page = ProductsPage(page)

    home_page.open()
    home_page.verify_home_page_is_visible()

    attach_screenshot(page, "Home Page")
    home_page.click_products_button() 

    products_page.verify_all_products_page_is_visible()
    attach_screenshot(page, 'All Products Page')

    products_page.search_product("Blue Top")

    expect(products_page.searched_products).to_be_visible()

    products_page.verify_searched_products_are_visible("Blue Top")

def test_verify_subscription_in_home_page(page: Page):

    user = generate_user()
    home_page = HomePage(page)

    home_page.open()
    home_page.verify_home_page_is_visible()

    home_page.verify_subscription_is_visible()

    home_page.subscribe(user['email'])

    expect(home_page.subscription_success_message).to_be_visible()
    attach_screenshot(page, 'Subscription Success Message')
