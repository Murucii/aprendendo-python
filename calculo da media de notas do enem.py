print ("==========Media do Enem==========")

nota_1 = float(input("nota de Linguagens:"))

if nota_1 < 400:
    print('não passou')

if nota_1 >= 400:
    print ('passou nessa.')
               
nota_2 = float(input("nota de  Humanas:"))
  
if nota_2 < 400:
    print('não passou')

if nota_2 >= 400:
    print ('passou nessa.')  
  
nota_3 = float(input("nota de Naturezas:"))

if nota_3 < 400:
    print('não passou')

if nota_3 >= 400:
    print ('passou nessa.')

nota_4 = float(input("nota de Matemática:"))

if nota_4 < 400:
    print('não passou')

if nota_4 >= 400:
    print ('passou nessa.')

nota_5 = float(input("Nota da Redação:"))

if nota_5 < 500:
    print('não passou')

if nota_5 >= 500:
    print ('passou nessa.')

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) // 5

print (f"sua nota do enem foi:{media}")

if media <= 550:
    print ('Lamento dizer... mas voce não passa em muita coisa :<')
    
if media >= 650:
    print ('Voce tem muitas chances!! :D')
    
