#Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
def segundo_maximo(lista):
  return sorted(set(lista), reverse=True) [1]
#sorted es para ordenar de menor a mayor
#set() es como una lista pero omite los duplicados
#reverse=True se usa para que el invertir el orden de "sorted" (de mayor a menor)
#[0] por ejemplo seria para que te de solo el primer numero de la lista, como queremos el segundo ponemos [1]
print(segundo_maximo([1, 3, 7, 6, 2, 5]))
