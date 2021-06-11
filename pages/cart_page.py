from pages.base_page import BasePage
from pages.locators import CartPageLocators

class CartPage(BasePage):

	    # Добавить товар в корзину из карточки товара
    def cart_page_add_to_basket(self):
        self.is_element_visible_and_click(CartPageLocators.CART_ADD_TO_BASKET)
    
        # Переходим в корзину через попап
    def go_to_basket_from_popup_cart(self):
        self.is_element_visible_and_click(CartPageLocators.POPUP_GO_TO_BASKET)
        
        # Запоминаем полную цену товара
    def remember_full_price(self):
        a = self.get_element_attribute(*CartPageLocators.FULL_PRICE)
    
        # Проверяем работу иконок избранного и сравнения
    def check_favorite_and_comparison(self):
        self.is_element_visible_and_click(CartPageLocators.ICON_COMPRASION)
        self.is_element_visible_and_click(CartPageLocators.ICON_FAVORITE)
        a = self.get_element_attribute(*CartPageLocators.FAVORITE_COUNT, 'textContent')
        b = self.get_element_attribute(*CartPageLocators.COMPRASION_COUNT, 'textContent')
        assert a == '1', 'Проблема в иконке избранного'
        assert b == '1', 'Проблема в иконке равнения'
        self.is_element_visible_and_click(CartPageLocators.ICON_COMPRASION)
        self.is_element_visible_and_click(CartPageLocators.ICON_FAVORITE)
        assert a == '0', 'Проблема при удалении товара из избранного'
        assert b == '0', 'Проблема при удалении товара из сравнения'
        

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
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