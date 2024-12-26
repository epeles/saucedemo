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


@allure.title("SauceDemo Full Purchase Flow")
def test_sauce_demo_purchase_flow(driver):
    """Test case for the full purchase flow in SauceDemo."""
    automation = SauceDemoAutomation(driver)

    with allure.step("Open SauceDemo website"):
        automation.open_website("https://www.saucedemo.com/")

    with allure.step("Log in to SauceDemo"):
        automation.login(SAUCEDO_USERNAME, SAUCEDO_PASSWORD)

    with allure.step("Add items to cart"):
        automation.add_items_to_cart([
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bike-light",
            "add-to-cart-sauce-labs-fleece-jacket"
        ])

    with allure.step("Go to the cart"):
        automation.go_to_cart()

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