#COMMAND-LINE ARGUMENTS
import sys
'''
try:
  print("hello, my name is", sys.argv[1])
except IndexError:
  print("Too few arguments")
'''
'''
if len(sys.argv) < 2:
  sys.exit("Too few arguments")
elif len(sys.argv) > 2:
  sys.exit("Too many arguments")
else:
  #print name tags
  print("hello, my name is", sys.argv[1])
'''
if len(sys.argv) < 2:
  sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    #slices, start from element 1 and until the end  ":"
  print("hello, my name is", arg)
