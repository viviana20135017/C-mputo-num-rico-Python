''' 
Tarea 2: Evaluar las funciones y=sin(2x) para x=1.3 
En la función y=e^(1-2x) en x=-0.45

Usando Método de Newton
'''
import math
from cmath import sin

x=1.3
y=sin(2*x)
print("Funcion y=sin(2x) para x=1.3 es: ", y)

x=-0.45
y = math.exp(1-2*(x))
print("Funcion y=e^(1-2x) en x=-0.45 es: ", y)

