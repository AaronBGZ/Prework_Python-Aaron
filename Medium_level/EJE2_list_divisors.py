# Define una función que tome un número y retorne una lista de sus divisores.

def divisores_de(n):
  return [i for i in range(1, n + 1) if n % i == 0]
n = int(input("Ingrese el número: ")) 
print(divisores_de(n))