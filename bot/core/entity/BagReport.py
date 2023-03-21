class BagReport:
    def __init__(self, fullName, group, user, server, bag_report_message):
        self.server = server
        self.bag_report_message = bag_report_message
        self.user = user
        self.group = group
        self.fullName = fullName
