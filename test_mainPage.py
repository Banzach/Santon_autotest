from pages.base_page import BasePage
from pages.main_page import MainPage
import time

link = "https://santehnika-online.ru"

def test_main_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.check_mainBanners()
    main_page.return_to_page()
    main_page.check_top_menu()
    