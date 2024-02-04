import requests

class Executor:
    def __init__(self, sms_activate_key, debug_mode=False) -> None:
        self.sms_activate_key = sms_activate_key
        self.debug_mode = debug_mode
        self.api_url = 'https://api.sms-activate.org/stubs/handler_api.php'
    
    def get_balance(self) -> int:
        data = {"action" : "getBalanceAndCashBack",
                "api_key" : self.sms_activate_key,
                }
        # делаем апи запрос на получение номера
        r = requests.get(self.api_url, params=data)
        balance = float(r.text.split(":")[1])
        return balance


    def get_number(self) -> dict:
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
    
    def get_code(self, activation_id) -> dict:
        data = {"action" : "getStatus",
                    "api_key" : self.sms_activate_key,
                    "id" : activation_id
                    }
        # делаем запрос на получение состояния активации
        r = requests.get(self.api_url, params=data)
        print(r.text)
        # если успешно
        if r.text == "STATUS_OK":
            return {"result" : True, "code" : r.text.split(":")[1]}
        # если неуспешно
        elif r.text == "STATUS_WAIT_CODE":
            return {"result" : False}
        else:
            return {"result" : False, "reason" : r.text}

    
   
        


    