import Helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# Localizadores para las pruebas
class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_get_taxi = (By.CSS_SELECTOR, ".button.round")
    comfort_button = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg" and @alt="Comfort"]')
    blanket_and_tissue_elements_comfort = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]')
    number_field = (By.CSS_SELECTOR, ".np-button")
    click_number_input = (By.CSS_SELECTOR, ".np-input")
    add_phone = (By.ID, "phone")
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    code_field = (By.XPATH, '//label[@for="code"]')
    add_code = (By.ID, "code")
    button_confirm = (By.XPATH, '//*[text()="Confirmar"]')
    number_text = (By.CSS_SELECTOR, '.np-text')
    payment_method_field = (By.CSS_SELECTOR, ".pp-text")
    button_plus_card = (By.CLASS_NAME, "pp-plus-container")
    add_number_card = (By.ID, "number")
    add_code_card = (By.NAME, "code")
    rectangle_colors = (By.CSS_SELECTOR, ".plc")
    button_add_card_code = (By.XPATH, '//*[text()="Agregar"]')
    button_close_payment_method = (
    By.XPATH, '//div[@class="payment-picker open"]/div[@class="modal"]/div[@class="section active"]/button')
    text_card = (By.CLASS_NAME, "pp-value-text")
    select_message_driver = (By.XPATH, '//label[@for="comment" and @class="label"]')
    message_driver_field = (By.ID, "comment")
    select_blanket_and_tissue = (By.CLASS_NAME, 'r-sw')
    confirm_blanket_and_tissue = (By.CSS_SELECTOR, '.r-sw > div >input')
    add_ice_cream = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-plus')
    select_two_ice_creams = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-value')
    search_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
    search_car_screen = (By.CSS_SELECTOR, ".order-header-title")
    img_driver = (By.XPATH, '//img[@src="/static/media/bender.e90e5089.svg"]')

    def __init__(self, driver):
        self.driver = driver

    # 1. Configuración de las direcciones
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_adress, to_adress):
        self.set_from(from_adress)
        self.set_to(to_adress)

    # 2.Seleccionar la tarifa Comfort
    def click_button_get_taxi(self):
        self.driver.find_element(*self.button_get_taxi).click()

    def click_ride_comfort(self):
        self.driver.find_element(*self.comfort_button).click()

    def active_comfort(self):
        return self.driver.find_element(*self.blanket_and_tissue_elements_comfort).is_displayed()

    def select_ride_comfort(self):
        self.click_button_get_taxi()
        self.click_ride_comfort()

    # 3.Seleccionar y rellenar el campo número de telefono
    def click_phone_field(self):
        self.driver.find_element(*self.number_field).click()

    def click_add_phone_field(self):
        self.driver.find_element(*self.click_number_input).click()

    def add_phone_number(self, number):
        self.driver.find_element(*self.add_phone).send_keys(number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def add_code_field(self):
        self.driver.find_element(*self.add_code).send_keys(Helpers.retrieve_phone_code(self.driver))

    def click_button_confirm(self):
        self.driver.find_element(*self.button_confirm).click()

    def write_phone_number_correct(self):
        return self.driver.find_element(*self.number_text).text

    def add_number_phone_field(self, number):
        self.click_phone_field()
        self.click_add_phone_field()
        self.add_phone_number(number)
        self.click_next_button()
        self.add_code_field()
        self.click_button_confirm()

    # 4.Agregar una tarjeta de crédito
    def click_payment_method_field(self):
        self.driver.find_element(*self.payment_method_field).click()

    def click_plus_button_card(self):
        self.driver.find_element(*self.button_plus_card).click()

    def add_card_number(self, card_number):
        self.driver.find_element(*self.add_number_card).send_keys(card_number)

    def add_card_code(self, card_code):
        self.driver.find_element(*self.add_code_card).send_keys(card_code)

    def click_another_place_screen(self):
        self.driver.find_element(*self.rectangle_colors).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.button_add_card_code).click()

    def click_close_payment_method_screen(self):
        self.driver.find_element(*self.button_close_payment_method).click()

    def correct_add_card(self):
        return self.driver.find_element(*self.add_number_card).get_property('value')

    def correct_text_add_card(self):
        return self.driver.find_element(*self.text_card).text

    def add_card_payment_method(self, card_number, card_code):
        self.click_payment_method_field()
        self.click_plus_button_card()
        self.add_card_number(card_number)
        self.add_card_code(card_code)
        self.correct_add_card()
        self.click_another_place_screen()
        self.click_add_card_button()
        self.click_close_payment_method_screen()

    # 5.Mensaje para el conductor
    def click_message_driver(self):
        self.driver.find_element(*self.select_message_driver).click()

    def write_message_driver(self, message):
        self.driver.find_element(*self.message_driver_field).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_driver_field).get_property('value')

    def send_message_for_driver(self, message):
        self.click_message_driver()
        self.write_message_driver(message)

    # 6. Pedir manta y pañuelos
    def click_select_blanket_tissue(self):
        self.driver.find_element(*self.select_blanket_and_tissue).click()

    def get_blanket_tissue(self):
        return self.driver.find_element(*self.confirm_blanket_and_tissue).is_selected()

    # 7.Seleccionar dos helados
    def click_add_first_ice_cream(self):
        self.driver.find_element(*self.add_ice_cream).click()

    def click_add_second_ice_cream(self):
        self.driver.find_element(*self.add_ice_cream).click()

    def set_two_ice_creams(self):
        return self.driver.find_element(*self.select_two_ice_creams).text

    def add_two_ice_creams(self):
        self.click_add_first_ice_cream()
        self.click_add_second_ice_cream()

    #  8. Seleccionar el botón para buscar un taxi
    def click_search_taxi_button(self):
        self.driver.find_element(*self.search_taxi_button).click()

    def open_search_taxi_screen(self):
        return self.driver.find_element(*self.search_car_screen).is_displayed()

    # 9. Esperar a que aparezca la información del conductor en el modal
    def open_information_driver_screen(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.img_driver))
        return self.driver.find_element(*self.img_driver).is_displayed()
