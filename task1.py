'''Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
*Попробуйте решить уравнения с другими значениями a, b, c.
'''

from math import sqrt

# a = 5
# b = -10
# c = -400

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + sqrt(d) / (2 * a))
    x2 = (-b - sqrt(d) / (2 * a))
    print(f'x1 = {x1}; x2 = {x2}')
elif d == 0:
    x1 = -b / (2 * a)
    print(f'x1 = {x1}')
else:
    print('Нет корней')
