# --> Student portal

class Student:
    name = ""
    age = 0
    branch = ""
    RollNo = 0

    def studentINFO(self,name,age,branch,RollNO):
        self.name = name
        self.age = age
        self.branch = branch
        self.RollNo = RollNO
        print("--- Student recoed created ---")

    def studentINFODisplay(self):
        print("----------------------------------------")
        print("--- Student Details ---")
        print("----------------------------------------")
        print("Studnet name : ",self.name)
        print("student age : ",self.age)
        print("student branch : ", self.branch)
        print("student rollno : ", self.RollNo)
        print("----------------------------------------")

s = Student()
while True:
    print("--------------------------------------")
    print("1. Fill the form")
    print("2. Dipslay your information")
    print("3. Exit")
    print("--------------------------------------")
    ch = int(input("pls enter ur choice : "))
    print("****************************************")
    match(ch):
        case 1:
            print("--- fill the form ---")
            print("----------------------------------------")
            name = input("Enter your name : ")
            age = int(input("Enter your age : "))
            branch = input("Enter your branch name : ")
            rollno = int(input("Enter your roll no : "))
            s.studentINFO(name,age,branch,rollno)
            print("----------------------------------------")

        case 2:
            s.studentINFODisplay()
            print("-----------------------------------------")

        case 3:
            print("--- Logout ---")
            break
