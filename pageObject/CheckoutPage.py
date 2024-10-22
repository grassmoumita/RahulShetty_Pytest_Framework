from selenium.webdriver.common.by import By


class CheckOut:


    def __init__(self,driver):
        self.driver = driver

    product = (By.XPATH, "//div[@class='card h-100']")

    def getProductName(self):
        return self.driver.find_elements(*CheckOut.product)




