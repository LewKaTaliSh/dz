user_input_1 = input(f"Введите числа:").split()
num_list = [int(i) for i in user_input_1]
result_1 = (sum(num_list))
print(result_1)
user_input_2 = 0
while user_input_2 != "да":
        user_input_2 = input(f"Вы хотите закончить:")
        if user_input_2 == "да":
            break
        else:
                user_input_3 = input(f"Введите числа:").split()
                num_list_1 = [int(i) for i in user_input_3]
                result_2 = (sum(num_list_1))
                result = result_1 + result_2
                print(result)
                result_1 = result


