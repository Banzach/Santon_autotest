import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    #driver.set_window_size(1024, 600)
    yield browser
    print("\nquit browser..")
    browser.quit()


















 ###### СЛОЖНАЯ ФИКСТУРА ДЛЯ ОТКРЫТИЯ ЧЕРЕЗ КОМАНДНУЮ ЛИБО ХРОМА ЛИБО ФАЙЕРФОКСА
 #Запрашиваем название браузера в CMD, устанавливаем дефолтное значение названия браузера
#def pytest_addoption(parser):
#    parser.addoption('--browser_name', action='store', default='chrome',
#                     help="Choose browser: chrome or firefox")


 #В фикстуре создаем условие. В зависимости от названия браузера запустится либо хром, либо фаерфокс
#@pytest.fixture(scope="function")
#def browser(request):
#    browser_name = request.config.getoption("browser_name")
#    browser = None
#    if browser_name == "chrome":
#        print("\nstart chrome browser for test..")
#        browser = webdriver.Chrome()
#    elif browser_name == "firefox":
#        print("\nstart firefox browser for test..")
#        browser = webdriver.Firefox()
#    else:
#        raise pytest.UsageError("--browser_name should be chrome or firefox")
#    yield browser
#    print("\nquit browser..")
#    browser.quit()
