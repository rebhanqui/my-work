# reads in percentage mark and prints related grade

# mark number


# grade result

percentage = float(input("Enter your percentage: "))
# will print the inputted number

if percentage < 0 or percentage > 100:
    # error handling
    print ("Please enter a number between 0 and 100")
elif percentage < 40: 
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60: 
    print("Merit 2")
elif percentage < 70: 
    print("Merit 1")
else:
    print("Distinction")
