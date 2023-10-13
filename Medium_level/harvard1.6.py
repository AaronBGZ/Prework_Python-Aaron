def main():
  print_colum(3)

def print_colum(height):
#  for _ in range(height):
#    print("#")
# o directamente
  print("#\n" * height, end="")

main()
###############################
def main():
  print_row(4)

def print_row(width):
  print("?" * width)

main()
###############################
def main():
  print_square(3)

def print_square(size):
  for i in range(size): #for each row in square
    for j in range(size): #for each brick in row
      print("#", end="") #print brick
    print()

main()
#resultado
 ###
 ###
 ###
#otra forma:
def main():
  print_square(3)
def print_square(size):
  for i in range(size):
    print("#" * size)
    print()