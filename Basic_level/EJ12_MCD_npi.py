#12. Dados dos números, crea una función para encontrar el (MCD) de esos dos números.
def mcd(x, y)
  while y: 
    x, y = y, x % y # no entiendo, preguntar
    return x

x = int(input("Ingrese el primer número: ")) 
y = int(input("Ingrese el segundo número: "))

print("El MCD es:", mcd(x, y))