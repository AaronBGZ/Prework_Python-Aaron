#Define una función que tome un número y retorne la suma de sus dígitos.
def suma_digitos(n): #definimos la funcion
  return sum(int(digito) for digito in str(n))
  # sumar int{numero entero}, para variable{digito} en str{cadena de texto} de otra varible
print(suma_digitos(123))

