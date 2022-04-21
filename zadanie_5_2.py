list_1 = [7, 5, 3, 3, 2]
a = int(input('Введите число: '))
for i, el in enumerate(list_1):
    if a >= el:
        b = list_1.insert(i, a)
        print(list_1)
        break