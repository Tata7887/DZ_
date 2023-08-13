'''
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче
выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''

import random

n = 8
x = []
y = []
for i in range(n):
    new_x = random.randint(1, 8)
    new_y = random.randint(1, 8)
    x.append(new_x)
    y.append(new_y)
print(x, y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')
