with open('test.txt','r', encoding = 'utf-8') as file:
    list_1 = []
    my_file = file.read().split('\n')
    for line in my_file:
        line = line.split()
        if float(line[1]) < 20000:
            list_1.append(line[1])
            print(list_1)
