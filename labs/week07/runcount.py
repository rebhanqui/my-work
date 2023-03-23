filename = "count.txt"

def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

num = readNumber
print(num)
print("done")

def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

writeNumber(3)
print("done")

num = readNumber()
num += 1
print(f"we have run this program {num} times")
writeNumber(num)
