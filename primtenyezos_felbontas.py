import sys
szam = int(input("Írj be egy számot: "))
i = 1
szamlista = []
if szam <= 2:
	print("A szám legalább 3 legyen!")
	sys.exit()
while i <= szam:
	i += 1
	if szam % i == 0:
		szamlista.append(i)
		szam = szam / i
		i = 1
print(szamlista)
