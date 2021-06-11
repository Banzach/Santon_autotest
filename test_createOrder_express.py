from pages.base_page import BasePage
from pages.create_express_order import CreateExpressOrder

link = "https://santehnika-online.ru/vanny/akrilovye/"
link_dev = "https://<sant>:<onsant123,>@dev17.sant-on.ru/vanny/akrilovye/"

def test_create_order_onlyExpress(browser):
    create_order_express = CreateExpressOrder(browser, link)
    create_order_express.open()
    create_order_express.press_filter_epxress()
    create_order_express.apply_filter()
    create_order_express.go_to_cart_page()
    create_order_express.cart_page_add_to_basket()
    create_order_express.remember_full_price_on_card()
    create_order_express.go_to_basket_from_popup_cart()
    create_order_express.remember_full_price_on_checkout()
    create_order_express.assert_price_with_checkoutPrice()
    create_order_express.go_to_checkout()
    create_order_express.fill_phone_field()
    create_order_express.choose_pickup_method()
    create_order_express.get_price_on_checkout()
    create_order_express.fill_order_coment()
    create_order_express.create_order() 