
def my_func(var_1, var_2, var_3):
    if var_1 > var_2:
        if var_2 > var_3:
            print(var_1 + var_2)
        else:
            print(var_1 + var_3)
    else:
        if var_1 > var_3:
            print(var_2 + var_1)
        else:
            print(var_2 + var_3)
my_func(int(input('Введите число номер 1: ')), int(input('Введите число номер 2: ')), int(input('Введите число номер 3: ')))
var_1 = int(input('Введите число номер 1: '))
var_2 = int(input('Введите число номер 2: '))
var_3 = int(input('Введите число номер 3: '))

