# take an input of currency amount with a minus
# banks take amount in cents

#program takes float and returns cents without minus
import math

convert_pennies = float(input("How much do you have? "))
print(f"You have {abs(convert_pennies * 100)} total in cents")