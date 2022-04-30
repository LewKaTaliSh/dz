stroka = 0
f = open('test.txt', 'r')
for i in f:
    stroka += 1
print(stroka)
f = open('test.txt', 'r')
data = f.read()
slova = data.split()
print(len(slova))

