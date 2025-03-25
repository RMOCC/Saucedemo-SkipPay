from selenium.webdriver.common.by import By

class SaucedemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"

    def go(self):
        self.driver.get(self.base_url)

    # Locators (přidáš si další podle potřeby)
    @property
    def swaglabs_login_logo(self):
        return self.driver.find_element(By.CLASS_NAME, "login_logo")

    @property
    def username_input(self):
        return self.driver.find_element(By.ID, "user-name")

    @property
    def password_input(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def login_button(self):
        return self.driver.find_element(By.ID, "login-button")

    @property
    def burger_menu_button(self):
        return self.driver.find_element(By.ID, "react-burger-menu-btn")

    @property
    def logout_sidebar_link(self):
        return self.driver.find_element(By.ID, "logout_sidebar_link")

    @property
    def page_title(self):
        return self.driver.find_element(By.CLASS_NAME, "title")

    @property
    def shopping_cart_button(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    @property
    def checkout_button(self):
        return self.driver.find_element(By.ID, "checkout")

    @property
    def first_name_input_text(self):
        return self.driver.find_element(By.ID, "first-name")

    @property
    def last_name_input_text(self):
        return self.driver.find_element(By.ID, "last-name")

    @property
    def postal_code_input_text(self):
        return self.driver.find_element(By.ID, "postal-code")

    @property
    def continue_button(self):
        return self.driver.find_element(By.ID, "continue")

    @property
    def back_to_products_button(self):
        return self.driver.find_element(By.ID, "back-to-products")

    # Příklad práce s produktem
    @property
    def item_5_title_link_inventory(self):
        return self.driver.find_element(By.ID, "item_5_title_link")

    @property
    def add_to_cart_item_5(self):
        return self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")

    @property
    def remove_item_5(self):
        return self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket")

    @property
    def item_5(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name")

    @property
    def item_5_title_link_detail(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_name")
