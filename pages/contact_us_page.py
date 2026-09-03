import allure

class ContactUsPage:
    __test__ = False

    def __init__(self, page):
        self.page = page
        self.get_in_touch = page.get_by_text('GET IN TOUCH')
        self.name_input = page.locator('[data-qa="name"]')
        self.email_input = page.locator('[data-qa="email"]')
        self.subject_input = page.locator('[data-qa="subject"]')
        self.message_input = page.locator('[data-qa="message"]')
        self.submit_button = page.locator('[data-qa="submit-button"]')
        self.file_input = page.locator('[class="form-control"]').get_by_role("button", name="Choose File")
        self.success_message = page.locator("#contact-page .status.alert.alert-success").filter(has_text="Success! Your details have been submitted successfully.")
        self.home_button = page.get_by_role("link", name=" Home")

    @allure.step("Fill contact us form with name, email, subject, message")
    def fill_contact_us_form(self, name, email, subject, message):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_input.fill(message)
        
    @allure.step("Upload file with file path")
    def upload_file(self, file_path):
        self.file_input.set_input_files(file_path)

    @allure.step("Submit contact us form")
    def submit(self):
        self.submit_button.click()

