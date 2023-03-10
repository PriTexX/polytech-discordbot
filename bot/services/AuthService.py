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

        async with self.client.get("https://e.mospolytech.ru/old/lk_api.php/?getAppData&token=" + str(token),
                                    data={"ulogin": login, "upassword": password}) as response:
            if response.status != 200:
                raise ServerError("Something went wrong")
            data = await response.json()

            return AuthenticatedUser(
                f"{data['surname']} {data['name']}",
                data['group'], data['specialty_code'], data['guid_person'])



