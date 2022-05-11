''' 
Tarea : Interpolacion lineal
Dados: (-4, -2) y (1, 5) estimar el valor para x cuando y = 3.7

'''
p1=(-4,-2)
p3=(1,5)
y=3.7

def fn(y,p1,p2):
    a=(y-p1[1])*(p3[0]-p1[0])
    b=(p3[1]-p1[1])
    return p1[0]+(a/b)

print(fn(y,p1,p3))