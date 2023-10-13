#Define una función que reciba una lista de números y retorne el promedio de los números en la lista.

#promedio es sumar todos los numeros de una lista y dividirlos por la cantidad de numeros
#la idea general ser hacer un sum(lista) para sumarlo tod y dividirlo por el conteo de la longitud de caracteres osea si tengo 1,2,3 la suma seria 6 y la longitud de caracteres seria 3 entonces 6/3= 2, len se puede usar tambien para numeros no solo cadenas.
def promedio(lista):
  return sum(lista) / len(lista)
lista = [1,2,3]
print(promedio(lista))
