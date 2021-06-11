from pages.base_page import BasePage
from pages.locators import MainPageLocators
import time
class MainPage(BasePage):

	# Проверка верхнего баннера
    def check_mainBanners(self):
        self.is_element_present(*MainPageLocators.DROP_DOWN_WC)
        self.is_element_visible_and_click(MainPageLocators.ARROW_PREV_BANNER)
        time.sleep(0.5)
        self.is_element_visible_and_click(MainPageLocators.ARROW_NEXT_BANNER)
        self.is_element_visible_and_click(MainPageLocators.BANNER)	
       
    # Проверяем отображаемые пункты меню 
    def check_top_menu(self):
        category_list = ['Мебельный гарнитур', 'Зона ванны', 'Зона душа', 'Общая зона', 'Стояк канализации']
        
        self.is_element_visible_and_click(MainPageLocators.DROP_DOWN_CATALOG)
        self.is_element_visible_and_click(MainPageLocators.DROP_DOWN_WC)
      #  self.get_list_of_elements(*MainPageLocators.LIST_OF_CATEGORY)
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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