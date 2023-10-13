#Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
def contar_M_m(cadena):
  M = sum(1 for letra in cadena if letra.isupper())
  m = sum(1 for letra in cadena if letra.islower())
  return M, m
cadena = 'CKJFLNfljrndc'
print(contar_M_m(cadena))
