'''
Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim:

Nota 9 ou 10: "Excelente!"

Nota 7 ou 8: "Muito bom"

Nota 5 ou 6: "Regular"

Menor que 5: "Ruim"
'''
#classificacao = int(input('Escolha uma nota de 0 a 10 para o filme:'))
classificacao = int(input('Qual a sua nota para o filme?'))

if classificacao >= 9 and classificacao <= 10:
    print('Excelente!')
elif classificacao >= 7 and classificacao <= 8:
    print('Muito Bom!')
elif classificacao >= 5 and classificacao <= 6:
    print('Regular!')
else:
    print('Ruim')