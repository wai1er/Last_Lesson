from Last_Lesson.pages.base_page import BasePage
from Last_Lesson.pages.locators import MainPageLocators
from Last_Lesson.pages.login_page import LoginPage

class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url) 
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"