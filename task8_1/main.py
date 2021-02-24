a = open('text.txt', 'r', encoding='utf8').readline()
a = str(a)[:2]
try:
    a = int(a)
    if a % 2 == 0:
        with open('even.txt', 'a') as file:
            file.write(str(a))
    else:
        with open('odd.txt', 'a') as file:
            file.write(str(a))
except ValueError:
    print("Первые 2 символа строки не являются цифрами")