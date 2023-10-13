#Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.

def verify_num_perfect(num):
  return num == sum(divisor for divisor in range(1, num) if num % divisor == 0)
# aqui lo que hacemos es que devuelva num mientras num sea = a la suma de variable para variamble en un rango entre 1 y num si num modulo variable = 0, en otras palabras creamos un bucle para que pruebe a dividir un numero entre 1 y todos los numeros hasta llegar al numero especificado  y los que no den decimal los sume, si la suma da el mismo num que lo devuelva
print(verify_num_perfect(28))