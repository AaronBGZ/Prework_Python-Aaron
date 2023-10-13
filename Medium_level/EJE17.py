#Define una función que reciba un número y retorne la suma de sus dígitos al cubo.

def suma_dig_cubo(n):
  return sum(int(digit)**3 for digit in str(n)) #suma: introducimos digito **3 = elevarlo al cuadrado, str = texto 
n = 123
print suma_dig_cubo(n)

#return sum(int(dig)**3 for dig in str(n))