class TestCasePage:
    __test__ = False

    def __init__(self, page):
        self.page = page
        self.test_cases_title = page.locator('[class="title text-center"]').filter(has_text='Test Cases')
        self.test_case_1 = page.locator("div.single-test > h2")
        self.test_case_2 = page.locator("div.single-test:nth-child(2) > h2")
        self.test_case_3 = page.locator("div.single-test:nth-child(3) > h2")
        self.test_case_4 = page.locator("div.single-test:nth-child(4) > h2")
        self.test_case_5 = page.locator("div.single-test:nth-child(5) > h2")
        self.test_case_6 = page.locator("div.single-test:nth-child(6) > h2")

    def verify_test_cases_page_is_visible(self):
        assert self.test_cases_title.is_visible(), "Test Cases title is not visible"
        assert self.test_case_1.is_visible(), "Test Case 1 is not visible"
        assert self.test_case_2.is_visible(), "Test Case 2 is not visible"
        assert self.test_case_3.is_visible(), "Test Case 3 is not visible"
        assert self.test_case_4.is_visible(), "Test Case 4 is not visible"
        assert self.test_case_5.is_visible(), "Test Case 5 is not visible"
        assert self.test_case_6.is_visible(), "Test Case 6 is not visible"  
