user_input_1 = int(input('Введите значение выручки: '))
user_input_2 = int(input('Введите значение издержек: '))
if user_input_1 > user_input_2:
    a = user_input_1 - user_input_2
    rent = a / user_input_1
    user_input_3 = int(input('Введите количество сотрудников: '))
    b = a / user_input_3
    print ('- прибыль', rent, b)
else:
    print ('- убыток')