#USANDO LA LIBRERIA CREADA EN 2.2
import sys
from temporal import hello

if len(sys.argv) == 2:
  hello(sys.argv[1])