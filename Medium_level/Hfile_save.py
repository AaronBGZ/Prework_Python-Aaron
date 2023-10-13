#input and output of files 
#(open, file, .append, .write, with _ as)
'''
names = []
for _ in range(3):
  names.append(input ("What's your name? "))
#append para añadir a la lista
for name in sorted(names):
  print(f"hello, {name}")
'''
#simplificacion:
name = input("What's your name? ")
#file = open("names.txt", "a")
with open("names.txt", "a") as file:
file.write(f"{name}\n")
#file.close()