#Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
def orden_inverso(lista):
  return lista[::-1]
lista = [1,4,2,3]
#lista que queremos que nos devuelva: [3,2,4,1]
print(orden_inverso(lista))
