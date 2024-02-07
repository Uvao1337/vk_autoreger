import os
import random
import shutil
import time
from colorama import Fore
import requests
from src.api import Executor
from faker import Faker
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import TimeoutException
import vk_api

class Robot:
    def __init__(self, sms_activate_key, max_wait, debug_mode = False) -> None:
        self.sms_activate_key = sms_activate_key
        self.max_wait = max_wait
        self.debug_mode = debug_mode
        self.sms = Executor(sms_activate_key=self.sms_activate_key, debug_mode=self.debug_mode)
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

    
    def __humanize_account(self) -> bool:
        """
        СДЕЛАТЬ СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ  СДЕЛАТЬ СДЕЛАТЬ 

        return успех или нет
        """
        
        if not self.token:
            self.token = self.__get_vk_token()
        session = vk_api.VkApi(token=self.token)
        vk = session.get_api()
        data = vk.users.get(lang=3)[0]
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        self.fake


        def download_random_image(width, height, destination):
            """Скачивает рандомную фотографию"""

            url = f"https://picsum.photos/{width}/{height}/?random"
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(destination, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)
                    return True

        def set_main_photo():
            """Устанавливает аватарку для аккаунта"""

            if not download_random_image(800, 600, "heh.jpg"):
                return print("Не удалось скачать фотографию.")

            url = vk.photos.getOwnerPhotoUploadServer()['upload_url']

            a = os.path.basename(__file__)
            b = os.path.abspath(__file__).replace(a, '')

            request = requests.post(url, files={'photo': open(str(b) + '/heh.jpg', 'rb')}).json()

            server = request['server'] 
            hash = request['hash']

            vk.photos.saveOwnerPhoto(server=server, hash=hash, photo=request['photo'])
            print('Successfully set your avatar')

        def set_screen_name():
            """Складывает первые три символа имени, последние 3 символа фамилии и последние 4 символа ID."""
            finnaly_screen_name = f"{first_name[0:3].lower()}{last_name[-3:].lower()}{str(data.get('id'))[-4:]}"
            domain = vk.users.get(fields='domain')[0]['domain']

            if domain == finnaly_screen_name:
                return print('It is impossible to change the domain to the same one')

            try:
                vk.account.saveProfileInfo(screen_name=finnaly_screen_name)
                print('Successfully set the short name')
            except vk_api.exceptions.ApiError:
                print('Failed to set short name')


        def set_random_city_and_country():
            """Устанавливает рандомный город по стране канада (id 10), также ставит плашку РОДНОГО города"""

            cities = vk.database.getCities(country_id=10)
            fake_city = self.fake.city()

            vk.account.saveProfileInfo(country_id=10, city_id=random.choice(cities['items'])['id'], home_town=fake_city)
            print('Successfully established your place of residence')

        def set_relation(id_partner: int = None):
            """Устанавливает рандомное семейное положение, можно указать id партнера по желанию"""
            rel = random.randint(0, 8)

            if rel not in [0, 1, 5, 6] and id_partner:
                partner = id_partner
            else: 
                partner = None

            vk.account.saveProfileInfo(relation=rel, relation_partner_id=partner)
            print('Successfully established marital status')

        def set_status():
            """Устанавливается статус. Максимальный размер цитаты для статуса: 100 символов"""
            link = 'http://api.forismatic.com/api/1.0/?method=getQuote'
            while True:
                r = requests.get(link)
                text = r.text.partition('<quoteText>')[2]
                text = text.partition('</quoteText>')[0]
                if len(text) <= 100:
                    break
            vk.status.set(text=text)
            print("Status successfully set")

        def invite_to_groups():
            """Инвайтится в группы по тематике. Количество групп от 5 до 10"""
            quantity_groups = random.randint(5, 10)
            search_requests = ['развлечения', 'tech', 'music']
            groups = vk.groups.search(q=random.choice(search_requests), count=quantity_groups)['items']

            for i in groups:
                try:
                    vk.groups.join(group_id=i['id'], not_sure=1)
                except vk_api.exceptions.ApiError as ex:
                    if ex.code == 15:
                        continue
            print('Successfully joined groups')

        set_main_photo()
        set_screen_name()
        set_random_city_and_country()
        set_relation()
        set_status()
        invite_to_groups()
        return True


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
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Открываю сайт для получения токена")
            self.browser.get(self.get_token_url)
            # нажимаем кнопку настройки
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку настройки")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.settings_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка настройки не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            # тыкаем на все разрешения
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку разрешить аудио")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_audio_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка разрешить аудио не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку разрешить уведомления")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_notifications_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка разрешить уведолмения не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку разрешить добавить в меню")    
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_add_to_menu_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка разрешить добавить в меню не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку разрешить быстрые посты")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_fast_posts_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка разрешить быстрые посты не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку разрешить сообщения")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_messages_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка разрешить сообщения не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку разрешить рекламу")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_ads_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка разрешить рекламу не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку разрешить номер телефона")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_phone_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка разрешить номер телефона не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            # нажимаем кнопку получить
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку получить токен")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.get_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][[INFO] - Кнопка получить токен не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            # нажимаем кнопку разрешить
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку разрешить")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.allow_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка разрешить не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
                
        except Exception:
            self.browser.quit()
            print(f"{Fore.RED}[{datetime.now()}][INFO] - Произошла неизвестная ошибка. ENTER для выхода")
            input()
            exit()
            
        # получаем содержимое адресной строки и обрезаем лишнее
        url = self.browser.current_url()
        self.token = url.partition('access_token=')[2]
        self.token = url.partition('&expires_in')[0]
        return self.token

        
    def create_vk(self) -> dict:
        try:
            print(f"{Fore.YELLOW}[{datetime.now()}][INFO] - Текущий баланс: {Fore.BLUE}{self.sms.get_balance()}{Fore.YELLOW} ₽\n")
            # # открываем вк
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Начинаю алгоритм создания аккаунта")
            count = 1

            while True:
                print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Покупаю номер Попытка {count}")
                data = self.sms.get_number()
                if data['result']:
                    id = data['id']
                    number = data['number']
                    print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Номер успешно получен Номер: {number} Айди: {id}")
                    break
                else:
                    print(f"{Fore.YELLOW}[{datetime.now()}][INFO] - Не удалось купить номер")
                    time.sleep(5)
                    count += 1
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Открываю вк")
            self.browser.get(self.vk_url)

            # находим кнопку sign up и нажимаем на нее
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю на кнопку зарегаться")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_in))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка зарегаться не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            # находим поле для ввода номера тела
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Ввожу номер")
            try:
                field = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.number_field)))
                field.click()
                field.send_keys(Keys.BACK_SPACE)
                field.send_keys(Keys.BACK_SPACE)
                field.send_keys(number)
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Поле для ввода номера не найдено. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            # находим кнопку продолжить и нажимаем на нее
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку продолжить")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка продолжить не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            count = 1
            # number = '79199968331'
            while True:
                if count > self.max_wait:
                    self.browser.quit()
                    print(f"{Fore.RED}[{datetime.now()}][INFO] - Достигнуто максимальное количество попыток. ENTER для выхода")
                    input()
                    exit()
                print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Жду код Попытка {count}/{self.max_wait}")
                get_code = self.sms.get_code(data.get('id'))
                print(get_code)
                if get_code['result']:
                    code = get_code['code']
                    print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Код успешно получен Код: {code}")
                    break
                else:
                    print(f"{Fore.YELLOW}[{datetime.now()}][INFO] - Код еще не пришел")
                    count += 1
                    time.sleep(10)

            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Ввожу код")
            try:
                WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.code_field))).send_keys(code)
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Поле для ввода кода не найдено. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку продолжить")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue2_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка продолжить не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            # находим поле для ввода имени и вводи туда фейковое имя
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Ввожу имя")
            try:
                WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_input))).send_keys(self.fake.first_name_male())
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Поле для ввода имени не найдено. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            # находим поле для ввода фамилии и вводи туда фейковую фамилию
            print(f"{Fore.GREEN}[{datetime.now()}][robot] - Ввожу фамилию")
            try:
                WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.surname_input))).send_keys(self.fake.last_name_male())
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][robot] - Поле для ввода фамилии не найдено. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            # находим поле для ввода даты и вводи туда фейковую дату рождения
            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Ввожу дату рождения")
            try:
                WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.birthday_input))).send_keys(self.fake.date_of_birth(minimum_age=25, maximum_age=50).strftime("%d %m %Y "))
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Поле для ввода даты рождения не найдено. Проверьте XPATH. ENTER для выхода")
                input()
                exit()

            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Выбираю пол")
            select = Select(self.browser.find_element(By.XPATH, self.sex_input))
            select.select_by_value("2")

            print(f"{Fore.GREEN}[{datetime.now()}][INFO] - Нажимаю кнопку продолжить")
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue3_button))).click()
            except TimeoutException:
                self.browser.quit()
                print(f"{Fore.RED}[{datetime.now()}][INFO] - Кнопка продолжить не найдена. Проверьте XPATH. ENTER для выхода")
                input()
                exit()
            
        except Exception as x:
            self.browser.quit()
            print(f"{Fore.RED}[{datetime.now()}][INFO] - Произошла неизвестная ошибка. ENTER для выхода")
            input()
            exit()

        """
        получение токена (__get_vk_token)

        return {номер, пароль токен}
        """

