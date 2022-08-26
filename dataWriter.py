import users
import pickle

def fileDumper(data,debug = "No"):
    file = open(f"data/{str(data)}.VOID" , "wb")
    pickle.dump(data,file)
    file.close()
    if debug == "Yes":
        print("Data Dumped")



fileDumper("DO NOT DELETE","No")