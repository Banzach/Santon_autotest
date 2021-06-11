from pages.base_page import BasePage
from pages.locators import CategoryPageLocators
from pages.locators import CartPageLocators
from pages.locators import BasketPageLocators
from pages.locators import CheckoutPageLocators

class CreateExpressOrder(BasePage):
    
        # Жмем на фильтр "Экспресс доставка"
    def press_filter_epxress(self):
        self.is_element_visible_and_click(CategoryPageLocators.FILTER_EXPRESS)
        
        # Применяем фильтр по тултипу.Иногда не применяется, для того чтоб начал - попробовать дважды команду или time.sleep
    def apply_filter(self):
        self.is_element_visible_and_click(CategoryPageLocators.FILTER_BTN_SHOW)
        
        # Идем на страничку первого товара
    def go_to_cart_page(self):
        self.is_element_visible_and_click(CategoryPageLocators.ADD_TO_CART_FIRST_GOOD)
        
        # Добавляем товар в корзину 
    def cart_page_add_to_basket(self):
        self.is_element_visible_and_click(CartPageLocators.CART_ADD_TO_BASKET)
    
        # Переходим в корзину через попап
    def go_to_basket_from_popup_cart(self):
        self.is_element_visible_and_click(CartPageLocators.POPUP_GO_TO_BASKET)
        
        # Переходим на страницу оформления заказа
    def go_to_checkout(self):
        self.is_element_visible_and_click(BasketPageLocators.GO_TO_CHECKOUT)
        
        # Запоминаем полную цену товара в карточке
    def remember_full_price_on_card(self):
        global a
        a = self.get_element_attribute(*CartPageLocators.FULL_PRICE, 'content') 
        
        # Запоминаем полную цену товара в корзине
    def remember_full_price_on_checkout(self):
        global b 
        b = self.get_element_attribute(*CartPageLocators.FULL_PRICE, 'content') 
        
        # Заполняем номер телефона(1)
    def fill_phone_field(self):
        self.input_message(*CheckoutPageLocators.CUSTOMER_PHONE,"9296722610")
    
        # Заполняем поле с комментом
    def fill_order_coment(self):
        self.input_message(*CheckoutPageLocators.ORDER_COMMENT,"1140")
        
        # Сравниваем цены из карточки и из корзины
    def assert_price_with_checkoutPrice(self):
        assert a == b, "Цена в карточке товара не совпадает с ценой товара в корзине"
        
        # Создаем заказ
    def create_order(self):
        self.is_element_visible_and_click(CheckoutPageLocators.CREATE_ORDER)
    
        # Выбираем способ доставки = Самовывоз
    def choose_pickup_method(self):
        self.is_element_visible_and_click(CheckoutPageLocators.PICKUP)
    
        # Сравниваем итоговую стоимость заказа с самовывозом с ценой добавленного овара
    def get_price_on_checkout(self):
        c = self.get_only_numbers_from_content(*CheckoutPageLocators.TOTAL_PRICE_CHECKOUT, 'textContent')
        assert c == a, "Итоговая цена при самовывозе не совпадает с ценой добавленного товара"
        print(c, a)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
		 # Добавляем товар в корзину Santehnika. ПЕРЕНЕСТИ В КАРТ ПЕЙДЖ
    #def add_goods_to_cart(self):
    #    self.scroll_page_to(*CartPageLocators.CART_ADD_TO_BASKET)
     #   self.is_element_visible_and_click(CartPageLocators.CART_ADD_TO_BASKET)

				
				
				
				#def guest_use_search(self):
    #    assert self.is_element_present(*BasePageLocators.SEARCH_BAR), 'элемент SEARCH_BAR не найден'
    #    self.input_message(*BasePageLocators.SEARCH_BAR, 'сумка')
    #    go_search_button = self.is_element_visible_and_click(BasePageLocators.GO_SEARCH_BUTTON)
    #    search_result = self.browser.find_element(*BasePageLocators.SEARCH_RESULTS)
    #    assert int(search_result.text) >= 300, "Следует проверить агент переиндексации поискового модуля" 
    #    print(f"Найдено {search_result.text}")
    
    #def go_to_sections_page_from_main(self):
    #    choose_section_man = self.is_element_visible_and_click(BasePageLocators.CHOOSE_SECTION_MAN)
    #    choose_section_man_bags = self.is_element_visible_and_click(BasePageLocators.CHOOSE_SECTION_MAN_BAGS)
    #    print(f"Текущая страница: {self.browser.current_url}")
    #    assert self.browser.current_url == "https://www.imperiasumok.ru/catalog/muzhskie-sumki/", "Текущая страница != /muzhskie-sumki/ "