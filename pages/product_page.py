from Last_Lesson.pages.base_page import BasePage
from Last_Lesson.pages.locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class ProductPage(BasePage): 
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_add_message(self):
        message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE).text
        assert "The shellcoder's handbook" in message, "Wrong add message"

    def check_sum_message(self):
        sum_message = self.browser.find_element(*ProductPageLocators.SUM_MESSAGE).text
        assert "9,99 £" in sum_message, "Wrong sum message"
