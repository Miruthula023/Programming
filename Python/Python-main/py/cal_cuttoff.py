#to calculate cutoff marks

def calculation():

	maths_mark = int(input("Enter ur maths mark : "))
	physics_mark = int(input("Enter ur Physics mark : "))
	chemi_mark = int(input("Enter ur chemistry mark: "))

	calc = maths_mark+(physics_mark+chemi_mark)/2
	print("UR CUTOFF : ",calc)

calculation()
