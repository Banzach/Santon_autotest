from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re

class BasePage():

    # Создаем конструктор, методы которого будут вызываться при создании нового объекта
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)
   
   # Переходим на другую вкладку
    def switch_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        
    # Переходим по ссылке
    def open(self):
        self.browser.get(self.url)  
    
    # Возвращаемся на предыдущую страницу
    def return_to_page(self):
        self.browser.back()
        
    # Проверяем, виден ли элемент и кликаем по нему
    def is_element_visible_and_click(self, locator, time=20):
        try:
            is_element_visible = WebDriverWait(self.browser,time).until(
            EC.visibility_of_element_located(locator)).click()
        except(NoSuchElementException):
            return False
        return is_element_visible
        
    # Проверяем наличие элемента на странице  
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False, "Element" + what + "is not present"
        return True
    
    # Ввод текст в какое-нибудь поле
    def input_message(self, how, what, message):
        input_field = self.browser.find_element(how, what)
        input_field.click()
        input_field.send_keys(message)
    
    # Скроллим страницу до нужного элемента
    def scroll_page_to(self, how, what):  
        target = self.browser.find_element(how, what)
        target.location_once_scrolled_into_view
    
    # Получаем значение аттрибута элемента 
    def get_element_attribute(self, how, what, attribute):
        return self.browser.find_element(how, what).get_attribute(attribute)
        
    # Оставляем в атрибуте только цифры
    def get_only_numbers_from_content(self, how, what, attribute):
        get_numbers_from = self.browser.find_element(how, what).get_attribute(attribute)
        numbers = re.sub('[^0-9]', '', get_numbers_from)
        return numbers
    
    
    
    
    # Ждем, пока у элемента не появится нужный класс
    #def is_element_have_attribute(self, locator, time=10):
    #    is_element_have = WebDriverWait(self.browser,time).until(
    #    EC.element_attribute_to_include(locator, [class= 'active'])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    # Пользователь может перейти на страницу авторизации с любой страницы сайта
    #def user_can_go_to_login_page(self):
    #    login_page_button = self.is_element_visible_and_click(BasePageLocators.LOGIN_PAGE)
    #    assert self.browser.current_url == "https://www.imperiasumok.ru/auth/", "Текущая страница != /auth/"
    