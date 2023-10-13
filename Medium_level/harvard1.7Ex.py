#try and except para anticiparse a errores que puedan introducir los usuarios
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
  while True: #para hacer un bucle infinito 
    try:
      x = int(input("What's x? "))
      #print(f"x is {x}")
    except ValueError: 
    #solo si la exepcion se cumple hara el siguiente print
      pass #print("x is not an integer")
    else:
      return x #return es mas fuerte que break asi que sirve 

main()
# en vez de usar excepciones del propio python con exept puedes usar "raice" para crear propias excepciones