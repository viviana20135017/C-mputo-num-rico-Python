''' 
Tarea : Diferencias finitas progresivas
Resuelve la siguiente derivada 

f(x)=(sen^(3)2x)/(x^(4)+1) obtener f(2.45)

'''

from math import sin

x0=2.45

def f(x):
    return ((sin(2*x))**3)/(x**4+1)

h1=0.5
dn1=(f(x0+h1)-f(x0))/h1
print("Derivada numérica:",dn1)

h2=0.3
dn2=(f(x0+h2)-f(x0))/h2
print("Derivada numérica:",dn2)

h3=0.1
dn3=(f(x0+h3)-f(x0))/h3
print("Derivada numérica:",dn3)

h4=0.00001
dn4=(f(x0+h4)-f(x0))/h4
print("Derivada numérica:",dn4)

h5=0.00000001
dn5=(f(x0+h5)-f(x0))/h5
print("Derivada numérica:",dn5)

h6=0.0000000001
dn6=(f(x0+h6)-f(x0))/h6
print("Derivada numérica:",dn6)
