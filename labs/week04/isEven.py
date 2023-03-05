import math

number = input("enter an integer ")

while number != -1 :
    print(math.trunc(int(input("enter an integer ")))) #takes number and prints until -1 put in
    # using trunc to round of negetive integers that might be inputted by user
else (number % 2) == 0 :
    print (f"{number} is an even number")

else:
    print(f"{number} is an odd number")
# ref: https://favtutor.com/blogs/round-down-python


