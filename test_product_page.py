from Last_Lesson.pages.product_page import ProductPage
from Last_Lesson.pages.login_page import LoginPage
from Last_Lesson.pages.basket_page import BasketPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        register_page = LoginPage(browser, link)
        register_page.open()
        email = str(time.time()) + "@fakemail.com"
        password = "ILY12345678"
        register_page.register_new_user(email, password)
        register_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductPage(browser, link)
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_add_message()
        page.check_sum_message()
            
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page=BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.text_basket_is_empty_should_be_present()

@pytest.mark.skip
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  #pytest.param(
                                     # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", 
                                    #  marks=pytest.mark.xfail
                                  #),
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser):
    #link = ('{}'.format(link))
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_add_message()
    page.check_sum_message()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()