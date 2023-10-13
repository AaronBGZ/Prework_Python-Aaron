#Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
def tabla_de_multiplicar(num):
  return {i: num * i for i in range(1,11)}
print(tabla_de_multiplicar(4))

'''
! { y } indican que estamos creando un diccionario en Python.
! i es la variable que se utiliza para representar cada número del 1 al 10 en el rango.
! : se utiliza para separar la clave del valor en cada par clave-valor del diccionario.
! numero * i calcula el valor correspondiente a cada clave. Aquí, numero es el argumento que se pasa a la función tabla_de_multiplicar, y i es un número del rango del 1 al 10. El resultado de esta multiplicación es el valor asociado a cada clave.

!!! Entonces, en resumen, esta primera parte {i: numero * i} se utiliza para crear pares clave-valor en el diccionario, donde las claves son números del 1 al 10 y los valores son el resultado de multiplicar el número pasado como argumento (numero) por cada número en ese rango.
'''