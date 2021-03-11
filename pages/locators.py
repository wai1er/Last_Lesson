from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_REG = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_REG_CHECK = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    SUM_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert.alert-safe.alert-noicon.alert-info.fade.in div p:nth-child(1) strong")