'''
O Desafio dos Três Números (O mais difícil!)
Objetivo: Encontrar o maior número entre três opções diferentes.
Como fazer: Peça para o usuário digitar três números (num1, num2 e num3).
Usando apenas estruturas condicionais (if, elif, else), descubra qual deles é o maior e imprima o resultado na tela.
Dica: Você precisará testar se um número é maior que o outro e, dentro dessa condição (ou usando elif), testar com o terceiro.
'''
numero_1 = float(input('digite um numero:'))
numero_2 = float(input('digite mais um numero:'))
numero_3 = float(input('digite mais outro:')) 
if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'{numero_1} é maior que {numero_2} e {numero_3}')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'{numero_2} é maior que {numero_1} e {numero_3}')
elif numero_3 > numero_1 and numero_3 > numero_2:
    print(f'{numero_3} é maior que {numero_1} e {numero_2}')

    


        