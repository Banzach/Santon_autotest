from pages.base_page import BasePage
from pages.locators import CategoryPageLocators
from pages.locators import CartPageLocators
import time

class CategoryPage(BasePage):
    
        #Жмем на фильтр "Экспресс доставка"
    def press_filter_epxress(self):
        self.is_element_visible_and_click(CategoryPageLocators.FILTER_EXPRESS)
        
        #Применяем фильтр по тултипу.Иногда не применяется, для того чтоб начал - попробовать дважды команду или time.sleep
    def apply_filter(self):
        self.is_element_visible_and_click(CategoryPageLocators.FILTER_BTN_SHOW)
        
        #Идем на страничку первого товара
    def go_to_cart_page(self):
        self.is_element_visible_and_click(CategoryPageLocators.ADD_TO_CART_FIRST_GOOD)
        

    
    
    
    
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