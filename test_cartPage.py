from pages.base_page import BasePage
from pages.cart_page import CartPage
import time

link = "https://santehnika-online.ru/product/akrilovaya_vanna_aquanet_bright_180x70_s_karkasom/"

def test_cart_page(browser):
    cart_page = CartPage(browser, link)
    cart_page.open()
    cart_page.check_favorite_and_comparison()
    #cart.page()

    