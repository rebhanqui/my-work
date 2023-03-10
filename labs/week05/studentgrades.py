

studentName = str(input("What is your name? "))
module = str(input("Please enter your module code "))
grade = int(input("What grade did you receive? "))

student = {
    "name" : "{studentName}",
    "moduleDetails": [
    {
        "courseName" : "{module}"
        "courseResult" : "{grade}"
    }
    ]
}

studentResult = student.pop
print(studentResult)