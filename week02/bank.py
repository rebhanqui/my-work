# bank.py 
#prompts user to input 2 amounts, adds both and prints output to user

#input 1
bankIn = int(input("Lodgement Amount 1: "))

#input 2
bankIn2= int(input("Lodgement Amount 2: "))

#add both int numbers
totalLodgement = (bankIn + bankIn2)

#euro and cent amount output to user
print(f"You have lodged €{totalLodgement}\nThank You!")
