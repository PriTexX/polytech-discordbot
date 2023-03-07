import requests
import fake_useragent
session = requests.Session()
user = fake_useragent.UserAgent().random
header = {
    'user-agent': user
}
payload = {
    "auth_action": 'userlogin',
    "ulogin": login,  # Логин
    "upassword": password  # Пароль
}

class Person_data:
    def __init__(self, payload):

        header = {
            'user-agent': user
        }
        with requests.session() as session:
            session.post("https://e.mospolytech.ru/old/index.php", data=payload, headers=header)
            response = session.post("https://e.mospolytech.ru/old/lk_api.php", data=payload)
            token = response.json()
            token_name = token['token']
            response2 = session.get("https://e.mospolytech.ru/old/lk_api.php/?getAppData&token=" + str(token_name))
            get_data_json = response2.json()
        self.User_datas = {
            "name_user": get_data_json['name'],
            "surname_user": get_data_json['surname'],
            "guid_user": get_data_json['guid_person'],
            "specialty_name": get_data_json['specialty_name'],
            "group_id": get_data_json['group']
        }


user = Person_data(payload).User_datas
print(user)
