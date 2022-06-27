import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setup class')
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_email_id_password(self):
       
        self.driver.get("http://localhost:4200/login")
        self.driver.find_element_by_id(
            "email").send_keys("dev@inesssolutions.com")
        password = self.driver.find_element_by_id("pwd").send_keys("Test@123")
        password = self.driver.find_element_by_id("pwd").send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(
            "/html/body/app-root/app-login/form/div/div/div[2]/div[3]/div/button[1]").click()
        print("valid")
        time.sleep(2)
        ele = self.driver.find_element_by_name("userDisplayName")
        print(self.driver.current_url)
        # print(ele.is_displayed())

    def test_valid_email_id_invalid_password(self):
        self.driver.get("http://localhost:4200/login")
        self.driver.find_element_by_id(
            "email").send_keys("dev@inesssolutions.com")
        self.driver.find_element_by_id("pwd").send_keys("hello")
        # time.sleep(2)
        self.driver.find_element_by_id("pwd").send_keys(Keys.TAB)
        time.sleep(2)
        print("invalid")
        self.driver.find_element_by_xpath(
            "/html/body/app-root/app-login/form/div/div/div[2]/div[3]/div/button[1]").click()
        time.sleep(2)
        print(self.driver.current_url)

    def test_invalid_email_id_valid_password(self):
        self.driver.get("http://localhost:4200/login")
        self.driver.find_element_by_id("email").send_keys("dev@ines.com")
        self.driver.find_element_by_id("pwd").send_keys("Test@123")
        # time.sleep(2)
        self.driver.find_element_by_id("pwd").send_keys(Keys.TAB)
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/app-root/app-login/form/div/div/div[2]/div[3]/div/button[1]").click()
        time.sleep(2)
        print("invalid")
        time.sleep(1)
        toast=self.driver.find_element_by_id("toast-container")
        print(toast)
        print(self.driver.current_url)
if __name__ == '__main__':
    unittest.main()
    $('#btnOneDInternalSave').click(function(e) {
        e.preventDefault();

        $.ajax({
            success: function(res) {
                toastr.success("Internal Stackholders data has been saved");
            },
            error: function(res) {
                toastr.error("Invalid Data");
            }
        });
        return false;
    });
    $('#btnOneDExternalSave').click(function(e) {
        e.preventDefault();

        $.ajax({
            success: function(res) {
                toastr.success("External Stackholders data has been saved");
            },
            error: function(res) {
                toastr.error("Invalid Data");
            }
        });
        return false;
    });