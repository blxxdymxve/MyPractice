<<<<<<< Updated upstream
from random import randint
from termcolor import cprint

x = int(input("Введите начало промежутка: "))
y = int(input("Введите конец промежутка: "))
array = [randint(x, y) for i in range(10)]
print("Массив до выполнения задания: ", array)

temp = []
for i, value in enumerate(array):
    if array[i] % 2 == 0:
        temp.append(array[i])

temp = temp[::-1]

for i, value in enumerate(array):
    if array[i] % 2 == 0:
        array[i] = temp.pop(0)

print("Массив после выполнения задания:")
for i in range(10):
    if array[i] % 2 == 0:
        cprint(array[i], 'green')
    else:
        print(array[i])
=======
from random import randint
from termcolor import cprint

x = int(input("Введите начало промежутка: "))
y = int(input("Введите конец промежутка: "))
array = [randint(x, y) for i in range(10)]
print("Массив до выполнения задания: ", array)

temp = []
for i, value in enumerate(array):
    if array[i] % 2 == 0:
        temp.append(array[i])

temp = temp[::-1]

for i, value in enumerate(array):
    if array[i] % 2 == 0:
        array[i] = temp.pop(0)

print("Массив после выполнения задания:")
for i in range(10):
    if array[i] % 2 == 0:
        cprint(array[i], 'green')
    else:
        print(array[i])
>>>>>>> Stashed changes
