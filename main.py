from dataLoader import customers , administrator, employees , items
from pwinput import pwinput
import time
import os

debug = False
Userdata = None # Filled with user information from Dictionary
# Short introduction
os.system("cls")
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
    os.system("cls")
    print(f"Main Menu : \t Logged in as {userData.username}")
    # Main menu for different users and differing options depending
    # on what type of user is accessing this menu
    # User Access control (UAC)
    if userType == " customer":
        print(f"Options: 1 --> Items \t 2 -->Settings ")
        menuInput = str(input("Input --> "))
    elif userType == "employee":
        print(f"Options: 1 --> Items \t 2 -->Transactions \t 3 -->Add Customer \t 4-->Settings ")
        menuInput = str(input("Input --> "))
    elif userType == "admin":
        print(f"Options: 1 --> Items \t 2 -->Transactions \t 3 -->Add User \t 5-->Debug \t 5-->Settings ")
        menuInput = str(input("Input --> "))
        match menuInput:
            case "1":
                items()
            
# endRegion