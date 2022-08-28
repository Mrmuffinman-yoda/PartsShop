import dataWriter
class customer:
    def __init__(self, firstname, lastname, username, password, email):
        self.username = username
        self.__password = password
        self.email = email
        self.__firstname = firstname
        self.__lastname = lastname

    # def __repr__(self):
    #     return [{self.username} ,{self.__firstname} , {self.__lastname} , {self.email}]

    # def __str__(self):
    #     return f"{self.username} \t {self.__firstname} \t {self.__lastname} \t {self.email}"
    def dataDumper(self):
        data = [self.username,self.__password,
                self.email,self.__firstname,self.__lastname]
        return data
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
    
    def dataDump(self,name,data,debug):
        dataWriter.dataWriter(name,data,debug)

class items:
    def __init__(self, itemName, Value, ID):
        self.name = itemName
        self.value = Value
        self.ID = ID

    def price(self):
        return self.value


if __name__ == "__main__":
    # raise PermissionError("Cannot run this , run main file instead.")
    shaggy = customer ("Shaggz" , "scooby" , "SSoobs" , "1234" ,"Shagy@gmail.com")
    print(shaggy)