# Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
def no_comun(lista1, lista2):
  return list(set(lista1) & set(lista2))
  #aqui pido que me devuelva una lista sacadas de las 2 listas en las que me de los valones que no coinciden en ambas
  # seria lo opuesto a &, que te devuelva solo las que se repiten en ambas
lista1 = [3,4,5]
lista2 = [5,6]
print(no_comun(lista1, lista2))