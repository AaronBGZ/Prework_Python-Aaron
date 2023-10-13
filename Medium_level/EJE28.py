#Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.

'''def suma_quadrados_pares(n):
  return sum(i**2 for i in range(2, n+1, 2))
n = 10
print(suma_quadrados_pares(n))'''

def suma_cuadrados_pares(n):
    # Inicializamos una variable para llevar la suma
    suma = 0
    # Iteramos a través de los números desde 1 hasta el número dado
    for i in range(1, n + 1):
        # Verificamos si el número es par
        if i % 2 == 0:
            # Si es par, calculamos su cuadrado y lo sumamos a la suma
            suma += i ** 2
    return suma
numero = 6
resultado = suma_cuadrados_pares(numero)
print(f"La suma de los cuadrados de los números pares hasta {numero} es: {resultado}")
