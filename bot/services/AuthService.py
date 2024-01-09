from aiohttp import ClientSession

from core.entity import AuthenticatedUser
from core.errors import WrongUsernameOrPasswordException, ServerError


class AuthService:
    def __init__(self, client: ClientSession):
        self.client = client

    async def authenticate(self, login: str, password: str) -> AuthenticatedUser:
        token = ""
        async with self.client.post("https://e.mospolytech.ru/old/lk_api.php",
                                    data={"ulogin": login, "upassword": password}) as response:

            if response.status == 400:
                raise WrongUsernameOrPasswordException("Wrong username or password")

            if response.status != 200:
                raise ServerError("Something went wrong")

            json = await response.json()
            token = json['token']

        async with self.client.get("https://e.mospolytech.ru/old/lk_api.php/?getAppData&token=" + str(token)) as response:
            if response.status != 200:
                raise ServerError("Something went wrong")
            data = await response.json()
            student_guid = data['guid_person']

        # В запросе на getAppData прилетают устаревшие данные, поэтому берем оттуда только гуид
        async with self.client.get("https://e.mospolytech.ru/old/lk_api.php/?getUser&token=" + str(token)) as response:
            if response.status != 200:
                raise ServerError("Something went wrong")
            data = await response.json()

            specialty_code = data['user']['specialty'][:8]

            return AuthenticatedUser(
                f"{data['user']['surname']} {data['user']['name']}",
                data['user']['group'], specialty_code, student_guid)



