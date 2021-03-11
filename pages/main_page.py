from Last_Lesson.pages.base_page import BasePage
from Last_Lesson.pages.locators import MainPageLocators
from Last_Lesson.pages.login_page import LoginPage

class MainPage(BasePage): 
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)