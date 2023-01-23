class AuthenticatedUser:
    def __init__(self, server_name: str, group: str, department: str, guid: str):
        self.guid = guid
        self.group = group
        self.department = department
        self.server_name = server_name
