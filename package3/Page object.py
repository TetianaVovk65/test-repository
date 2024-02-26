from selenium.webdriver.common.by import By


class ObjPage:
    FullName_field = '//input[@id="userName"]'
    Email_field = '//input[@id="userEmail"]'
    Current_address_field = '//textarea[@id="currentAddress"]'
    Permanent_address_field = '//textarea[@id="permanentAddress"]'
    Submit = '//button[@id="submit"]'

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get('https://demoqa.com/text-box')
        return self

    def fill_name(self, name: str):
        self.driver.find_element(By.XPATH, self.FullName_field).send_keys(name)
        return self

    def fill_email(self, email: str):
        self.driver.find_element(By.XPATH, self.Email_field).send_keys(email)
        return self

    def fill_current_address(self, current_address: str):
        self.driver.find_element(By.XPATH, self.Current_address_field).send_keys(current_address)
        return self

    def fill_permanent_address(self, permanent_address: str):
        self.driver.find_element(By.XPATH, self.Permanent_address_field).send_keys(permanent_address)
        return self

    def submit(self):
        self.driver.find_element(By.XPATH, self.Submit).click


def test_text_boxes1(chrome):
    page = ObjPage(chrome)
    page.open_page().fill_name("Ivan").fill_email("test@com.com").fill_current_address("Shevchenka str.").fill_permanent_address("Osvytska str.").submit

    pass
    # name = driver.find_element(By.XPATH, FullName_field)
    # email = driver.find_element(By.XPATH, Email_field)
    # current_address = driver.find_element(By.XPATH, Current_address_field)
    # permanent_address = driver.find_element(By.XPATH, Permanent_address_field)
    # submit = driver.find_element(By.XPATH, Submit)
    #
    # name.send_keys("Tetiana Vovk")
    # email.send_keys("test@ua.com")
    # current_address.send_keys("Shevchenka str.")
    # permanent_address.send_keys("Pulyia str.")
    # submit.click()
    #
    # result_name = driver.find_element(By.ID, 'name').text
    # result_email = driver.find_element(By.ID, 'email').text
    # result_current_address = driver.find_element(By.CSS_SELECTOR, 'p[id=currentAddress]').text
    # result_permanent_address = driver.find_element(By.CSS_SELECTOR, 'p[id=permanentAddress]').text
