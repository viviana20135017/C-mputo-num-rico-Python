#Tarea 1: Desarrollar un programa para obtener el radio de un circulo inscrito en un triángulo de lados a, b, y c.
import math

a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))
c=int(input("Ingrese un numero: "))


if ((a < c) and (b < c)):
    s = 0.5*(a+b+c)
    r=math.sqrt(s*(s-a)*(s-b)*(s-c))/s
    
    print("El semiperímetro de un triángulo es: ", s)
    print("El valor del radio es: ", r)
else:
    print("c debe de ser mayor que a y b")
