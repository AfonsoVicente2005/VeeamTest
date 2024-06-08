import time
import os
import shutil
import filecmp


def origin():
    originpath = input("Choose the Original Folder Path: ")
    if os.path.exists(originpath):
        print("New Origin Path = " + originpath)
        input("Press Enter to continue...")
        return originpath
    else:  
        print("Path not found")
        input("Press Enter to continue...")
def replica():
    replicapath = input("Choose the Replica Folder Path: ")
    if os.path.exists(replicapath):
        print("New Replica Path = " + replicapath)
        input("Press Enter to continue...")
        return replicapath
    else:
        print("Path not found/Unknown\nDo you wish to create a new folder\n Attention that the new folder will be created at the current working directory.")
        con = input("Yes or No? Y/N")
        if(con == "yes" or con == "y"):
            d = os. getcwd()
            e = input("Choose the name of the replica directory: ")
            f = os.path.join(d, e)  
            os.mkdir(f)
            if os.path.exists(f):
                print("New Replica Path = " + f)
                input("Press Enter to continue...")
                return f
        else:
            input("Press Enter to continue...")
def synctime():
    synctimes = int(input("How much seconds you want to sync both folders: "))
    
    print("The folder will be copied for each ", synctimes, " Seconds")
    input("Press Enter to continue...")
    return synctimes
def logpath():
    logp = input("Choose the Logs Folder Path: ")
    if os.path.exists(logp):
        print("New Logs Path:\n"+logp)
        input("Press Enter to continue...")
        return logp
    else:
        print("Path not found")
        input("Press Enter to continue...")

def execution(originpath, replicpath, logpath):
    

    count = 1
    counta = str(count)
    logname = 'log' + counta + ".txt"
    newlog = os.path.join(logpath, logname)

    while os.path.exists(newlog):
        count+=1
        counta = str(count)
        logname = 'log' + counta + ".txt"
        newlog = os.path.join(logpath, logname)

    for filename in os.scandir(originpath):
        if filename.is_file():
            destination = replicpath+"/"+filename.name
            if os.path.exists(destination):
                if filecmp.cmp(filename.path, destination):
                     pass
                else:                    
                    shutil.copy2(filename.path, destination)
                    with open(newlog, "a") as file: 
                        file.write(filename.name + " was copied\n") 
                        print(filename.name+" was copied")
            else:
                shutil.copy2(filename.path, destination)
                with open(newlog, "a") as file: 
                    file.write(filename.name+"  was created\n")
                    print(filename.name+" was created")
        if filename.is_dir():
            destination = replicpath+"/"+filename.name
            if os.path.exists(destination):
                if filecmp.cmp(filename.path, destination):
                    pass
                else: 
                    shutil.copytree(filename.path, destination, dirs_exist_ok=True)
            else:
                shutil.copytree(filename.path, destination)
                with open(newlog, "a") as file: 
                    file.write(filename.name+" was created\n") 
                    print(filename.name+" was created")
    for filename in os.scandir(replicpath):
        checkexit = originpath+"/"+filename.name
        if filename.is_file():
            if os.path.exists(checkexit):
                pass
            else:
                os.remove(filename.path)
                with open(newlog, "a") as file: 
                    file.write(filename.name+" was removed\n") 
                    print(filename.name+" was removed")
        if filename.is_dir():
            if os.path.exists(checkexit):
                pass
            else:
                shutil.rmtree(filename.path)
                with open(newlog, "a") as file: 
                    file.write(filename.name+" directory removed\n") 
                    print(filename.name+" directory removed")


def menu():
    
    originpat = str
    replicpat = str
    synctiming = int
    logpat = str

    originpat = ""
    replicpat = ""
    synctiming = ""
    logpat = ""


    while True:
        print("-----------CONFIGURATION------------")
        print("1 - Choose origin folder path ")
        print("2 - Choose replica folder path")
        print("3 - Choose Sync time")
        print("4 - Choose log path")
        print("--------------EXECUTE---------------- ")
        print("5 - Execute copy")
        print("-------------------------------------- ")
        print("6 - Exit program")

        a = input("\n\nChoose a Number to continue\n")

        if(a == "1"):
            originpat = origin()
            print(originpat)
        elif(a == "2"):
            replicpat = replica()
            print(replicpat)
        elif(a == "3"):
            synctiming = synctime()
        elif(a == "4"):
            logpat = logpath()
        elif(a == "5"):
            if originpat == "" or originpat == None:
                print("Origin Path is empty/Invalid")
                input("Press Enter to continue...")
            elif replicpat == "" or replicpat == None:
                print("Replic Path is empty/Invalid")
                input("Press Enter to continue...")
            elif synctiming == "" or synctiming == None:
                print("Sync Timing is empty/Invalid")
                input("Press Enter to continue...")
            elif logpat == "" or logpat == None:
                print("Log Path is empty/Invalid")
                input("Press Enter to continue...")
            else:
                while True:               
                    execution(originpat, replicpat, logpat)
                    time.sleep(synctiming) 
        elif(a == "6"):
            exit()
        else:
            print("Invalid operation")
    


menu()