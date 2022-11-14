class Login():
    def __init__(self, email, password):
        # log in variables
        self.email = email
        self.password = password
    def passwordCheck(self, password):
        decMessage = fernet.decrypt(encMessage).decode()
        if decMessage == password:
            return "password exist"