#Crea una función que, dado un número, verifique si un número es primo.
def num_primo(num): 
  if num <= 1: 
    return False 
  for i in range(2, num): 
    if num % i == 0: 
      return False 
      return True 
num = int(input("Ingresa un número: "))

if num_primo(num): 
  print("Es un número primo.") 
else: 
  print("No es un número primo.")