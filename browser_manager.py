import undetected_chromedriver as uc

class BrowserManager:
    def __init__(self):
        self.driver = None

    def start(self):
        if self.driver is None:
            options = uc.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            self.driver = uc.Chrome(options=options)
        return self.driver

    def stop(self):
        if self.driver:
            self.driver.quit()
            self.driver = None