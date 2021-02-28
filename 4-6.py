from itertools import cycle, count

start = int(input('Введите начальное число: '))
stop = start * 2 + 10 + 1

for el in count(start):
    if el < stop:
        print(el)
    else:
        break
del el

my_list = [el for el in range(stop)]
count = 0
for b in cycle(my_list):
    if count < stop + 10:
        print(b)
        count += 1
    else:
        break