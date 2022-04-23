from functools import reduce
new = [i for i in range(100, 1001, 2)]
a = reduce(lambda a,b: a * b, new)
print(a)