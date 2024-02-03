import os
import configparser
from colorama import Fore
from src.api import Executor
from src.robot import Robot

cfg = configparser.ConfigParser()
cfg.read('cfg/config.ini', encoding='utf-8')

SMS_ACTIVATE_KEY = cfg['Settings']['sms_activate_key']
DEBUG_MODE = cfg['Settings']['debug_mode']
PROXY = cfg['Settings']['proxy']
MAX_PRICE = cfg['Settings']['max_price']
SEX = cfg['Settings']['accounts_sex']
AUTOUPLOAD = cfg['Settings']['auto_upload']
AUTOUPLOAD_IF_MORE_THAN = cfg['Settings']['autoupload_if_more_than']
AUTOPROMOTION = cfg['Settings']['auto_promotion']
TASKS = 1
TEST = '+792570613376'

os.system('cls')
os.system('TITLE autoreger v 1.0')
print(Fore.YELLOW +     "===================================")
print(                  "|                                  |")
print(                 f"|    {Fore.MAGENTA}External autoreger script{Fore.YELLOW}     |")
print(                  "|                                  |")
print(                 f"|          {Fore.CYAN}v 1.0{Fore.YELLOW}                   |")
print(                  "|                                  |")
print(                 f"|        {Fore.RED}Type: dev{Fore.YELLOW}                 |")
print(                  "|                                  |")
print(                 f"|    {Fore.WHITE}coded by {Fore.BLUE}Илюша {Fore.WHITE}& {Fore.BLUE}Тимоша{Fore.YELLOW}       |")
print(                  "|                                  |")
print(                  f"|    {Fore.WHITE}с любовью {Fore.BLUE}Илюши{Fore.WHITE} к {Fore.MAGENTA}Дашуле {Fore.YELLOW}     |")
print(                  "|                                  |")
print(                  f"|         {Fore.WHITE}и {Fore.BLUE}Тимоши{Fore.WHITE} к {Fore.MAGENTA}Лере {Fore.YELLOW}         |")
print(                  "|                                  |")
print(                  "===================================\n\n")
print(f"{Fore.BLUE}---> Настройки <---\n\n{Fore.CYAN}=======================================\n")
print(f"{Fore.YELLOW}Режим отладки: {Fore.BLUE}{DEBUG_MODE}\n\n"
      f"{Fore.YELLOW}Максимальная цена номера: {Fore.BLUE}{MAX_PRICE}\n\n"
      f"{Fore.YELLOW}Автоповышение максимальной цены: {Fore.BLUE}{AUTOPROMOTION}\n\n"
      f"{Fore.YELLOW}Пол аккаунтов: {Fore.BLUE}{SEX}\n\n"
      f"{Fore.YELLOW}Автовыгрузка на {Fore.GREEN}lolz.guru{Fore.WHITE}: {Fore.BLUE}{AUTOUPLOAD}\n")
if AUTOUPLOAD:
    print(f"{Fore.YELLOW}Выгружать если аккаунтов создано: {Fore.BLUE}{AUTOUPLOAD_IF_MORE_THAN}\n")
print(Fore.CYAN +     f"========================================")


while True:
    try:
        tasks = int(input(f"\n{Fore.YELLOW}Введите необходимое количество аккаунтов: {Fore.BLUE}"))
        break
    except ValueError:
        print(f"\n{Fore.RED}Количество аккаунтов может быть только числом")

robot = Robot(sms_activate_key=SMS_ACTIVATE_KEY, debug_mode=DEBUG_MODE)

task_counter = 1
for task in range(TASKS):
    print(f"\n{Fore.YELLOW}Задача: {Fore.CYAN}{task_counter}/{TASKS}\n")
    robot.create_vk()
    task_counter += 1
    

    









