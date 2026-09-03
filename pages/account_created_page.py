class AccountCreatedPage:

    def __init__(self, page):
        self.page = page
        self.account_created = page.get_by_text('Account Created!')
        self.continue_button = page.locator('[data-qa="continue-button"]')