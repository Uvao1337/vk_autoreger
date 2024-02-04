import faker
import random
import string

class Generator:
    def __init__(self, debug_mode = False) -> None:
        self.debug_mode = debug_mode
        self.fake = faker.Faker("en_US")
    
    def generate_password(self, lenght):
        symbols = string.ascii_letters + string.punctuation + string.digits
        password = [random.choice(symbols) for x in range(lenght)]
        password = ''.join(password)
        return password

    def generate_data(self, gender) -> dict:
        if gender == 'male':
            return {"name" : self.fake.first_name_male(),
                    "surname" : self.fake.last_name_male(),
                    "birthdate" : self.fake.date_of_birth(minimum_age=25, maximum_age=50).strftime("%d %m %Y ")
                    }
