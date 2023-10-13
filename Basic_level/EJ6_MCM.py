#6. Dados dos números, crea una función para encontrar el mínimo común múltiplo(MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.
def mcm(x, y):
   if x == 0 or y == 0:
    return 0
   else: maximo = max(x, y)
   while True: 
      if maximo % x == 0 and maximo % y == 0:
        return maximo
        maximo += 1
x = int(input("Ingrese el primer número: ")) 
y = int(input("Ingrese el segundo número: ")) 
print('El MCM es:', mcm(x, y))
############################################################################
# def mcm(x, y):
#   z = max(x, y)

#   while True:
#     if (z % x)