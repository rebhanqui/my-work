#Author: Rebecca Quinn

#READS IN USERS DETAILS

while True:
    example = str(input("Name: ")), {input("Module here: "):input("Grade here: ")}
#prints results in for loop unless nothing entered
#for key in example:
    #print(key)
#else:
    #print(f"Please enter your information to continue: {example}")

    if example == ("", {"":""}):    
        print("Please press enter to continue and enter your information ")
        break
    else:
        print(example)








#ref: https://www.youtube.com/watch?v=Hgcd86lQc70
#ref: https://bobbyhadz.com/blog/python-add-user-input-to-dictionary