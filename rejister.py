from validate_email_address import validate_email
from cryptography.fernet import Fernet
import re

class Rejister():
    def init(self, account, name, tell, email, password):
        self.account = account
        self.name = name
        self.number = tell
        self.email = email
        self.password = password


    def storage(self, account, name):
        self.account = account
        self.name = name
        self.email = emailConfirmation()
        self.numbers = tellConfirmation()
        self.password = passwordEncryption()

    def emailConfirmation(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)):
            validate = validate_email('kubasugrantonokello@gmail.com', verify=True)
            if validate is not None:
                return email



    def tellConfirmation(self, number):
        pattern = "^0(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$"
        matched = re.match(pattern, number)
        if bool(matched) is "True":
            return number
        return number

    def passwordEncryption(self, password):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encMessage = fernet.encrypt(password.encode())
        return password


