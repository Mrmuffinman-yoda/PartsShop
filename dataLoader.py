import users
import json
# Region Customers

customers = None
administrator = None
employees = None
items = None

def dataReader(filename):
    deserialisedDict = {}
    file = open(f"data/{filename}.JSON", "r")
    data = json.load(file)
    print(type(data))
    for i in data:
        name ,array = i,data[i]
    print(name)
    print(array)
    

dataReader("customers")