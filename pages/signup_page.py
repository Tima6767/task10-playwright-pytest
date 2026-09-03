import allure

class SignupPage:

    def __init__(self, page):
        self.page = page
        self.name_input = page.locator('[data-qa="name"]')
        self.password_input = page.locator('[data-qa="password"]')
        self.day_of_birth = page.locator('[data-qa="days"]')
        self.month_of_birth = page.locator('[data-qa="months"]')
        self.year_of_birth = page.locator('#years')
        self.news_box = page.locator('#newsletter')
        self.special_offer_box = page.locator('#optin')
        self.first_name_input = page.locator('[data-qa="first_name"]')
        self.last_name_input = page.locator('[data-qa="last_name"]')
        self.company_input = page.locator('[data-qa="company"]')
        self.address_input = page.locator('[data-qa="address"]')
        self.second_address_input = page.locator('[data-qa="address2"]')
        self.country_dropdown = page.locator('[data-qa="country"]')
        self.state_input = page.locator('[data-qa="state"]')
        self.city_input = page.locator('[data-qa="city"]')
        self.zipcode_input = page.locator('[data-qa="zipcode"]')
        self.mobile_number_input = page.locator('[data-qa="mobile_number"]')
        self.create_account_button = page.locator('[data-qa="create-account"]')
        

    @allure.step("Fill account information with password")
    def fill_account_information(self, password):
        self.password_input.fill(password)
        self.day_of_birth.click()
        self.day_of_birth.select_option(value="1")
        self.month_of_birth.click()
        self.month_of_birth.select_option(value="1")
        self.year_of_birth.click()
        self.year_of_birth.select_option(value="2000")
        self.news_box.click()
        self.special_offer_box.click()

    @allure.step("Fill address information")
    def fill_address_information(self, first_name, last_name, company, address, address2, state, city, zipcode, mobile_number):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.company_input.fill(company)
        self.address_input.fill(address)
        self.second_address_input.fill(address2)
        self.country_dropdown.click()
        self.country_dropdown.select_option(value="Israel")
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_number_input.fill(mobile_number)

    @allure.step("Register user")
    def register_user(self, user):
        self.fill_account_information(user['password'])

        self.fill_address_information(
        user['first_name'],
        user['last_name'],
        user['company'],
        user['address'],
        user['address2'],
        user['state'],
        user['city'],
        user['zipcode'],
        user['mobile_number']
        )
        self.create_account_button.click()

    

