from selenium.webdriver.common.by import By


FullName_field = '//input[@id="userName"]'
Email_field = '//input[@id="userEmail"]'
Current_address_field = '//textarea[@id="currentAddress"]'
Permanent_address_field = '//textarea[@id="permanentAddress"]'
Submit = '//button[@id="submit"]'


def test_text_boxes1(chrome):
    driver = chrome
    driver.get('https://demoqa.com/text-box')
    name = driver.find_element(By.XPATH, FullName_field)
    email = driver.find_element(By.XPATH, Email_field)
    current_address = driver.find_element(By.XPATH, Current_address_field)
    permanent_address = driver.find_element(By.XPATH, Permanent_address_field)
    submit = driver.find_element(By.XPATH, Submit)

    name.send_keys("Tetiana Vovk")
    email.send_keys("test@ua.com")
    current_address.send_keys("Shevchenka str.")
    permanent_address.send_keys("Pulyia str.")
    submit.click()

