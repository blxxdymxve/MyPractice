import shutil
total, used, free = shutil.disk_usage("/")
if ((free // (2**30)) * 1024 > 1):
    i = 0
    while i < 10000:
        file = open('test.txt', 'a')
        a = str(i)
        a = a + " "
        file.write(a)
        i = i + 1
else:
    print("Места на диске мало")