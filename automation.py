from selenium.webdriver.common.by import By
import time

class LinkedInAutomation:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(2)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

    def go_to_profile_and_connect(self, profile_url, message_if_connected=None):
        self.driver.get(profile_url)
        time.sleep(3)
        try:
            connect_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Connect')]")
            connect_button.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[@aria-label='Send now']").click()
        except:
            print("Already connected or no connect button found.")
            if message_if_connected:
                self.send_message(message_if_connected)

    def send_message(self, message):
        try:
            self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Message')]").click()
            time.sleep(2)
            textarea = self.driver.find_element(By.TAG_NAME, "textarea")
            textarea.send_keys(message)
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]").click()
        except Exception as e:
            print("Error sending message:", e)