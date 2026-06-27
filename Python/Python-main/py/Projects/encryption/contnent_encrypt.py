
def file():

	with open("page.txt","a") as file:
	
		print("Enter ur content here type EXIT to exit....")
		while 1<2:
			content = input()
			if(content == "EXIT"):
				break

			else:

				stripped = content.strip()
				for x in stripped:
					
					ord_val = str(ord(x))
					file.write(ord_val)


file()
