import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name) #r = rules
# := asign a value from left to right and ask a boolean question (if)
  name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")