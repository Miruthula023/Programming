#generating random number 
#asking user to guess the number 
#checking and reporting whether guess is corrrect or not

#importing randm library
import random

def gen_rand():
	
	#minimum and maximum value to generate random numbers

	min_val = 0
	max_val = 5

	while max_val>min_val:

		ran_int = random.randint(min_val,max_val)
		print("guess the number from ",min_val,"to",max_val)
		us_input = int(input("Guess the number : "))
	
		#checking whether it is true or not

		if(ran_int == us_input):
			print("congrats!\n")
		else:
			print("wrong!\n")
			max_val-=5
	
		max_val+=5

gen_rand()
