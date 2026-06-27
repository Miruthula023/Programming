class String:

	def __init__(self):
		self.lower = 0
		self.upper = 0
		self.vowel =  0
		self.consonants = 0
		self.space = 0
		self.string = ''
	def get_str(self):

		self.string = str(input("Enter the string : "))
		
	def count(self):

		for x in self.string:

			if(x.isupper()):

				self.upper +=1

			if(x.islower()):

				self.lower += 1

			if(x in ('AEIOUaeiou')):

				self.vowel += 1

			if(x == " "):

				self.space +=1

		self.consonants = self.upper+self.lower-self.vowel


	def disp(self):


		print("%d Uppercase letters"%self.upper)
		print("%d lowercase letters"%self.lower)
		print("%d vowels"%self.vowel)
		print("%d spaces"%self.space)
		print("%d consonants"%self.consonants)





S = String()
S.get_str()
S.count()
S.disp()
