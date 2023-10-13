#Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
def contar_caracteres(cadena):
  return {caracter: cadena.count(caracter) for caracter in cadena}
  #{} para decir que es un diccionario
  #caracter: para poner el caracter a la izquierda y el contador a la derecha, especificar del caracter que hablamos vaya.
  #variable en este caso la frase/cadena .count(caracter) contar caracteres para caracter en la variable, la frase/cadena
print(contar_caracteres('laalalalalalalall'))