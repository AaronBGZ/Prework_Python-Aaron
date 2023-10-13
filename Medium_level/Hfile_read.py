#####with open("names.txt", "r") as file:
'''
  lines = file.readlines() # read and return in form of a list in a variable names lines
for line in lines:
  print("hello,", line, line.rstrip()) # se usa para quitar lineas en blanco entre lines, se puede usar tambien end=""
'''
'''
for line in file:
  print("hello,", line.rstrip())
'''
''
names = []
with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())
for name in sorted(names):
  print(f"hello, {name}")
'''
with open("names.txt") as file:
  for line in sorted(file):
    print("hello,", line.rstrip())
'''