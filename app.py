from src.executor import Executor
from src.robot import Robot

"""
TODO: метод создания почты мэйл ру через регнутый акк + привязка почты к вк
TODO: метод получения токена череза vk_host
"""

SMS_ACTIVATE_KEY = 'Af6e8801cd3b821e6dc2342A9A8682ee'
DEBUG_MODE = True
PROXY = ''
MAX_PRICE = 20
TASKS = 1
TEST = '+792570613376'

sms = Executor(sms_activate_key=SMS_ACTIVATE_KEY, debug_mode=DEBUG_MODE)
robot = Robot(debug_mode=DEBUG_MODE)
for task in range(TASKS):
    robot.run(TEST)
    









