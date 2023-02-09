# this program prints out a random fruit from a list
import random

# can use lists or tuples here, tuple preferably
fruits = ('Apple', 'Orange', 'Pears', 'Banana')

index = random.randint(0, len(fruits)-1)
fruit = fruits[index]
print("A random fruit: {}".format(fruit))