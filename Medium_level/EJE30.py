#Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
def cadena_mas_grande(lista):
  return max(lista, key=len)
  #En esta versión, utilizamos la función max con un argumento key que es la función len, lo que significa que max buscará el elemento en la lista que tenga la longitud máxima según la función len. Esto simplifica el código y hace que la búsqueda de la cadena más larga sea más eficiente y legible.
lista = ['awder', 'abyss', 'kovalczyk']
print(cadena_mas_grande(lista))