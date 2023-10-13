#7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.

def area_triangulo(b, a):
  return (b * a) / 2
b = float(input("Ingrese la base: ")) 
a = float(input("Ingrese la altura: "))
print('el area es:', area_triangulo(b, a))