import math

a = 7
b = 5
c = 0

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('A equação não há raíz real.')
elif delta == 0:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    print(f'A equação tem apenas uma raíz real x1 = {x1}')
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    print(f'A equação possui duas raizes reais x1 = {x1} e x2 = {x2}')
