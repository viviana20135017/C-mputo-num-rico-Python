import numpy 

moneda = ['cara', 'sello', 'cara', 'sello']

def selectRandom(moneda):
  return numpy.random.choice(moneda, 4)

print("La cara de la moneda es:: ", selectRandom(moneda))
