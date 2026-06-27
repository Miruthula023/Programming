#asking user for two names
#generating random mumbers
#assinging a meaning for each number and displaying

#importing random library

import random

def flame():

	Name1 = input("Enter ur name:")
	Name2 = input("Enter ur friend name:")

	category = ["Friends","Enemies","Best friends","Close friends","just friend"]
	Rand_number = random.randint(0,4)
	print(category[Rand_number])
	

flame()

