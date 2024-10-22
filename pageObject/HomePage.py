from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver


    shop = (By.LINK_TEXT,"Shop")
    name = (By.CSS_SELECTOR,"input[name='name']")

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)



