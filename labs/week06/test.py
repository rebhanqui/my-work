print(1,2,3, sep=" . ", end="\t")

def fun1(*args):
    print(type(args))
    for val in args:
        print(val)

fun1("a", "b", "c")

# Initialize an empty dictionary
my_dict = {}

# Ask the user for input
while True:
    key = input("Enter a key (or 'q' to quit): ")
    if key == "q":
        break
    value = input("Enter a value: ")

    # Add the key-value pair to the dictionary
    my_dict[key] = value

#print(my_dict)
def readNum(message = "enter a number"):
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
            print("that was not a number ", end="\t")
    return num

num1 = readNum()
num2 = readNum()

answer = num1 * num2

print(f"answer is {answer}")

