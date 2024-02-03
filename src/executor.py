import requests

class Executor:
    def __init__(self, sms_activate_key, debug_mode=False) -> None:
        self.sms_activate_key = sms_activate_key
        self.debug_mode = debug_mode
        self.api_url = 'https://api.sms-activate.org/stubs/handler_api.php'

    def get_number(self, max_price=None) -> dict:
        data = {"action" : "getNumber",
                "service" : "vk",
                "api_key" : self.sms_activate_key,
                "country" : 36
                }
        # делаем апи запрос на получение номера
        r = requests.get(self.api_url, params=data)
        # если успешно
        if "ACCESS_NUMBER" in r.text:
            print(r.text)
            # возвращаем результат True, айди активации, номер 
            return {"result" : True, "id" : r.text.split(":")[1], "number" : r.text.split(":")[2]}
        # если неуспешно
        else:
            print(r.text)
            return {"result" : False, "reason" : r.text}
    
    def get_state(self, activation_id) -> bool:
        data = {"action" : "getStatus",
                    "api_key" : self.sms_activate_key,
                    "id" : activation_id
                    }
        # делаем запрос на получение состояния активации
        r = requests.get(self.api_url, params=data)
        # если успешно
        if r.text == "ACCESS_READY":
            print(r.text)
            return True
        # если неуспешно
        else:
            return False
    
    def get_code(self, activation_id) -> dict:
        data = {"action" : "getHistory",
                "api_key" : self.sms_activate_key
                }
        # делаем апи запрос на получение истории активаций
        r = requests.get(self.api_url, params=data)
        print(r)
        # проходимся по каждому элементу в списке
        for element in r:
            # если айди активации наш, то возвращаем смс код
            if activation_id in element:
                return {"result" : True, "code" : element['sms']}
        # иначе возвращаем неудачу
        return {"result" : False, "reason" : "код не найден"}
        


    