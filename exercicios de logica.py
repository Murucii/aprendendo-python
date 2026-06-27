#exercicios de logica de programação com python
print('============================================================')
#numero 1:O Verificador de Votação, um programa que verifique se uma pessoa já pode votar

idade = int(input('qual a sua idade?'))
if idade >= 16:
    print('Voce ja pode votar')
else:
    print('Voce ainda não pode votar')

print('============================================================')
#numero 2: O Maior de Dois Números, Descobrir qual de dois números é o maior.

numero_1 = float(input( "digite um numero:"))

numero_2 = float(input("digite outro numero:"))

if numero_1 == numero_2:
    print('os numeros são iguais')
elif numero_1 > numero_2:
    print(f'O numero {numero_1} é maior que o {numero_2}')
elif numero_1 < numero_2:
    print(f'O numero {numero_1} é menor que o {numero_2}')


print('============================================================')
#numero 3: Calculadora de Média Escolar, Avaliar o desempenho de um aluno baseado em duas notas.

nota_1 = float(input('qual a sua nota?'))

nota_2 = float(input('qual a sua nota?'))

media = (nota_1 + nota_2) / 2
if media >= 7:
    print ('APROVADO!')
else:
    print ('REPROVADO!')

print('============================================================')
#numero 4: Par ou Ímpar? Descobrir se um número inteiro é par ou ímpar.

numero = int(input('me de um numero:'))
if numero % 2 == 0:
    print('esse numero é par')
else:
    print('esse numero é impar')


print('============================================================')
#numero 5: Simulador de Radar de Velocidade, Aplicar uma multa fictícia baseada na velocidade de um carro.

velocidade = float(input('velocidade do carro:'))
if velocidade > 80:
    print ('voce foi multado!')
else:
    print('Boa viagem, dirija com segurança.')

print('============================================================')

#numero 6: Classificador de Idade, Categorizar uma pessoa de acordo com a sua idade.

idade = int(input('Qual a sua idade?'))

if idade <= 12:    
    print('Criança')
elif 12 < idade <= 17:  # Corrigido para incluir o 12
    print('Adolescente')
elif 18 <= idade <= 59:  # Corrigido para incluir o 59
    print('Adulto')
else:
    print('Idoso')

print('============================================================')

#numero 7: Reajuste Salarial,Calcular o aumento de salário de um funcionário dependendo de quanto ele ganha.

#Pedir o salário atual do funcionário.

print('aumento salarial, se o salario for +3k, aumenta10%, se for -3k, aumenta 15%')
salario = float(input('Qual seu salario atual?'))

#Se o salário for maior que R$ 3.000,00, dê um aumento de 10% (multiplique o salário por 1.10).

if salario > 3000:
    aumento_1 = salario * 1.10
    print(f'Seu aumento salarial é de:{aumento_1: .2f}R$')
#Se for menor ou igual a R$ 3.000,00, dê um aumento de 15% (multiplique por 1.15).
else:
    aumento_1 = salario * 1.15
    print(f'Seu aumento salarial é de:{aumento_1: .2f}R$')
    
#numero 8: Qual é o Clima? Dar uma recomendação baseada na temperatura atual.
#Peça a temperatura em graus Celsius.
print('============================================================')

temp = float(input('Qual a temperatura?'))
if temp < 15:
    print(f'São {temp}Graus Celsius, esta frio, leve um casaco!')
elif temp >= 15 and temp < 25:
    print(f'São {temp}Graus Celsius,o clima esta agradavel!')
else:
    print(f'São {temp}Graus Celsius,está calor, hidrate-se')
print('============================================================')   

    


