while True:
	name = str(input("Please Enter name: "))
	trueName = "yakup"
	if 3 > len(name) or len(name) > 15:
		print("Error! Please Enter name again")
	elif name == trueName:
		print("hello dude")
		break
	elif name.lower() == "quit":
		print("goodbye")
		breaks