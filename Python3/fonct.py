def tcKontrol(tcNo:str)->bool:
	if len(tcNo)<11 or len(tcNo)>11:
		return False

	tcList = []
	tCift = 0
	tTek = 0 
	rToplam = 0 

	for i in tcNo:
		tcList.append(int(i))

	for x in range(0,9,2):
		tCift += tcList[x]
	print(tCift)
	for z in range(1,9,2):
		tTek += tcList[z]
	hane10 = (tTek*7 - tCift)%10
	for y in range(10):
		rToplam += tcList[y]
	hane11 = rToplam%10
	if(tcList[9]==hane10 and tcList[10]==hane11):
		return True
	else:
		return False



tcNo = input("Tc giriniz: ")
if tcKontrol(tcNo):
	print("başarılı giriş")
else:
	print("tc hatalı")