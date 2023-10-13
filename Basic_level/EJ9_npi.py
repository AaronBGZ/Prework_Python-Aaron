# 9. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
def contar_letras(word):
  contador = 0
  for letra in word:
    if letra.isalpha(): 
                        #The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False.
      contador += 1
    return contador
word = input("Ingresa una palabra: ")
print("La cantidad de letras es:", contar_letras(word))