#function that prints out a menu of commands to perform based on user selection and returns that selection
addStudent = ("(a) Add Student")
viewStudent = ("(v) View Students")
quitProgram = ("(q) Quit")
requestsOptions = (f"What would you like to do?\n{addStudent}\n{viewStudent}\n{quitProgram}\n")


def displayMenu():
    print(requestsOptions)
    selection = input("Type letter: (a/v/q) to select option: ").strip()

    return selection

students = []

#adds student name and modules to dict and into list of students and modules
def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Please enter your name: ")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)

#function reads in modules
def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit)" ).strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName

        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)

        moduleName = input("Enter next module name (blank to quit)").strip()
    return modules

def displayModules(modules):
    print("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}")

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);

#testing function main
selection = displayMenu
print(f"You have selected: {selection}")
while(selection != 'q'):
    if selection == 'a':
        doAdd(students)
    elif selection == 'v':
        doView(students)
    elif selection != 'q':
        print("\n\nplease select either a,v or q: ")
    selection = displayMenu()


