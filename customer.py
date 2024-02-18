class Customer:
    def __init__(self, name):
        self.name = name
        self.account = None

    def set_account(self, account):
        self.account = account
