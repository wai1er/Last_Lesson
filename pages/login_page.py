from Last_Lesson.pages.base_page import BasePage
from Last_Lesson.pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "No login url" 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"
    
    def register_new_user(self, email, password):
        email_input=self.browser.find_element(*LoginPageLocators.EMAIL)
        password1_input=self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password2_input=self.browser.find_element(*LoginPageLocators.PASSWORD2)
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        button_submit=self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        button_submit.click()