def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >=3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3

print(my_func(arg_1 = int(input('Введите первый аргумент: ')), arg_2 = int(input('Введите второй аргумент: ')), arg_3 = int(input('Введите третий аргумент: '))))