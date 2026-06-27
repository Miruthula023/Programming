#rock paper scissor game

import random

def rps():

	x = 1
	while x > 0:

		user_inp = input("Enter Rock paper or scissor : ")
		category = ["rock","paper","scissor"]
	
		rand_num = random.randint(0,2)

		print("Computer:",category[rand_num])

		if(user_inp != "paper" and user_inp != "rock" and user_inp != "scissor"):
			print("Enter the name coorectly")
			break

		elif(user_inp == category[rand_num]):

			print("Match draw")
		elif(user_inp == "rock" and category[rand_num] == "paper"):
		
			print("ur out")

		elif(user_inp == "paper" and category[rand_num] == "scissor"):

			print("ur out")
			
		elif(user_inp == "scissor" and category[rand_num] == "rock"):
			print("ur out")
	
		
		else:
			print("congrats! ur win...")

rps()
