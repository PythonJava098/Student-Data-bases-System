# STUDENT DATA BASE MANAGEMENT
def sortDict(dictionary):
    myList = list(dictionary.keys())
    myList.sort()
    sortedDict = {}


    
    for element in myList:
        sortedDict[element] = dictionary[element]
    
    return sortedDict

def studentDetails():
    name = input("Enter Students's Name: ")
    grade = input("Enter Class: ")
    subj = input("Enter Subjects: ")
    address = input("Enter your present address: ")
    details = {
        "Name of the Student" : name,
        "Grade" : grade,
        "Subjects" : subj,
        "Address" : address,
    }

    return details

def updateDetails(details):
    slNo = int(input("Enter Your Roll No.: "))
    topic = input("Enter the subject of information you want to change: ")
    detail = input("Enter the details: ")

    details[slNo][topic] = detail
    return details

def delDetails(details):
    roll = int(input("Enter Roll No.: "))
    details.pop(roll)

    return details


def showDetails(details):
    slNo = int(input("Enter Roll No.: "))


    return details[slNo]

def functions(string):
    details = {}

    if string.lower() == "fill":
        roll = int(input("Enter roll no.: "))
        details[roll] = studentDetails()
    
    elif string.lower() == "update":
        updateDetails(details)

    elif string.lower() == "delete":
        delDetails(details)
    
    return details

print('''
To fill the data: Enter fill
To see specific data: Enter show
To update any Details: Enter update
To delete any student's Data : Enter delete
To see all data: Enter show all

REMEMBER : while updating follow the instruction 
''')

string = input("Enter keyword (every keyword is alphabet only): ")
length = len(string)

while length > 0:
    details = functions(string)
    print(details)
    if string.lower() == "show":
        print(showDetails(details))
    elif string.lower() == "show all":
        sortDict(details)
        print(details)
 
    string = input("Enter keyword (every keyword is alphabet only): ")
        
