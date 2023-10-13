#Conditionals (>, <, <=, >=, ==, !=)
x = int(input("what's x? "))
y = int(input("what's y? "))

#if x < y or x > y: no esta mal pero podemos simplificar
if x != y:
  print("x is not equal to y")
else:
  print("x is equal yo y")

# match, instead of using if, elif, elif..., else, si queremos asocias cosas a cosas podeos usar match

match name:
    case"Harry" | "Hermione" | "Ron"：
      print("Gryffindor")
    case "Draco":
      print("Slytherin")
    case _:
      print("Who?")

