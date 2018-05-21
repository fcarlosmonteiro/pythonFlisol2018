# -*- coding: utf-8 -*-

lista1 = [1,2,3]
lista2 = ["a","b","c"]
print "Lista 1: ", lista1
print "Lista 2: ", lista2

for i in range(len(lista2)):
	lista1.append(lista2[i])
print(lista1)