#Define una función que reciba una lista de números y retorne la suma acumulada de los números
def suma_acumulada(lista):
  total = 0 #contador
  suma_acumulada = []
  for numero in lista:
    total += numero
    suma_acumulada.append(total) 
    #.append añade total como siguiente en la suma_acumulada 
    #1,2,3,4.append(5) = 1,2,3,4,5
  return suma_acumulada
print(suma_acumulada([1, 2, 3, 4, 5]))
