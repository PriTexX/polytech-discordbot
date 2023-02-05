
class UserEntity:
    id: int
    external_id: str

    def __init__(self, user_id: int = None, external_id: str = None):
        self.id = user_id
        self.external_id = external_id

    def __str__(self):
        return f"[UserEntity {self.id} - {self.external_id}]"

    def __repr__(self):
        return f"{self.__class__}: {self.id} - {self.external_id}"

    def is_empty(self) -> bool:
        return self.id is None
