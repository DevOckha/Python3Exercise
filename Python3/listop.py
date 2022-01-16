names = []

while len(names) < 5:
    name = input('Enter name...: ')
    if name == "":
        break
    name = name.upper()
    if name not in names:
        names.append(name)
    else:
        print('ERROR ! the name you entered is on the list ')
        continue
print(names)
