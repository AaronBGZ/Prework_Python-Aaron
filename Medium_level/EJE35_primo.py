#Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
def es_primo(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
    return True
print(es_primo(17))