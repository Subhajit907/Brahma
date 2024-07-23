from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Set a wait time
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Load the application
    driver.get("https://console.brahma.fi")

    # Step 2: Click on "Connect Wallet"
    connect_wallet_button = wait.until(
        EC.element_to_be_clickable(("xpath", "//button[contains(text(), 'Connect Wallet')]"))
        )
    connect_wallet_button.click()

    # Step 2.1: Wait for the modal to appear
    wallet_modal = wait.until(
        EC.visibility_of_element_located(("xpath", "//div[contains(@class, 'wallet-modal')]"))

        )
    # Button for MetaMask with specific text
    metamask_button = wait.until(
        EC.element_to_be_clickable(("xpath", "//button[contains(text(), 'MetaMask')]"))

        )
    metamask_button.click()

    #waiting for confirmations or handling any popups from the wallet.

except Exception as e:
    print(f"An error occurred while handling the wallet connection: {e}")

    # Step 3: Click on "Sign Message"
    sign_message_button = wait.until(
        EC.element_to_be_clickable(("xpath", "//button[contains(text(), 'Sign Message')]"))
    )
    sign_message_button.click()


    # Step 5: Select UI - testing console
    testing_console_link = wait.until(
        EC.element_to_be_clickable(("xpath", "//a[contains(text(), 'UI - Testing Console')]"))
    )
    testing_console_link.click()

    # Step 6: Verify that we are on the correct page
    wait.until(EC.title_contains("Dashboard"))

    # Step 7: Take a screenshot
    driver.save_screenshot('dashboard_screenshot.png')

    # Step 8: Assert the text below UI testing
    ui_testing_text = wait.until(
        EC.visibility_of_element_located(("xpath", "//div[contains(text(), '$0.00')]"))
    )

    assert ui_testing_text.is_displayed() and ui_testing_text.text == "$0.00", "Text assertion Passed"

finally:
    driver.quit()
