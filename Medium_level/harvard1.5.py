#diccionarios DICT (keys --> values)
#students = ["Hermione","Harry","Ron","Draco"]
#houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]
students = {
  "Hermione": "Gryffindor",# first key after value.
  "Harry": "Gryffindor",
  "Ron": "Gryffindor",
  "Draco": "Slytherin"
}

for student in students:
  print(student, students[student], sep=", ")
  #asi se expresa el value

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
for student in students:
  print(student["name"], student["house"], student["patronus"], sep=", ")