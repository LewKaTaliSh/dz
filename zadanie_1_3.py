
def my_func(user_num_1, user_num_2):
    if user_num_2 == 0:
        print("Ошибка. На ноль делить нельзя.")
    else:
        return user_num_1 / user_num_2
user_num_1 = int(input('Введите первое число: '))
user_num_2 = int(input('Введите второе число: '))
print('res =', my_func(user_num_1, user_num_2))

