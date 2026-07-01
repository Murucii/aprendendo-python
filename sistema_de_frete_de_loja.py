'''
Seu programa deve verificar se o usuário tem direito a frete grátis. As regras são:

O valor da compra deve ser maior ou igual a 100

E o cliente precisa estar cadastrado no programa de fidelidade
Se as duas condições forem verdadeiras, mostre: "Frete grátis aplicado!"
Caso contrário: "Frete não disponível gratuitamente."
'''
print('====================Checagem de Frete====================')
valor_da_compra = float(input('Qual o valor da compra?'))
programa_de_fidelidade = input('Voce esta cadastrado no programa de fidelidade?')

if valor_da_compra >= 100 and programa_de_fidelidade == 'sim':
    print('Frete grátis aplicado!')
    print('Boa compra! :D')
else:
    print('Frete não disponível gratuitamente.')
    print('Pague o valor inteiro.')
print('====================Fim da Checagem======================')
    
