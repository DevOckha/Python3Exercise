 def delNumber(numbers: str) -> bool:
	addNumber = list()
	for number in numbers:
		addNumber.append(int(number))
	for same in addNumber:
		if addNumber.count(same) > 1:
			addNumber.remove(same)
			addNumber.sort()			
	return addNumber

while True:
	ınputNumbers = input("lütfen en az 10 adet tamsayı giriniz: ")
	if len(ınputNumbers) >= 10:
		print(delNumber(ınputNumbers))
		break
	else:
		print("lütfen en az on adet tamsayı giriniz")



