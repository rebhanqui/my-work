import json
FILENAME = "testdict2.json"

def readDict():
    with open(FILENAME) as f:
        return json.load(f)

somedict = readDict()
print(somedict)