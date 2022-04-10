user_input_1 = input('Ваше имя: ')
user_input_2 = input('Фамилия: ')
user_input_3 = input('Год рождения: ')
user_input_4 = input('Город проживания : ')
user_input_5 = input('email: ')
user_input_6 = input('Номер для связи: ')
def my_func(name, surname, date, sity, email, tel):
    stroka = name + ' ' + surname + ' ' + date + ' ' + sity + ' ' + email + ' ' + tel
    print(stroka)
my_func(name = user_input_1, surname = user_input_2, date = user_input_3, sity = user_input_4, email = user_input_5, tel = user_input_6)


