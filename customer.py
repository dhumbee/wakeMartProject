# Main class Customer
class Customer:
    # create object and instance variables
    def __init__(self, name):
        self.__name = name
        self.__cc_number = ""
        self.__security_code = ""
        self.__dbc_number = ""
        self.__db_pin = ""

    # user inputs cards information
    def inputCardInfo(self):
        self.__cc_number = input("Enter credit card number: ")
        self.__security_code = input("Enter 3 digit security code: ")
        self.__dbc_number = input("Enter debit card number : ")
        self.__db_pin = input("Enter 4 digit pin: ")

    # verify that the code customer enters at checkout is the same as what is on file
    def verifyCreditCard(self, code_entered):
        if code_entered == self.__security_code:
            return True
        else:
            return False

    # verify that the pin customer enters at checkout is the same as what is on file
    def verifyDebitCard(self, pin_entered):
        if pin_entered == self.__db_pin:
            return True
        else:
            return False

    # returns the last 4 digits of the credit card
    def creditCardLastFour(self):
        return self.__cc_number[-4:]

    # returns the last 4 digits of the debit card
    def debitCardLastFour(self):
        return self.__dbc_number[-4:]
