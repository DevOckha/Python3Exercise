def isLeapYear(year: int) -> bool:
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
		else:
			return True
	return False


for year in range(2020, 1900, -1):
	if isLeapYear(year):
		print(f"{year} is a leap year")