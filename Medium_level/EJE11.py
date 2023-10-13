#Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def palindromo(x):
  return x == x[::-1]
x = str(input("Ingrese la palabra: ")) 
print(palindromo(x))