print ("==========O Calculador de Média Acadêmica==========")

#Peça o nome do aluno.

nome_do_aluno = input("qual seu nome?")

#Nota 1

primeira_nota = float(input("qual a sua primeira nota?"))

#Nota 2 

segunda_nota = float(input("qual a sua segunda nota?"))

#Nota 3 

terceira_nota = float(input("qual a sua terceira nota?"))

#média final do aluno.

media = (primeira_nota + segunda_nota + terceira_nota) / 3

#nome do aluno, as três notas que ele tirou e a média final.

print (f"{nome_do_aluno} sua media de nota foi {media: .2f}")

if media < 7:
    print ('Voce não passou. :<')

if media >= 7:
    print ('voce passou!')
    print ('==========PARABENS==========')



