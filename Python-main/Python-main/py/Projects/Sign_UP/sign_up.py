import csv

class form:

	__EMAIL = input("EMAIL : ")
	__USERNAME = input("USERNAME :")
	__PASSWORD = input("PASSWORD : ")
	__CONFIRM_PASSWORD = input("CONFIRM PASSWORD : ")
	DATA_COLLECTION = [__EMAIL,__USERNAME,__PASSWORD,__CONFIRM_PASSWORD]

	def Bind_Datas(self):

                File = open("sign_form.csv",'a')
                write = csv.writer(File)
                write.writerow(self.DATA_COLLECTION)
                File.close()


	def Conditions(self):

		f = open("sign_form.csv","r")
		read = csv.reader(f)
		p = 0

		for x in read:

			if(self.__EMAIL == x[0]):

				print("You have already signed with  the Mail id {}".format(self.__EMAIL))
				p+=1
				break


		if(self.__PASSWORD != self.__CONFIRM_PASSWORD):

			p+=1
			print("Check confirm password... it doesn't match")

		elif("@gmail.com" not in self.__EMAIL):

			print("Enter a valid email eg: example@gmailcom")
			p+=1


		elif(len(self.__USERNAME) <= 3 or len(self.__PASSWORD) <= 8):

			p+=1
			print("Username must contains atlest 4 characters")
			print("password must contains atleast 8 characters")


		elif(p==0):

			self.Bind_Datas()
			print("Succesfully signed up!")

		
	

		f.close()


process = form()
process.Conditions()
