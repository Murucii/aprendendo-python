print ("==========O Calculador de Média Acadêmica==========")

#Peça o nome do aluno.

nome_do_aluno = input("qual seu nome?")

#Peça a Nota 1 (pode ser um número quebrado, ex: 7.5).

primeira_nota = float(input("qual a sua primeira nota?"))

#Peça a Nota 2 (ex: 8).

segunda_nota = float(input("qual a sua segunda nota?"))

#Peça a Nota 3 (ex: 6.5).

terceira_nota = float(input("qual a sua terceira nota?"))

#Calcule a média final do aluno.

media = (primeira_nota + segunda_nota + terceira_nota) / 3

#Mostre o nome do aluno, as três notas que ele tirou e a média final bem organizada na tela.

print (f"{nome_do_aluno} sua media de nota foi {media}")

