#Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).

#basicamente creo que pide que marque los elemento que son repetidos, que esten contenidos en ambas listas

def interseccion(list1, list2):

  return list(set(list1) & set(list2))

list1 = [1,2,3,3,4.1,5,6,8,9,10]
list2 = [1,3,6,7,11,100]
print(interseccion(list1, list2))
