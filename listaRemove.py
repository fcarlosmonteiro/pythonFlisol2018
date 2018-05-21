# -*- coding: utf-8 -*-

lista = [1,2,10,3,4,10,5,6,10,7,8,10,9,10]
print "lista original \n",lista
cont=0
for num in lista:
	if num == 10:
		lista.remove(10)
		cont+=1
print "Quantidade de 10 removidos foi =",cont
print "lista nova \n",lista
