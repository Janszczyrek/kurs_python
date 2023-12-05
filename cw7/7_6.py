from itertools import cycle
import random

iterator1 = cycle('01')
iterator2 = iter(lambda:random.choice(['N','E','S','W']),-1)
iterator3 = cycle(range(1,8))

