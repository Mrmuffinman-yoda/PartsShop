import users
# Region Customers
Jake = users.customer("Jake","Paul","jake2090",
 "paulbrothers","jakePaul@watsman.nl")
Bryan = users.customer("Bryan","Nuke","BNuke203",
"nukers23","bryan_nukers@gmail.com")
Jordan = users.customer("Jordan","Taylor","jcarter39",
"cartsWhy","Jordan.T32@yahoo.com")
Drake = users.customer("Drake","Cooper","DcOops",
"Ooper99","Doops@telcom.net")
Sam = users.customer("Sam","Smith","Ssmiths",
"samlj","SamSmithy@grims.fr")
# endRegion
customers = {
    "jake2090": Jake, #paulbrothers
    "BNuke203": Bryan, #nukers23
    "jcarter39": Jordan,#cartsWhy
    "DcOops": Drake,#Ooper99
    "Ssmiths": Sam #samlj
}

#Region Employees
Ted = users.Employee("Ted", "Baker", "Tbakes",
                      "baker23", "tbaker47@vscode.pi")
Smith = users.Employee("Smith", "Stores", "SuperStore",
                       "sstorer", "SStores@snipers.net")
#endRegion
employees = {

}
# Region Administrators
Harison = users.admin("Harison","Sundaramoorthy","Mr Muffin Man","root","harisoncom@gmail.com")
# endRegion
administrator = {
    "Mr Muffin Man" : Harison,
}

items = {

}


if __name__ == "__main__":
    raise PermissionError("Cannot run this , run main file instead.")
