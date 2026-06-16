#automatizando a loja
quantidade_camisas = 5
valor_camisa = 40
faturamento_total = quantidade_camisas * valor_camisa
print ("o faturamento total da loja foi de",faturamento_total)
#margem de lucro
faturamento = 200
custo = 30
lucro = faturamento - custo
margem = lucro / faturamento *100

print ("e a margem de lucro foi de", margem)
"""
>>> %Run -c $EDITOR_CONTENT
o faturamento total da loja foi de 200
e a margem de lucro foi de 85.0
>>> 
"""
