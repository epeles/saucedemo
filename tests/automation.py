from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import allure


class SauceDemoAutomation:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Open website: {url}")
    def open_website(self, url):
        self.driver.get(url)

    @allure.step("Login with username: {username} and password: {password}")
    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    @allure.step("Add items to cart: {item_ids}")
    def add_items_to_cart(self, item_ids):
        for item_id in item_ids:
            self.wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()
        assert self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))).text == str(
            len(item_ids)
        ), "Incorrect number of items in the cart"

    @allure.step("Go to cart")
    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item_name')))
        return len(items)

    @allure.step("Remove item from cart: {item_id}")
    def remove_item_from_cart(self, item_id):
        self.wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()

    @allure.step("Checkout with first name: {first_name}, last name: {last_name}, postal code: {postal_code}")
    def checkout(self, first_name, last_name, postal_code):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(last_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys(postal_code)
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    @allure.step("Finish purchase")
    def finish_purchase(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, "finish"))).click()

    @allure.step("Validate button styles")
    def validate_button_styles(self):
        back_home_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='back-to-products']"))
        )
        back_home_color = back_home_button.value_of_css_property("background-color")
        back_home_font_size = back_home_button.value_of_css_property("font-size")

        assert back_home_color == "rgba(61, 220, 145, 1)", f"Unexpected background color: {back_home_color}"
        assert back_home_font_size == "16px", f"Unexpected font size: {back_home_font_size}"

    @allure.step("Save screenshot: {file_name}")
    def save_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)
        allure.attach.file(file_name, attachment_type=allure.attachment_type.PNG)

    @allure.step("Logout")
    def logout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

    @allure.step("Quit driver")
    def quit(self):
        print("The tests ran successfully!")
        self.driver.quit()