# 1.Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
def verificar_signo(num):
  if num > 0:
    return "positivo"
  elif num < 0:
    return "negativo"
  else: 
    return "cero"
num = float(input("Ingresa un número: "))
print("El número es:", verificar_signo(num))
# 2. Ejercicio: Dado un número, imprime si es par o impar.
num = 4
if num % 2 == 0: print(num, "es par.")
# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
num1 = 3
num2 = 7
num3 = -2
if num1 > num2 and num1 > num3: print(num1, 'es el mayor')
else:
    if num2 > num1 and num2 > num3: print(num2, 'es el mayor')
    else: print (num3, 'es el mayor')
# tipo lista tmb
a, b, c = 5, 7, 2
mayor = max(a, b, c)
print(mayor)
