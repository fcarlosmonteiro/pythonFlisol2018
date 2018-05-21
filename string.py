string1 = "Remo "
string2 = "Campeao Paraense 2018"
string3 = string1 + string2
print string3

contLetra=0
for letra in string3:
	if letra == "a" or letra == "A":
		print "letra a encontrada"
		contLetra+=1
print "Quantidade de A's encontrada eh =",contLetra