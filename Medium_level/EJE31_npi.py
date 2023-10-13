#Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
''' def es_primo(num):
  if num < 2:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
      return True

def primeros_n_primos(n):
  primos = []
  numero = 2
  while len(primos) < n:
    if es_primo(numero):
      primos.append(numero)
    numero += 1
  return primos
print(primeros_n_primos(6)) '''

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def n_primeros_primos(n):
    if n <= 0:
        return []

    numeros_primos = []
    i = 2

    while len(numeros_primos) < n:
        if es_primo(i):
            numeros_primos.append(i)
        i += 1

    return numeros_primos

n = 10
resultado = n_primeros_primos(n)
print(resultado)