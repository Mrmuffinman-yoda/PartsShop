import main
import json


def dataWriter(name,data,debug = "no"):
    filename = name
    SerialisedData = {}
    for i in data:
        SerialisedData[i] = data[i].dataDumper()
    if debug == "yes":
        print(SerialisedData)
    file = open(f"data/{filename}.JSON", "w")
    file.write(json.dumps(SerialisedData))
    file.close()
    if debug == "yes":
        print("Data Dumped")

# def fileDumper(e,a,c,i):
#     dataWriter("employees", e)
#     dataWriter("administrator", a)
#     dataWriter("customers", c)
#     dataWriter("items", i)
