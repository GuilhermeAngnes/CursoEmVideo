import random
import math

num = random.randint(1, 10)

raiz = math.sqrt(num)

result = ('Raiz de {} é {}'.format(num, math.ceil(raiz)))

print(result)