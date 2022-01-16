name = str(input("Please Enter name: "))
lastName = str(input("Please Enter surname: "))

if 3<(len(name) and len(lastName))<15:
	print(f"Hi {name} {lastName}")
else:
	print("ERROR")