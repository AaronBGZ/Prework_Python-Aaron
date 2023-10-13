#Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
def tienen_comun(lista1, lista2):
  return bool(set(lista1) & set(lista2))
lista1 = [1,2,3]
lista2 = [3,4,5]
print(tienen_comun(lista1, lista2))
#bool para que te de true o false en vez de devolverte lo que tienen en comun
#set para convertirlo en listas
#& se usa para ver la union, imprimir los que tienen en comun entre las 2 listas
# lista1 = [1,3,8,4,3]
# lista2 = [2,9,0,9]
# print(tienen_comun(lista1, lista2))