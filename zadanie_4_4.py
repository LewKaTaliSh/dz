list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_2 =[]
a = [int(i) for i in list_1]
for i in a:
   if a.count(i) == 1:
       list_2.append(i)
print(list_2)