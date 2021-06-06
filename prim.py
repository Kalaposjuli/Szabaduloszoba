import math
import sys
szam = int(input("Írj be egy számot: "))
i = 2
if szam == 2:
	print("A szám prímszám")
	sys.exit()
elif szam == 1:
	print("A szám nem príszám")
	sys.exit()
elif szam <= 0:
	print("A szám legalább 1 legyen!")
	sys.exit()
while i <= math.sqrt(szam):
	if szam % i == 0:
		print("A szám nem prímszám.")
		sys.exit()
	i += 1
print("A szám prímszám")
