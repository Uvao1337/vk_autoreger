import os
from src.api import Executor
from src.robot import Robot
os.system('cls')
os.system('TITLE autoreger v 1.0')

print("=====================\n"
      "|   autoreger        |\n"
      "|                    |\n"
      "|     v 1.0          |\n"
      "|                    |\n"
      "|      dev           |\n"
      "|                    |\n"
      "|    private         |\n"
      "|                    |\n"
      "| by илюша & тимоша  |\n"
      "|                    |\n"
      "=====================\n")
"""
TODO: метод создания почты мэйл ру через регнутый акк + привязка почты к вк
TODO: метод получения токена череза vk_host

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


robot = Robot(sms_activate_key=SMS_ACTIVATE_KEY, debug_mode=DEBUG_MODE)

# повторяем цикл в зависимости от количества задач
for task in range(TASKS):
    print(f"[main] Задача {task}/{TASKS}")
    """
    вызов метода покупки номера
    
    вызов метода создания акка вк

    получение данных и запись их в файлик
    """
    data = robot.create_vk(TEST)
    

    









