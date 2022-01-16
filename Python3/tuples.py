#Tuple'lar değiştirilemez
#tuple içinde birden fazla item aldığı zaman tuple olur.

numbers = [(11,22),(33,55),(55,11),(11,44)]
elevenList = []
for i in numbers:
	if i[0] == 11 or i[1] == 11:
		elevenList.append(i)

print(elevenList)