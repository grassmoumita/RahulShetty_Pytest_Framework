import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObject.CheckoutPage import CheckOut
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_endtoend(self):

        log = self.getlogger()

        homepage = HomePage(self.driver)
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        homepage.shopItem().click()

        checkoutpage = CheckOut(self.driver)
        products = checkoutpage.getProductName()
        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for i in products:
            productname = i.find_element(By.XPATH, "div/h4/a").text
            if productname == "Blackberry":
                i.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.verifylinkpresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        log.info("Text received from application is" + success_text)

        assert "Success! Thank you!" in success_text  # partial assertion



