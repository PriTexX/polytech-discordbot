class AuthenticatedUser:
    def __init__(self, server_name: str, group: str, department_code: str, guid: str):
        self.guid = guid
        self.group = group
        self.department_code = department_code
        self.server_name = server_name
