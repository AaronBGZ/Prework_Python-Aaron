#Define una función que encuentre el elemento más común en una lista.
'''
from collections import Counter
def buscar_comun(lista):
  contador = Counter(lista)
  buscar_comun = contador.most_common(1)
  return buscar_comun[0][0]
lista = [1,2,2,3,4,4,4,6]
print(buscar_comun(lista))
'''
from collections import Counter
def elemento_mas_comun(lista):
  return Counter(lista).most_common(1)[0][0]
print(elemento_mas_comun([1, 2, 3, 2, 4, 2, 5]))
  #añadimos un contador aplicamos .most_common para ver el mas comun y (1)[0][0] para que te devuelva solo ese, si no ponemos nada te devolvera cada numero cuantas veces se repite.