#Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
def contar_digitos_letras(cadena):
  digitos = sum(c.isdigit() for c in cadena) #c.isdigit significa caracter es digit
  letras = sum(c.isalpha() for c in cadena) #c.isalpha significa caracter es letra
  return digitos, letras

cadena = "Hola123Mundo456"
digitos, letras = contar_digitos_letras(cadena)
print("Número de dígitos:", digitos)
print("Número de letras:", letras)