user_input_1 = int(input(f"Сколько кортежей создать(число):"))
a = 0
user_list_1 = []
user_dict_1 = {"название" : [],
               "цена" : [],
               "количество" : [],
               "ед" : []}
while a != user_input_1:
    user_input_2 = input(f"Введите название {a + 1}:")
    user_input_3 = input(f"цена {a + 1}:")
    user_input_4 = input(f"количество {a + 1}:")
    user_input_5 = input(f"ед {a + 1}:")
    user_list_1.append((a+1, {"название" : user_input_2,
                       "цена" : user_input_3,
                       "количество" : user_input_4,
                       "ед" : user_input_5}))
    a += 1
    for key, values in enumerate(user_list_1):
        key_list = ['название', 'цена', 'количество', 'ед']
        dd = dict.fromkeys(key_list, [values])
        print(dd)


