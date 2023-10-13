#Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
def contar_vocales(cadena):
  return sum(1 for c in cadena.lower() if c in 'aeiou')
cadena = 'Alemania'
print(contar_vocales(cadena))
