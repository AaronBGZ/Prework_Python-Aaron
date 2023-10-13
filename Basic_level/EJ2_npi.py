#2. Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
def factorial(n): 
resultado = 1 
  for i in range(1, n+1): 
    resultado *= i 
    return resultado 
num = int(input("Ingresa un número: "))
print("El factorial de", num, "es:", factorial(num))
#este no funciona, devuelve 1 con cualquier variable que se añada.