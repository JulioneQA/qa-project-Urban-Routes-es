import data
from Locators import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        # cls.driver = webdriver.Chrome(desired_capabilities=capabilities)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    # 1. Comprobar que las direcciones han sido agregadas correctamente
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(5)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # 2. Comprobar que la tarifa comfort ha sido seleccionada
    def test_select_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_ride_comfort()
        assert routes_page.active_comfort() == True

    # 3. Comprobar que el número de teléfono aparezca en el campo correctamente
    def test_phone_number_correct(self):
        routes_page = UrbanRoutesPage(self.driver)
        number_phone = data.phone_number
        routes_page.add_number_phone_field(number_phone)
        assert routes_page.write_phone_number_correct() == number_phone

    # 4. Comprobar que una tarjeta haya sido agregada
    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number, card_code = data.card_number, data.card_code
        routes_page.add_card_payment_method(card_number, card_code)
        assert routes_page.correct_add_card() == card_number
        assert routes_page.correct_text_add_card() == "Tarjeta"

    # 5. Comprobar el mensaje para el conductor
    def test_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.send_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

    # 6. Comprobar que el botón Mantas y pañuelos este seleccionado
    def test_button_blanket_and_tissue(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_select_blanket_tissue()
        assert routes_page.get_blanket_tissue() == True

    # 7.  Comprobar que se han agregado dos helados
    def test_add_two_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_two_ice_creams()
        assert routes_page.set_two_ice_creams() == "2"

    # 8. Comprobar que la ventada "Buscar automóvil" se abra al dar click en el modal
    def test_select_search_taxi_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(5)
        routes_page.click_search_taxi_button()
        assert routes_page.open_search_taxi_screen() == True

    # 9. Comprobar que la ventana con la información del conductor aparezca
    def test_driver_information_screen(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.open_information_driver_screen() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
