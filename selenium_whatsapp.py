from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to chromedriver (adjust the path to where you have your chromedriver)
s = Service("chromedriver-mac-arm64/chromedriver")

# Now use the Service object when creating the driver
driver = webdriver.Chrome(service=s)


def send_whatsapp_message(phone_number, message):
    try:
        # Navigate to the URL
        driver.get(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")

        # Wait for the send button to be clickable
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='compose-btn-send']")
            )
        )

        # Find and click the send button
        send_btn = driver.find_element(
            By.XPATH, "//button[@data-testid='compose-btn-send']"
        )
        send_btn.click()

    except Exception as e:
        print(f"An error occurred: {e}")


# Log in to WhatsApp Web by scanning the QR code
driver.get("https://web.whatsapp.com")
input("Scan QR Code, then press Enter to continue...")

# Example usage
contacts = ["+9122345", "+9112344"]
message = "Hi, sent from Python using Selenium!"
for phone in contacts:
    send_whatsapp_message(phone, message)

# You may choose to keep the browser open or close it
# driver.quit()
