print ("==========Media do Enem==========")

nota_1 = float(input("nota de Linguagens:"))
               
nota_2 = float(input("nota de  Humanas:"))
               
nota_3 = float(input("nota de Naturezas:"))

nota_4 = float(input("nota de Matemática:"))

nota_5 = int(input("Nota da Redação:"))

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) // 5

print (f"sua nota do enem foi:{media}")