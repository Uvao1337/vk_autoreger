import os
from src.api import Executor
from src.robot import Robot
os.system('cls')
os.system('TITLE autoreger v 1.0')
"""
" " " " " " " " " " "                   
"  autoreger        "
"                   "
"    v 1.0          "
"                   "
"     dev           "
"                   "
"                   "
" " " " " " " " " " "

TODO: метод создания почты мэйл ру через регнутый акк + привязка почты к вк
TODO: метод получения токена череза vk_host
TODO: обработка исключений

"""

# ключ апи от сервиса sms activate
SMS_ACTIVATE_KEY = 'Af6e8801cd3b821e6dc2342A9A8682ee'
# режим отладки для вывода системных сообщений 
DEBUG_MODE = True
# прокси (рекомендуются мобильные или резидентские с ротацией на каждый запрос)
PROXY = ''
# максимальная цена на виртуальный номер
MAX_PRICE = 20
# количество аккаунтов которое нужно зарегистрировать
TASKS = 1
# псевдономер для тестов
TEST = '+792570613376'

sms = Executor(sms_activate_key=SMS_ACTIVATE_KEY, debug_mode=DEBUG_MODE)
robot = Robot(debug_mode=DEBUG_MODE)

for task in range(TASKS):
    if DEBUG_MODE:
        print(f"[main] Задача {task}/{TASKS}")
    """
    вызов метода покупки номера
    
    вызов метода создания акка вк

    получение данных и запись их в файлик
    """
    data = robot.create_vk(TEST)
    

    









