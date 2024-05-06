from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def automate_whatsapp():
    # Setup WebDriver
    driver = webdriver.Chrome()  # Specify the path if it's not in your PATH

    driver.get("https://web.whatsapp.com")
    print("Please scan the QR Code. Waiting for WhatsApp Web to load...")

    # Wait for some element that indicates the page has loaded
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "canvas[aria-label='Scan me!']")
            )
        )

        print("Logged in. Now navigating chats...")

        # You'll need to update these selectors based on the current structure of WhatsApp Web
        chat_selector = "div[class*='_2nY6U']"  # Update this selector
        message_box_selector = "div[contenteditable='true']"  # Update this selector

        chats = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, chat_selector))
        )

        for chat in chats:
            chat.click()  # Open the conversation
            time.sleep(2)  # Wait for the chat to load

            message_box = driver.find_element(By.CSS_SELECTOR, message_box_selector)
            if message_box.text.strip() != "":
                message_box.send_keys(Keys.ENTER)  # Press Enter to send the message
                time.sleep(1)  # Wait a bit before moving to the next chat

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Optionally keep the browser open for a while before closing
        time.sleep(10)
        driver.quit()


# Example usage
automate_whatsapp()
