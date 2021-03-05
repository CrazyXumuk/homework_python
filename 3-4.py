def my_func(x,y):
    if y == 0:
        return 1
    return x*(my_func(x, y+1))

print(1/my_func(x = int(input('Введите любое положительное число: ')), y = int(input('Введите любое отрицательное число: '))))
