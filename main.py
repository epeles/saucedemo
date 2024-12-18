from config import get_driver
from automation import SauceDemoAutomation
from config import SAUCEDO_USERNAME, SAUCEDO_PASSWORD, FIRST_NAME, LAST_NAME, POSTAL_CODE

def main():
    driver = get_driver()
    automation = SauceDemoAutomation(driver)
    
    try:
        automation.open_website("https://www.saucedemo.com/")
        automation.login(SAUCEDO_USERNAME, SAUCEDO_PASSWORD)
        automation.add_items_to_cart([
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bike-light",
            "add-to-cart-sauce-labs-fleece-jacket"
        ])
        automation.go_to_cart()
        automation.remove_item_from_cart("remove-sauce-labs-backpack")
        automation.checkout(FIRST_NAME, LAST_NAME, POSTAL_CODE)
        automation.save_screenshot("screenshot1.png")
        automation.finish_purchase()
        automation.validate_button_styles()
        automation.logout()
    finally:
        automation.quit()

if __name__ == "__main__":
    main()