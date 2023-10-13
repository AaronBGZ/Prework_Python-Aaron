#Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
#Tupla: conjunto ordenado e inmutable de elementos del mismo o diferente tipo.

def ordenar_por_ultimo_elemento(tuplas):
    # Utilizamos la función sorted con un argumento key personalizado
    # para ordenar la lista de tuplas por el último elemento de cada tupla
    return sorted(tuplas, key=lambda x: x[-1])
mi_lista = [(1, 5), (2, 3), (3, 8), (4, 1)]
resultado = ordenar_por_ultimo_elemento(mi_lista)
print(resultado)

'''Utilizamos la función sorted() para ordenar la lista de tuplas lista_de_tuplas.
Especificamos un argumento key que es una función lambda lambda x: x[-1]. Esta función toma una tupla x y devuelve su último elemento x[-1], que se utilizará para determinar el orden de las tuplas.
La lista resultante, lista_ordenada, contendrá las tuplas ordenadas por el último elemento de cada tupla.'''

'''Esta función ordenará la lista de tuplas en función del último elemento de cada tupla de manera ascendente. Puedes cambiar el orden si necesitas que sea descendente agregando reverse=True como argumento adicional a la función sorted().'''