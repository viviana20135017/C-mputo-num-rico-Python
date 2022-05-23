''' 
Tarea : random.gauss()
    Los pesos de unos gatos se distribuyen normalmente, con media 4.23 kg
    y desviacion tipica 0.76kg

Los pesos de los gatos que estan a menos de una desviacion tipica de la media.
'''

import random
peso=0
peso = random.gauss(4.23, 0.76)
print("Peso de los gatos que estan a menos de una desviacion tipica de la media: ", peso)
