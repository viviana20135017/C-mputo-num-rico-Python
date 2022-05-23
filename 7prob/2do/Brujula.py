import numpy 

brujula = ['norte', 'este', 'sur', 'oeste']

def selectRandom(brujula):
  return numpy.random.choice(brujula, 4)

print("Direcciones cardinales: ", selectRandom(brujula))
