#REGULAR EXPRESSIONS
'''
re.search(
pattern(normal usando regular expressions),
string(variable que yo defina de antemano), 
flags=0()
)
flags: re.IGNORECASE|re.MULTILINE|re.DOTALL

. any character (except a new line)
.* 0 or more repetitions
.+ 1 or more repetitions
? 0 or 1 repetition
{m} m repetition
{m,n} m-n repetitions
^ match the start of the string
$ match the end of the string
[] set of characters (todo lo que haya dentro es lo que queremos aceptar)
[^] completing the set (todo lo que aya dentro pasado ^ es lo que queremos excluir)
\d decimal digit
\D not decimal digit
\s white space characters
\S not white space characters
\w word character [a-zA-Z0-9_]
\W not word character
A|B either A or B
(...) a group
(?:...) non-capturing version, no tomarlo como grupo
'''
#validating email adress 
import re

email = input("What's your email? ").strip()
#[a-zA-Z0-9_] = \w
if re.search(r"^(\w|\.)+@(\w\.)?\w+\.(edu|com|es)$", email, ):
  #(...)? todo lo que haya entre parentesis, puede estar o no estar, opcional
  print("Valid")
else:
  print("Invalid")
