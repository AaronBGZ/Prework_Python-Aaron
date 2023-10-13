# Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
def sumar_digitos(numero):
  suma = 0
  while numero > 0:
    suma += numero % 10
    numero //= 10
  return suma 
  num = int(input("Ingresa un número: "))

print("La suma de los dígitos es:", sumar_digitos(num))