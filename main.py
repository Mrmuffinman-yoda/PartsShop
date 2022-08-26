from dataLoader import customers , administrator, employees , items
from pwinput import pwinput
import time

global UserData
Userdata = None # Filled with user information from Dictionary
# Short introduction
print("Welcome to Spekz")
print("PC Hardware on a budget!")

# Wait period then asks for user details
time.sleep(1.5)
userType = str(input("Select one -->  \t customer : c \t employee : e \t admin:a  >> ")).lower()
username = str(input("What is your username?: "))

# Set usertype to Administrator , employee or customer 
if userType =="a":
    userType = "admin"
    userData = administrator[username]
elif userType == "c":
    userData = customers[username]
    userType = "customer"
elif userType == "e":
    userData = employees[username]
    userType = "employee"
# While loop to check if input value is equal to password recorded in files

while True:
    password = str(pwinput("What is your password? : "))
    if userData.returnPass() == password:
        
        print(
            f"logged in as {userData.fullname()[0]} {userData.fullname()[1]}")
        break


# RegionMain Menu
while True:
    print(f"Options : \t Logged in as {userData.username}")
    menuInput = str(input("Main Menu:"))

# endRegion