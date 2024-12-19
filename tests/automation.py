from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class SauceDemoAutomation:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_website(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    def add_items_to_cart(self, item_ids):
        for item_id in item_ids:
            self.wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()
        # More robust assertion, handles potential string formatting differences
        assert self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))).text == '3', "Incorrect number of items in cart"

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        # More robust check for items, using a better locator if available (e.g., data-test attribute) and len()
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item_name'))) # Or better locator
        assert len(items) == 3, f"Expected 3 items in cart, but found {len(items)}"


    def remove_item_from_cart(self, item_id):
        self.wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()

    def checkout(self, first_name, last_name, postal_code):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(last_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys(postal_code)
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def finish_purchase(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, "finish"))).click()

    def validate_button_styles(self):  # Example with data-test attribute, if available. Use a better locator as per your page.
        back_home_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='back-to-products']"))) # Use data-test or other suitable locator
        back_home_color = back_home_button.value_of_css_property("background-color")
        back_home_font_size = back_home_button.value_of_css_property("font-size")

        assert back_home_color == "rgba(61, 220, 145, 1)", f"Unexpected background color: {back_home_color}"
        assert back_home_font_size == "16px", f"Unexpected font size: {back_home_font_size}"

    def save_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    def logout(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
            self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
        except StaleElementReferenceException:  # Handle stale element
            self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

    def quit(self):
        self.driver.quit()
