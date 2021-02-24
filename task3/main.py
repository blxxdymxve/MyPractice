from random import randint

x = int(input("Введите начало промежутка: "))
y = int(input("Введите конец промежутка: "))

array = [randint(x, y) for elem in range(10)]
array_plus = []
array_minus = []

for elem in array:
    if elem > 0:
        array_plus.append(elem)
    elif elem < 0:
        array_minus.append(elem)
    else:
        pass

print("Исходный массив: ", array)
print("Положительный массив: ", array_plus)
print("Отрицательный массив: ", array_minus)