''' 
Tarea : 
Resuelve la siguiente Integración numérica

Regla del Trapecio
Regla de Simpson

'''

a = -1
b = 2
c = (a+b)/2

def f(x):
    return (7**-x)+3

r = ((b-a) / 2) * (f(a) + f(b))
print("Regla del Trapecio:", r)

r2 = ((b-a)/6)*(f(a)+4*f(c)+f(b))
print("Regla de Simpson:",r2)
