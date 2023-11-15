
import math
import random



# parameterbe kap 2 szamot, ezen 2 egesz szam kozotti paros szamok osszeget szamolja ki az eljaras
def ParosSzamok(szam1,szam2):
	osszeg = 0	
	while szam1 != szam2:
		szam1 += 1
		if szam1 % 2 == 0:
			print("paros:",szam1)
			osszeg += szam1

	return osszeg	#print("osszeg:",osszeg)





def ParosSzamok2(szam1,szam2):
	osszeg = 0
	for i in range(szam1,szam2,1):
		if i % 2 == 0:
			print("paros:",i)
			osszeg += i
	return osszeg









#[30,1000) --> 30 benne van, 1000 nincs benne
#math.floor(random.random()*(1001-30)+30)




# general 20db veletlen szamot -10 és +10 kozott, szamold meg hany negativ van kozotte, a visszateresi ertek a negativ száma
def NegativSzamok():
	i = 0
	osszeg = 0
	while i != 20:
		veletlen = math.floor(random.random()*(11-(-10))+(-10))
		print("veletlen:",veletlen)
		if veletlen < 0:
			osszeg += 1
		i += 1	
	return osszeg











# fuggveny, general 10db random szamot 12 es 33 kozott, és visszater ezek osszegevel
def VeletlenekOsszege():
	osszeg = 0
	for i in range(0,10,1):
		veletlen = math.floor(random.random()*(34-12)+12)
		print("veletlen",veletlen)
		osszeg += veletlen
	return osszeg













# generalj 8db veletlen szamot [20,50] intervallumban és visszatér ezek kozul a legnagyobb szammal
def LegnagyobbVeletlen():
	legn = 0
	for i in range(0,8,1):
		veletlen = math.floor(random.random()*(50-20)+20)  #[20,50]
		print("veletlen",veletlen)
		if veletlen > legn:
			legn = veletlen
	return legn









#kerjunk be 3 db egesz szamot, mekkora a szamok atlaga?
def Atlag():
	osszeg = 0
	for i in range(0,3,1):
		szam = int(input(f"Kérem az {i+1}. egész számot: "))
		osszeg += szam
	return osszeg/3









#kerjunk egesz szamokat amig 0-t nem ad, irjuk ki a szamok atlagat
def Nulladik():
	szam = -1
	osszeg = 0
	szamlalo = 0
	while szam != 0:
		szam = int(input("Kérek egy számot: "))
		print("szam:",szam)
		osszeg += szam
		szamlalo += 1
	return osszeg/(szamlalo-1)

























