#Define una función que reciba una lista de palabras y un entero n y retorne la lista de palabras que son + largas o = que n.

def filtrar_lista(lista_palabras, n):
  return [palabra for palabra in lista_palabras if len(palabra) >= n]

lista_palabras = ['camion','lamento', 'ser', 'estar', 'parecer']
print(filtrar_lista(lista_palabras, 5))