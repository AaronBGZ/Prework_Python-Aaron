'''
re.sub 
pattern(normal usando regular expressions),
repl(lo que queremos remplazar)
string(variable que yo defina de antemano), 
count0
flags=0()
'''
import re

url = input("URL: ").strip()
#username = url.removeprefix("^(https?://)?(www\.)?twitter\.com/", "", url)
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
#ponemos \ antes del . paraaceptar el punto
#(?:----) si estoy usando parentesis para agrupar todo junto pero no, no necesitas capturarlo como grupo 1, basicamente () es un grupo y a la hora de llamar con martches.group, va en orden y el primer parentesis en el pattern es 1, el segundo es 2, etc.
  print(f"Username:", matches.group(1)) 
#ponemos 2 prq hemos puesto 2 parentesis el primero con el www es 1 y el segundo con el = es 2
