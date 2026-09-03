from playwright.sync_api import expect
import allure

class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.blue_top = page.locator('[class="productinfo text-center"]').filter(has_text='Blue Top')
        self.all_products = page.locator('[class="title text-center"]').filter(has_text='All Products')
        self.blue_top_name = page.get_by_text("Blue Top")
        self.category = page.get_by_text("Category: Women > Tops")
        self.price = page.get_by_text("Rs. 500")
        self.availability = page.get_by_text("Availability: In Stock")
        self.condition = page.get_by_text("Condition: New")
        self.brand = page.get_by_text("Brand: Polo")
        self.search_product_input = page.locator('#search_product')
        self.searched_products = page.locator('[class="title text-center"]').filter(has_text='Searched Products')
        self.search_product_result = page.locator('[class="features_items"]')

    @allure.step("Verify all products page is visible")
    def verify_all_products_page_is_visible(self):
        expect(self.all_products).to_be_visible()
        expect(self.blue_top).to_be_visible()

    @allure.step("Click Blue Top and view product")
    def click_blue_top_view_product(self):
        self.page.locator('[href="/product_details/1"]').click()

    @allure.step("Verify product details are visible")
    def verify_product_details_is_visible(self):
        expect(self.blue_top_name).to_be_visible()
        expect(self.category).to_be_visible()
        expect(self.price).to_be_visible()
        expect(self.availability).to_be_visible()
        expect(self.condition).to_be_visible()
        expect(self.brand).to_be_visible()

    @allure.step("Search for product '{product_name}'")
    def search_product(self, product_name):
        self.search_product_input.fill(product_name)
        self.page.locator('#submit_search').click()

    @allure.step("Verify searched products are visible")
    def verify_searched_products_are_visible(self, product_name):
        expect(self.search_product_result.filter(has=self.page.get_by_text(product_name))).to_be_visible()
        