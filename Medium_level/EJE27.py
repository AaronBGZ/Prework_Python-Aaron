#Define una función que tome una lista y retorne la lista sin duplicados.
def sin_repetir(lista):
  return list(set(lista)) #set elimina duplicados
lista = [1,2,3,3,4]
print(sin_repetir(lista))