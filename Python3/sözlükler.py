bannedMapping = {"amk":"***", "aq":"**"}
─▒nputString = input("Enter in sentence: ").split()
banned = ""

for ban in ─▒nputString:
	banned += f'{ban}'
	for b in bannedMapping.keys():
		if ban == b:
			banned = banned.replace(b, bannedMapping[b])
		else:
			continue

print(banned, end=" ")