# Define una función que reciba un número y retorne su representación en binario.

def a_binario(a):

  return bin(a).replace("0b", "")

a = int(input('ingresa un num: '))

print(a_binario(a))