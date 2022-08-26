class customer:
    def __init__(self, firstname, lastname, username, password, email):
        self.username = username
        self.__password = password
        self.email = email
        self.__firstname = firstname
        self.__lastname = lastname

    def fullname(self):
        return self.__firstname, self.__lastname

    def resetPassword(self, newPassword):
        print("Password changed")
        self.__password = newPassword

    def changeUsername(self, newUsername):
        print("Username changed")
        self.username = newUsername

    def returnPass(self):
        return self.__password

    def returnEmail(self):
        return self.email

class Employee(customer):
    def additem(self,itemName):
        print(f" {itemName} Item theoretically added")

class admin(Employee):
    def changeItemPrice(self,price):
        print(f"Item price has been changed to {price}")

class merchendise:
    def __init__(self, itemName, Value, ID):
        self.name = itemName
        self.value = Value
        self.ID = ID

    def price(self):
        return self.value


if __name__ == "__main__":
    raise PermissionError("Cannot run this , run main file instead.")