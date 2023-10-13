#8. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
# def valor(a)
#   if a > 0 
#     print('el valor es positivo')
#   else a < 0 
#     print('el valor es negativo')
#   elif a == 0
#     print('el valor es 0')

def verificar_signo(num):
  if num > 0: 
    return "positivo" 
  elif num < 0:
    return "negativo"
  else: 
    return "cero" 
num = float(input("Ingresa un número: ")) 
print("El número es:", verificar_signo(num))