#Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
def orden_inverso(cadena):
  return' '.join(cadena.split()[::-1]) #join juntar palabras, split separarlas
cadena = 'Hola prueba 11 de 100'
print(orden_inverso(cadena))

'''Utilizamos el método split() para dividir la cadena en palabras. Esto crea una lista de palabras utilizando el espacio como separador.
Luego, invertimos el orden de las palabras utilizando la notación de segmento palabras[::-1]. Esto crea una nueva lista con las palabras en orden inverso.
Finalmente, utilizamos el método join() para unir las palabras invertidas en una cadena nuevamente, separadas por espacios.'''