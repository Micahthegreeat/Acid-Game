import random
num = '123450'
f = open('test2.txt', 'w')
list = []
for x in range(0, 576):
    list.append(random.choice(num))
for line in list:
    f.write(line + '\n')
f.close