import random

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num): continue
        line = aline
    print(line)

random_line(open('text.txt', encoding='utf8'))
'one\n'
while True:
    if input():
        random_line(open('text.txt', encoding='utf8'))
        'one\n'