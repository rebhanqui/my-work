information = {}
name = input("Please enter your name: ")
# prints ('Reb', {'PANDS': '100'})
studentinformation = name, information

for i in range(1):
    module = input("Enter module name: ")
    grade = input("Enter final grade: ")

    information[module] = (grade)

print(studentinformation)

#ref: https://bobbyhadz.com/blog/python-add-user-input-to-dictionary