import csv

students = []
with open("students.csv") as file:
  # for line in file:
  #   name, house = line.rstrip().split(",")
  #   student = {"name": name, "house": house}
  #   students.append(student)
  reader = csv.DictReader(file)
  for row in reader:
    students.append({"name": row["name"], "house": row["home"]})

#def get_name(student):
#  return student["name"]
#for student in sorted(students, key=get_name):
#estas 3 linias son declarar una funcion y usarla, si solo la usamos una vez es las facil asignar una funcion sin nombre y decir que hacer:
for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is in {student['house']}")