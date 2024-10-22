import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        # service_obj = Service(
        #     "C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        # driver = webdriver.Chrome(service=service_obj)
        #
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        # driver.maximize_window()

        homepage = HomePage(self.driver)


        # homepage.getName().send_keys("Moumita")
        homepage.getName().send_keys(getData[0])

        driver.find_element(By.NAME, "email").send_keys("moumitajoardar95@gmail.com")
        driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        driver.find_element(By.ID, "exampleCheck1").click()
        driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Moumita")
        driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello again")
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

        dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown.select_by_visible_text(getData[2])
        dropdown.select_by_index(1)

        message = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "Success" in message  # assert use to check pass or fail


    @pytest.fixture(params=[("Moumita","Joardar","Female"),("Rahul","Shetty","Male")])
    def getData(self,request):
        return request.param



