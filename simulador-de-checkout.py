#nome do produto.
produto = input ("qual o nome do produto?")

#quantidade desse produto que ele deseja comprar.

quantidade = int(input ("qual a quantidade desse produto que voce deseja comprar?"))

#preço unitário desse produto.

preço_unitario_do_produto = float(input ("qual o preço unitario do produto?"))

print('==========SUA COMPRA===============')

#valor total da compra (Quantidade × Preço Unitário).

valor_total_da_compra = quantidade * preço_unitario_do_produto

print(f'nome:{produto}')

if quantidade > 1:
    print(f'quantidade:{quantidade} unidades')
else:
    print(f'quantidade:{quantidade} unidade')
      
print(f'preço unitario do produto:{preço_unitario_do_produto: .2f}R$')

print ('==========VALOR DA COMPRA==========')

print (f'Preço total:{valor_total_da_compra: .2f}R$')

