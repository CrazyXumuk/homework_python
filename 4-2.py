my_list = [int(el) for el in input('Введите случайные числа через пробел: ').split()]
for el in range(1, len(my_list)):
    if my_list[el] > my_list[el - 1]:
        print(my_list[el])