user_sen = input('Введите предложение: ').split()
a = 0
for word in user_sen:
    a = a + 1
    print(a, word[0:11])