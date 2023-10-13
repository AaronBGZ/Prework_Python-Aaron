# 1. Ejercicio: Define una función que tome dos números y retorne su suma.
def suma(a, b):
  return a + b
print(suma(5, 3))
# 2. Ejercicio: Define una función que tome un número y retorne su factorial.
def factorial(a):
 if a == 0:
  return 1
 else:
  return a * factorial(a-1)
print(factorial(9))
# 3. Ejercicio: Define una función que tome un número y determine si es primo.
def es_primo(a):
  for i in range(2, a):
    if a % i == 0:
      return False
  return True
print(es_primo(2))
# 4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
def sumar_lista(lista):
  return sum(lista)
print(sumar_lista([1, 2, 3, 4, 5]))
# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
def reversa(cadena):
  return cadena[::-1]
print(reversa("Hola"))