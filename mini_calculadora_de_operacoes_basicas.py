print('==========Mini Calculadora de Operações Básicas==========')
#Criar um menu simples que faz uma operação matemática.

#1-Peça para o usuário digitar dois números.
numero_1 = int(input('digite um numeros:'))
numero_2 = int(input('digite outro numero:'))

operação_1 = numero_1 + numero_2
operação_2 = numero_1 - numero_2

#Mostre uma mensagem pedindo para ele escolher uma operação: + para somar ou - para subtrair.
print('==========Soma ou Subtração==========')

operadores = input('escolha um operador entre + ou -:')
 
  
#Use if e elif para verificar qual operação ele escolheu, faça o cálculo e mostre o resultado. Se ele digitar algo diferente, exiba "Operação inválida".
if operadores == "+":
    print(f'O resultado da soma é:{operação_1}')
elif operadores == "-":
    print(f'O resultado da subtração é:{operação_2}')
else:
    print('==========Operação Invalida==========')
    
