#4. Dada una lista de números, crea una función que devuelva el número máximo de la lista.

# def encontrar_maximo(lista):
#   maximo = lista[0]

#   for numero in lista:
#     if numero > maximo:
#       maximo = numero 
#     return maximo 
# numeros = [5, 12, 3, 8, 9]
# print("El número máximo es:", encontrar_maximo(numeros))


# lista = [3,6,8,2,6]
# def maximo(lista):
#   maximo = lista[0];
#   for x in lista:
#       if x > maximo:
#           maximo = x
#   return maximo
# print(maximo)


numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]

max_value = 0

for num in numbers:
    if (max_value == 0 or num > max_value):
        max_value = num

print('Maximum value:', max_value)
