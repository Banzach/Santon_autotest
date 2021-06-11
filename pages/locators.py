from selenium.webdriver.common.by import By

class CategoryPageLocators():
    FILTER_EXPRESS = (By.CSS_SELECTOR, ".field-label.switch-field")
    FILTER_BTN_SHOW = (By.CSS_SELECTOR, ".rc-tooltip.b-tooltip.rc-tooltip-placement-right ")
    ADD_TO_CART_LAST_GOOD = (By.CSS_SELECTOR, ".p-supercategory__section-middle-col-right .small-tiles:last-child")
    ADD_TO_CART_FIRST_GOOD = (By.CSS_SELECTOR, ".b-preloader-ajax div>div:first-child")
    
class MainPageLocators():
    FIRST_PRODUCT_CHOICE_CUSTOMER = (By.CSS_SELECTOR, "[aria-label='1 / 18']")
    ARROW_NEXT_BANNER = (By.CSS_SELECTOR, ".slick-arrow.slick-next")
    ARROW_PREV_BANNER = (By.CSS_SELECTOR, ".slick-arrow.slick-prev")
    BANNER = (By.CSS_SELECTOR, ".slick-slide.slick-active")
    DROP_DOWN_CATALOG = (By.CSS_SELECTOR, ".b-header-catalog__button")
    DROP_DOWN_WC = (By.CSS_SELECTOR, "[data-room='vanny_menu']")
    LIST_OF_CATEGORY = (By.CSS_SELECTOR, "b-header-main-menu-list__item-text")
    
class CartPageLocators():
    BUY_IN_ONE_CLICK = (By.CSS_SELECTOR, ".buttons-row .btn--primary.button--one-click")
    CART_ADD_TO_BASKET_ON_COMPLECTATION = (By.CSS_SELECTOR, ".js-show-barcart-primary .btn--lg")
    CART_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn--primary.btn--md.button")
    POPUP_CONTINUE = (By.CSS_SELECTOR, ".button--continue")
    POPUP_GO_TO_BASKET = (By.CSS_SELECTOR, ".button--warning")
    FULL_PRICE = (By.CSS_SELECTOR, ".b-price__price-core [itemprop='price']") # Работает и для BasketPage
    ICON_FAVORITE = (By.CSS_SELECTOR, ".card-product-info-btns button:last-of-type")
    ICON_COMPRASION = (By.CSS_SELECTOR, ".card-product-info-btns button")
    FAVORITE_COUNT = (By.CSS_SELECTOR, ".b-header__icon-link--heart .b-header__icon-container--count")
    COMPRASION_COUNT = (By.CSS_SELECTOR, ".b-header__icon-link--compare .b-header__icon-container--count")
    
class BasketPageLocators():
    GO_TO_CHECKOUT = (By.CSS_SELECTOR, ".btn--primary.btn--lg")
	
class CheckoutPageLocators():
    CUSTOMER_PHONE = (By.CSS_SELECTOR, ".checkout-section--base [tabindex='1']")
    FIO = (By.CSS_SELECTOR, ".checkout-section--base [tabindex='2']")
    EMAIL = (By.CSS_SELECTOR, ".checkout-section--base [tabindex='3']")
    PICKUP = (By.XPATH, "//div[contains(text(), 'Самовывоз')]")
    ORDER_COMMENT = (By.CSS_SELECTOR, ".field-margin-md [rows='2']")
    CREATE_ORDER = (By.CSS_SELECTOR, ".checkout-action .btn-text")
    TOTAL_PRICE_CHECKOUT = (By.CSS_SELECTOR, ".total-price-price")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
	

	
class BasePageLocators():
    # DESCTOPE
    BODY = (By.TAG_NAME, "body")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".middle a #Layer_1")
    USER_NAME_ON_HEADER = (By.CSS_SELECTOR, ".middle [href = '/personal/'] span")
    SEARCH_BAR = (By.CSS_SELECTOR, ".middle [name='q']")
    GO_SEARCH_BUTTON = (By.CSS_SELECTOR, ".middle [type='submit']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".result b")
    FAVORITE_ICON = (By.CSS_SELECTOR, ".hidden-header .elem-fav span")
    CART_ICON = (By.CSS_SELECTOR, ".hidden-header .count")
    BUTTON_TO_CHANGE_CITY = (By.CSS_SELECTOR, ".btn.btn-gray.hidden-xs")
    BUTTON_TO_CHANGE_CITY_ON_THIS = (By.PARTIAL_LINK_TEXT, "Челябинск")
    LOGIN_PAGE = (By.LINK_TEXT, "Вход")
    CHOOSE_SECTION_MAN_BAGS= (By.CSS_SELECTOR, ".nav-top.hidden-xs [href='/catalog/muzhskie-sumki/']")
    CHOOSE_SECTION_MAN = (By.LINK_TEXT, 'Мужчинам')

#class LoginPageLocators():
    # DESCTOPE
    USER_LOGIN = (By.CSS_SELECTOR, "[name = 'USER_LOGIN']")
    USER_PASSWORD = (By.CSS_SELECTOR, "[name = 'USER_PASSWORD']")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[name='Login']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".box-auth-reg a[href = '/reg/']")

#class SectionPageLocators():
    # DESCTOPE
    FIRST_PRODUCT_CART = (By.CSS_SELECTOR, ".row .col-xs-6.col-sm-6.col-md-4.col-lg-3:nth-child(1) .box-snippet-full.product_item")
    ADD_TO_FAVORITE_FIRST_PRODUCT = (By.CSS_SELECTOR, ".row .col-xs-6.col-sm-6.col-md-4.col-lg-3:nth-child(1) .fa.fa-heart-o")
    ADD_TO_CART_FIRST_PRODUCT = (By.CSS_SELECTOR, ".row .col-xs-6.col-sm-6.col-md-4.col-lg-3:nth-child(1) .to_basket")
    SMART_FILTER = (By.CSS_SELECTOR, ".col-sm-4 .filter")

#class CartPageLocators():
    # DESCTOPE
    FIRST_PICKUP_POINT = (By.CSS_SELECTOR, "[data-ng-if='delivery.SHOPS'] label:nth-child(1)")
    DISCOUNT_CARD_FIELD = (By.CSS_SELECTOR, "[name='barcode']")
    APPLY_DISCOUNT_CARD = (By.CSS_SELECTOR, "button.btn.btn-gray")
    NEXT_STEP = (By.CSS_SELECTOR, "a.btn.btn-blue.pull-right")
    CONTACT_DATA_NAME = (By.CSS_SELECTOR, "[name='name']")
    CONTACT_DATA_LASTNAME = (By.CSS_SELECTOR, "[name ='surname']")
    CONTACT_DATA_EMAIL = (By.CSS_SELECTOR, "[name = 'email']")
    CONTACT_DATA_MESSAGE = (By.CSS_SELECTOR, "[name = 'message']")
    