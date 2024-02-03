import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import TimeoutException

class Robot:
    def __init__(self, debug_mode = False) -> None:
        self.debug_mode = debug_mode
        self.browser = webdriver.Chrome()
        self.fake = Faker("ru_RU")
        self.vk_url = 'https://vk.com/'
        self.get_token_url = 'https://vkhost.github.io/'
        # xpath адрес кнопки "sign up"
        self.sign_in = "/html/body/div[10]/div/div/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/div[1]/button/span"
        # xpath адрес поля для ввода номера тела
        self.number_field = "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/section/div[1]/div/div/input"
        # xpath адрес кнопки продолжить после ввода номера
        self.continue_button = "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div[1]/button/span[1]"
        # xpath адрес поля для ввода кода
        self.code_field = '//*[@id="otp"]'
        # xpath адрес кнопки продолжить после ввода кода
        self.continue2_button = "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/form/div[3]/div/button/span[1]"
        # xpath адрес поля для ввода информации
        self.name_input = "/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/section/div[1]/form/div/div[1]/div[1]/div/div[2]/div[1]/input"
        self.surname_input = "/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/section/div[1]/form/div/div[1]/div[1]/div/div[2]/div[2]/input"
        self.birthday_input = '//*[@id="userDate"]'
        self.sex_input = "/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/section/div[1]/form/div/div[1]/div[3]/label/select"
        # xpath адрес кнопки продолжить после ввода информации о себе
        self.continue3_button = "/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/section/div[1]/form/div/div[2]/button/span[1]"
        
        # xpath адрес кнопки настройки
        self.settings_button = "/html/body/section[1]/div/div[16]"
        # xpath адреса кнопок разрешений
        self.allow_audio_button = "/html/body/div[1]/div/div[2]/div[2]/label[4]"
        self.allow_notifications_button = "/html/body/div[1]/div/div[2]/div[2]/label[1]"
        self.allow_add_to_menu_button = "/html/body/div[1]/div/div[2]/div[2]/label[8]"
        self.allow_fast_posts_button = "/html/body/div[1]/div/div[2]/div[2]/label[9]"
        self.allow_messages_button = "/html/body/div[1]/div/div[2]/div[2]/label[12]"
        self.allow_ads_button = "/html/body/div[1]/div/div[2]/div[2]/label[22]"
        self.allow_phone_button = "/html/body/div[1]/div/div[2]/div[2]/label[25]"
        # xpath адрес кнопки получить
        self.get_button = '//*[@id="submit"]'
        # xpath адрес кнопки разрешить 
        self.allow_button = "/html/body/div[1]/div/div/div[3]/div/div[1]/button[1]"

    
    def __connect_mail(self, mail) -> bool:
        """
        СДЕЛАТЬ СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ

        return получилось или не получилось
        """
        pass

    def __create_mail_ru(self) -> dict:
        """
        СДЕЛАТЬ СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ 

        return {почта, пароль}
        """
        
        pass

    def __get_vk_token(self) -> str:
        """
        СДЕЛАТЬ СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ СДЕЛАТЬ 

        return токен
        """
        # создаем новую вкладку
        try:

            self.browser.execute_script("window.open('');")
            # переключаемся на нее
            self.browser.switch_to.window(self.browser.window_handles[1])
            # открываем сайт для получения токена
            if self.debug_mode:
                print("[robot] - Открываю сайт для получения токена")
            self.browser.get(self.get_token_url)
            # нажимаем кнопку настройки
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку настройки")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.settings_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка настройки не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            # тыкаем на все разрешения
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку разрешить аудио")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_audio_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка разрешить аудио не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку уведомления аудио")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_notifications_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка разрешить уведолмения не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку разрешить добавить в меню")    
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_add_to_menu_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка разрешить добавить в меню не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку разрешить быстрые посты")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_fast_posts_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка разрешить быстрые посты не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку разрешить сообщения")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_messages_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка разрешить сообщения не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку разрешить рекламу")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_ads_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка разрешить рекламу не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку разрешить номер телефона")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_phone_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка разрешить номер телефона не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            # нажимаем кнопку получить
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку получить токен")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.get_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка получить токен не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            # нажимаем кнопку разрешить
            if self.debug_mode:
                print("[robot] - Нажимаю кнопку разрешить")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_button))).click()
                time.sleep(5)
            except TimeoutException:
                self.browser.quit()
                print("[robot] Кнопка разрешить не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
                
        except Exception as x:
            self.browser.quit()
            print(f"[robot] Произошла неизвестная ошибка. Текст ошибки: {x} ENTER для выхода")
            input()
            exit()
            
        # получаем содержимое адресной строки и обрезаем лишнее
        url = self.browser.current_url()
        input(url)

        
    def create_vk(self, number) -> dict:
        try:
            # # открываем вк
            if self.debug_mode:
                print("[robot] - Начинаю алгоритм создания аккаунта")
                print("[robot] - Открываю вк")
            self.browser.get(self.vk_url)

            ## находим кнопку sign up и нажимаем на нее
            #if self.debug_mode:
            #    print("[robot] - Нажимаю на кнопку зарегаться")
            #try:
            #    WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_in))).click()
            #except TimeoutException:
            #    self.browser.quit()
            #    print("[robot] Кнопка зарегаться не найдена. Проверьте XPATH. ENTER для выхода")
            #    input()
            #    exit()
#
            ## находим поле для ввода номера тела
            #if self.debug_mode:
            #    print("[robot] - Ввожу номер")
            #try:
            #    field = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.number_field)))
            #    field.click()
            #    field.send_keys(Keys.BACK_SPACE)
            #    field.send_keys(Keys.BACK_SPACE)
            #    field.send_keys(number)
            #except TimeoutException:
            #    self.browser.quit()
            #    print("[robot] Поле для ввода номера не найдено. Проверьте XPATH. ENTER для выхода")
            #    input()
            #    exit()
#
            ## находим кнопку продолжить и нажимаем на нее
            #if self.debug_mode:
            #    print("[robot] - Нажимаю кнопку продолжить")
            #try:
            #    WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button))).click()
            #except TimeoutException:
            #    self.browser.quit()
            #    print("[robot] Кнопка продолжить не найдена. Проверьте XPATH. ENTER для выхода")
            #    input()
            #    exit()
#
            ## логика для получения и ввода кода...
            #code = input("[robot] Код подтверждения: ")
            #
            #if self.debug_mode:
            #    print("[robot] - Ввожу код")
            #try:
            #    WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.code_field))).send_keys(code)
            #except TimeoutException:
            #    self.browser.quit()
            #    print("[robot] Поле для ввода кода не найдено. Проверьте XPATH. ENTER для выхода")
            #    input()
            #    exit()
#
            #if self.debug_mode:
            #    print("[robot] - Нажимаю кнопку продолжить")
            #try:
            #    WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue2_button))).click()
            #except TimeoutException:
            #    self.browser.quit()
            #    print("[robot] Кнопка продолжить не найдена. Проверьте XPATH. ENTER для выхода")
            #    input()
            #    exit()
#
            ## находим поле для ввода имени и вводи туда фейковое имя
            #if self.debug_mode:
            #    print("[robot] - Ввожу имя")
            #try:
            #    WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_input))).send_keys(self.fake.first_name_male())
            #except TimeoutException:
            #    self.browser.quit()
            #    print("[robot] Поле для ввода имени не найдено. Проверьте XPATH. ENTER для выхода")
            #    input()
            #    exit()
#
            ## находим поле для ввода фамилии и вводи туда фейковую фамилию
            #if self.debug_mode:
            #    print("[robot] - Ввожу фамилию")
            #try:
            #    WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.surname_input))).send_keys(self.fake.last_name_male())
            #except TimeoutException:
            #    self.browser.quit()
            #    print("[robot] Поле для ввода фамилии не найдено. Проверьте XPATH. ENTER для выхода")
            #    input()
            #    exit()
#
            ## находим поле для ввода даты и вводи туда фейковую дату рождения
            #if self.debug_mode:
            #    print("[robot] - Ввожу дату рождения")
            #try:
            #    WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.birthday_input))).send_keys(self.fake.date_of_birth(minimum_age=25, maximum_age=50).strftime("%d %m %Y "))
            #except TimeoutException:
            #    self.browser.quit()
            #    print("[robot] Поле для ввода даты рождения не найдено. Проверьте XPATH. ENTER для выхода")
            #    input()
            #    exit()
#
            #if self.debug_mode:
            #    print("[robot] - Выбираю пол")
            #select = Select(self.browser.find_element(By.XPATH, self.sex_input))
            #select.select_by_value("2")
#
            #if self.debug_mode:
            #    print("[robot] - Нажимаю кнопку продолжить")
            #try:
            #    WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue3_button))).click()
            #except TimeoutException:
            #    self.browser.quit()
            #    print("[robot] Кнопка продолжить не найдена. Проверьте XPATH. ENTER для выхода")
            #    input()
            #    exit()
            self.__get_vk_token()
            
        except Exception as x:
            self.browser.quit()
            print(f"[robot] Произошла неизвестная ошибка. Текст ошибки: {x} ENTER для выхода")
            input()
            exit()

        """
        получение токена (__get_vk_token)

        создание почты mail.ru (__create_mail_ru)

        привязка mail.ru к аккаунту вк (__connect_mail)

        return {номер, токен, почта, пароль от почты}
        """

