# Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.

def no_repeat(numeros_randoms):
  return list(set(numeros_randoms)) 
  #para que te devuelva la lista sin repetir ponemos list(set(y el nombre que le hayas dado a la lista ))
numeros_randoms = [1,4,5,6,4,5,7,6,66,6.6,6.666,'mba','barcelona']

print(no_repeat(numeros_randoms))

