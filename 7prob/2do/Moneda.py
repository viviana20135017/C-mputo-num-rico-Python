import random

cara=0
sello=0
moneda=int(input("Ingrese un numero: "))
    
for i in range(moneda):
    if (random.choice(['cara', 'sello', ]) == 'cara'):
        cara+=1
    else:
        sello+=1

print("De", moneda,"monedas lanzadas" , cara, "fueron cara")
print("De", moneda,"monedas lanzadas" , sello, "fueron sello")
