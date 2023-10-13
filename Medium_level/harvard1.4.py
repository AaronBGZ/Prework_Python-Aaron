#LOOPS
  #while
i = 0
while i < 3:
  print("meow")
  i += 1
#################################
  #for para listas
for _ in range(3): #[0,1,2]: 
  print("meow")
  # _ se usa para crear una variable a la que no le daremos mas uso
#################################
  #otra opcion
  print("meow\n" * 3, end="") #\n para que cabie de linia cada vez, end para que no se añada un espacio blanco al final
#################################
while True:
  n = int(input("What's n? "))
  if n > 0:
    break #se usa para salir de un loop infinito

for _ in range(n):
  print("meow")
#################################
def main():
  number = get_number()
  meow(number)

def get_number():
  while True:
    n = int(input("What's n? "))
    if n > 0:
      return n

def meow(n):
  for _ in range(n):
    print("meow")

main()
#######################################
students = ["Hermione", "Harry", "Ron"]
#print(students[0]) #0 indica el primer termino de la lista
for i in range(len(students)):
  print(i + 1, students[i])

