#10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.
def valor_absoluto(lista): 
  for i in range(len(lista)): lista[i] = abs(lista[i])
  # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
  # The len() function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.
  return lista 
numeros = [5, -12, 3, -8, 9] 
print("Lista con valores absolutos:", valor_absoluto(numeros))