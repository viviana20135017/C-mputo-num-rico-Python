''' 
Tarea : 
Resuelve la siguiente Integración numérica

Regla del rectángulo
Regla del punto medio

'''

from math import sin, sqrt

a = 0
b = 1.9724
c = (a+b)/2

def f(x):
    return 2*(sin(sqrt(x)))-x

r = f(a)*(b-a)
print("Regla del rectángulo:",r)

r2 = f(c)*(b-a)
print("Regla del punto medio:",r2)
