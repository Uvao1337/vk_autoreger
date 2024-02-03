import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

class Robot:
    def __init__(self, debug_mode = False) -> None:
        self.debug_mode = debug_mode
        self.browser = webdriver.Chrome()
        self.fake = Faker("ru_RU")
        self.vk_url = 'https://vk.com/'
        self.get_token_url = "https://oauth.vk.com/authorize?client_id=6121396&scope=501202911&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1"
        # xpath адрес кнопки "sign up"
        self.sign_in = "/html/body/div[10]/div/div/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/div[1]/button/span"
        # xpath адрес поля для ввода номера тела
        self.number_field = "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/section/div[1]/div/div/input"
        # xpath адрес кнопки продолжить
        self.continue_button = "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div[1]/button/span[1]"
        # xpath адрес поля для ввода кода
        self.code_field = '//*[@id="otp"]'
        self.continue2_button = "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/form/div[3]/div/button/span[1]"
        # xpath адрес поля для ввода информации
        self.name_input = "/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/section/div[1]/form/div/div[1]/div[1]/div/div[2]/div[1]/input"
        self.surname_input = "/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/section/div[1]/form/div/div[1]/div[1]/div/div[2]/div[2]/input"
        self.birthday_input = '//*[@id="userDate"]'
        self.sex_input = "/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/section/div[1]/form/div/div[1]/div[3]/label/select"
        self.continue3_button = "/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/section/div[1]/form/div/div[2]/button/span[1]"
    
    def create_mail_ru(self) -> None:
        pass

    def get_vk_token(self) -> None:
        pass

    def create_vk(self, number) -> None:
        # # открываем вк
        self.browser.get(self.vk_url)
        # # находим кнопку sign up и нажимаем на нее
        # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_in))).click()
        # # находим поле для ввода номера тела 
        # field = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.number_field)))
        # field.click()
        # field.send_keys(Keys.BACK_SPACE)
        # field.send_keys(Keys.BACK_SPACE)
        # # вводим туда наш псевдономер
        # field.send_keys(number)
        # # находим кнопку продолжить и нажимаем на нее
        # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button))).click()
        # """
        # логика для получения и ввода кода...
        # """
        # code = input("код: ")
        # WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.code_field))).send_keys(code)
        # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue2_button))).click()
        # # находим поле для ввода имени и вводи туда фейковое имя
        # WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_input))).send_keys(self.fake.first_name_male())
        # # находим поле для ввода имени и вводи туда фейковую фамилию
        # WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.surname_input))).send_keys(self.fake.last_name_male())
        # # находим поле для ввода имени и вводи туда фейковую дату рождения
        # WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.birthday_input))).send_keys(self.fake.date_of_birth(minimum_age=25, maximum_age=50).strftime("%d %m %Y "))
        # select = Select(self.browser.find_element(By.XPATH, self.sex_input))
        # select.select_by_value("2")
        # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue3_button))).click()
        time.sleep(10)
        body = self.browser.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.CONTROL + 'T')
        self.browser.close()
        time.sleep(5)

