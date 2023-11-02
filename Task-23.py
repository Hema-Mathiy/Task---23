from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class dragdrop:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.actions = ActionChains(self.driver)

    def logging(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def drag_drop(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            frame = self.driver.find_element(By.CLASS_NAME, value='demo-frame')
            self.driver.switch_to.frame(frame)
            drag_obj = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Drag me to my target']")))
            drop_destinee = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Drop here']")))
            self.actions.drag_and_drop(drag_obj, drop_destinee).perform()
            sleep(2)
        except :
            print("unable to drop the box")
        finally:
            self.driver.quit()

url = "https://jqueryui.com/droppable/"
dd = dragdrop(url)
dd.logging()
dd.drag_drop()
