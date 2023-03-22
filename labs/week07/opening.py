FILENAME = "data.txt"

with open(FILENAME, 'rt') as f:
    for data in f:
        print(data.strip()) #, end="") another strip option, strip best for linux etc

with open("data2.txt", "w+") as f:
    f.write("how now brown cow\n")
    f.write("how now brown cow\n")
    f.seek(0) #starts read from byte 0 or the beginning no need to 'cat' file to see text
    data = f.read()
    print(data)

print("done")