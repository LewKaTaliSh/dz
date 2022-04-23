user_input_1 = input(f"Введите слова:").split()
def int_func_1(user_input_1):
    user_map_1 = [str.capitalize(i) for i in user_input_1]
    return user_map_1
print(int_func(user_input_1))
user_input_2 = input(f"Введите слова:").split()
def int_func_2(user_input_2):
    user_map_2 = [str.capitalize(i) for i in user_input_2]
    return user_map_2
res = int_func_1(user_input_1) + int_func_2(user_input_2)
print(res)