def res(arg_1, arg_2):

    try:
        res = arg_1 / arg_2
        return res
    except ValueError:
        return 'value error'
    except  ZeroDivisionError:
        return 'error! you cant use zero as a divider'

print(res(arg_1 = int(input('Введите первое число: ')), arg_2 = int(input('Введите первое число: '))))