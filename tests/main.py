import pytest
from config import get_driver
from automation import SauceDemoAutomation
from config import SAUCEDO_USERNAME, SAUCEDO_PASSWORD, FIRST_NAME, LAST_NAME, POSTAL_CODE
import allure


@pytest.fixture
def driver():
    """Fixture to initialize and quit the WebDriver."""
    driver = get_driver()
    yield driver
    driver.quit()

@allure.feature("Valid Login and Purchase") 
@allure.story("Complete Purchase Flow") 
def test_sauce_demo_purchase_flow(driver):
    """Test case for the full purchase flow in SauceDemo."""
    automation = SauceDemoAutomation(driver)

    with allure.step("Open SauceDemo website"):
        automation.open_website("https://www.saucedemo.com/")

    with allure.step("Log in to SauceDemo"):
        automation.login(SAUCEDO_USERNAME, SAUCEDO_PASSWORD)

    item_ids = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bike-light",
        "add-to-cart-sauce-labs-fleece-jacket"
    ]
    with allure.step("Add items to cart"):
        automation.add_items_to_cart(item_ids)

    with allure.step("Filter items by price (low to high)"):
        automation.filter_items()
    
    with allure.step("Go to the cart and verify item count"):
        cart_item_count = automation.go_to_cart()
        assert cart_item_count == len(item_ids), f"Expected {len(item_ids)} items in cart, but found {cart_item_count}"

    with allure.step("Remove an item from the cart"):
        automation.remove_item_from_cart("remove-sauce-labs-backpack")

    with allure.step("Checkout items"):
        automation.checkout(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    with allure.step("Take a screenshot after checkout"):
        automation.save_screenshot("screenshot1.png")

    with allure.step("Finish the purchase process"):
        automation.finish_purchase()

    with allure.step("Validate button styles on the confirmation page"):
        automation.validate_button_styles()

    with allure.step("Log out of SauceDemo"):
        automation.logout()

@allure.feature("Invalid Login Handling")  # Group related test cases
@allure.story("Incorrect Password") 
def test_sauce_demo_invalid_login(driver):
    """Test case for the invalid login flow in SauceDemo."""
    automation = SauceDemoAutomation(driver)

    with allure.step("Open SauceDemo website"):
        automation.open_website("https://www.saucedemo.com/")

    with allure.step("Log in to SauceDemo"):
        automation.login(SAUCEDO_USERNAME, "invalid_password")

    with allure.step("Validate error message"):
        automation.validate_error_msg()
