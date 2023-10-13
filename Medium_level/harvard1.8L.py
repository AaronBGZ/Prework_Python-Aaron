#Libraries / modules RANDOM
#flip a coin 50%
'''
import random
coin = random.choice(["cara", "cruz"])
print(coin)
'''
'''
from random import choice
coin = choice(["cara", "cruz"])
print(coin)
'''
'''
import random
number = random.randint(1,10)
print(number)
'''
import random
cards = ["jack", "Queen", "King"] #lista para desordenar
rando.shuffle(cards) #funcion para desordenar
for card in cards: #para ordenar de 1 en 1
  print(card)
