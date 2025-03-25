
from pages.drivers import Drivers
from pages.saucedemo_page import SaucedemoPage
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SaucedemoTest:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = None
        self.saucedemo_page = None
        self.wait = None

    def setup(self):
        logging.info("Setting up browser")
        self.browser = Drivers().chrome()
        self.saucedemo_page = SaucedemoPage(driver=self.browser)
        self.wait = WebDriverWait(self.browser, 10)

    def teardown(self):
        logging.info("Tearing down browser")
        self.browser.quit()

    def safe_click(self, element):
        try:
            self.wait.until(EC.element_to_be_clickable(element.locator)).click()
            logging.info(f"Clicked on element: {element}")
        except (TimeoutException, ElementClickInterceptedException) as e:
            logging.warning(f"Failed to click element: {element}. Reason: {e}")

    def wait_for_element_text(self, element, text):
        try:
            self.wait.until(EC.text_to_be_present_in_element(element.locator, text))
            logging.info(f"Element {element} has text: {text}")
        except TimeoutException:
            logging.error(f"Expected text '{text}' not found in {element}")
            raise

    def run(self):
        self.setup()
        try:
            logging.info("Opening login page")
            self.saucedemo_page.go()
            self.wait_for_element_text(self.saucedemo_page.swaglabs_login_logo, 'Swag Labs')

            self.login()

            self.safe_click(self.saucedemo_page.burger_menu_button)
            self.wait_for_element_text(self.saucedemo_page.logout_sidebar_link, 'Logout')

            self.wait_for_element_text(self.saucedemo_page.page_title, 'Products')
            item_name = self.saucedemo_page.item_5_title_link_inventory.text()

            self.safe_click(self.saucedemo_page.item_5_title_link_inventory)
            self.wait_for_element_text(self.saucedemo_page.back_to_products_button, 'Back to products')

            assert self.saucedemo_page.item_5_title_link_detail.text() == item_name

            self.safe_click(self.saucedemo_page.add_to_cart_item_5)
            self.wait_for_element_text(self.saucedemo_page.remove_item_5, 'Remove')

            self.safe_click(self.saucedemo_page.shopping_cart_button)
            self.wait_for_element_text(self.saucedemo_page.page_title, 'Your Cart')
            assert self.saucedemo_page.item_5.text() == 'Sauce Labs Fleece Jacket'

            self.safe_click(self.saucedemo_page.checkout_button)
            self.wait_for_element_text(self.saucedemo_page.page_title, 'Checkout: Your Information')

            self.enter_shipping_payment_info()
            self.safe_click(self.saucedemo_page.continue_button)

            self.wait_for_element_text(self.saucedemo_page.page_title, 'Checkout: Overview')
            assert self.saucedemo_page.item_5.text() == 'Sauce Labs Fleece Jacket'

            self.handle_random_popups()
            self.logout()

        except Exception as e:
            logging.error(f"Test failed: {e}")
        finally:
            self.teardown()

    def login(self):
        logging.info("Logging in")
        self.saucedemo_page.username_input.input_text(self.username)
        self.saucedemo_page.password_input.input_text(self.password)
        self.safe_click(self.saucedemo_page.login_button)

    def enter_shipping_payment_info(self):
        logging.info("Entering shipping and payment info")
        self.saucedemo_page.first_name_input_text.input_text('Jan')
        self.saucedemo_page.last_name_input_text.input_text('Novak')
        self.saucedemo_page.postal_code_input_text.input_text('10400')

    def logout(self):
        logging.info("Logging out")
        self.safe_click(self.saucedemo_page.burger_menu_button)
        self.safe_click(self.saucedemo_page.logout_sidebar_link)
        assert self.saucedemo_page.login_button is not None

    def handle_random_popups(self):
        logging.info("Checking for random popups/modals")
        try:
            popup = self.saucedemo_page.random_popup
            if popup.is_displayed():
                logging.info("Popup detected, closing it")
                self.safe_click(self.saucedemo_page.popup_close_button)
        except (NoSuchElementException, AttributeError):
            logging.info("No popup appeared")

if __name__ == "__main__":
    test = SaucedemoTest('standard_user', 'secret_sauce')
    test.run()
    print('Test completed')
