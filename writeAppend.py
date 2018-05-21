# -*- coding: utf-8 -*-

arquivo = open('file.txt', 'r') 
conteudo = arquivo.readlines()
conteudo.append('No FliSol\n')   # insira seu conteúdo

arquivo = open('file.txt', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()