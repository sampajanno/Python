import random
import string


a = input('input string')
find_x = a.find('x')
find_w = a.find('w')
if find_x >= 0 and 0 <= find_w < find_x:
    print('w occurs earlier')
elif 0 <= find_x < find_w and find_w >= 0:
    print('x occurs earlier')
if not ('x' in a) and not ('w' in a):
    print('no w or x')
elif not ('x' in a):
    print('no x')
elif not ('w' in a):
    print('no w')

# 2
a = input()
a = list(a)
for i in range(len(a)):
    if i % 2 == 1:
        if a[i] != 'a':
            a[i] = 'a'
    elif a[i] == 'a':
        a[i] = 'b'
a = ''.join(a)
print(a)

# 3
a = input()
count = 0
for i in range(len(a)):
    if a[i].isdigit():
        count = count + int(a[i])
print(count)

# 4
a = input()
a = a.replace('!', '')
print(a)

# 5
a = int(input('input list length'))
list1 = list()
for i in range(a):
    if i % 2 == 0:
        list1.append(0)
    else:
        list1.append(1)
print(list1)

# 6
a = [1, 5, 7, 7, 8165, 6235, 72308, 524347, 626, 7262, 525, 2]
count = 0
for i in range(len(a)):
    if i % 2 == 1:
        count = count + a[i]
print(count)

# 7
a = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
max_number = 0
previous = 0
etal = 0
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count = count + 1
    if previous < count:
        previous = count
        etal = a[i]
print(f'element {etal} occurs {previous} times')

# 8
list1 = input('input numbers list with spaces').split()
list1 = list(map(int, list1))
max_ind = list1.index(max(list1))
max_c = max(list1)
min_ind = list1.index(min(list1))
min_c = min(list1)
list1[max_ind] = min_c
list1[min_ind] = max_c
print(list1)

# 9
list1 = input('input list elements with spaces').split()
index_start = 0
index_fin = 5
count = 0
if len(list1) % 5 == 0:
    cicle = len(list1) // 5
else:
    cicle = len(list1) // 5 + 1
for i in range(cicle):
    if count == 0:
        print(list1[index_start:index_fin])
        count = count + 1
    else:
        print(list1[index_fin - 1:index_start - 1:-1])
        count = count - 1
        index_start = index_fin
        index_fin = index_fin + 5

# 10


list1 = list()
for i in range(20):
    a = random.randint(0, 100)
    list1.append(a)
list2 = list()
for j in list1:
    if 35 < j < 65:
        list2.append(j)
    del list1[list1.index(j)]
print(list1)
print(list2)

# 11
list1 = list(map(int, input('input even numbers with spaces').split()))
for i in range(len(list1)):
    if list1[i] < 0:
        list1[i] = -1
    elif list1[i] > 0:
        list1[i] = 1
print(list1)

# 12
list1 = list(map(int, input('input even numbers').split()))
ind = int(input('input number index'))
if 0 <= ind < len(list1):
    print(f'number with index {ind} is equal to {list1[ind]}')
else:
    print('no number with such index')

# 13
list1 = list(map(int, input('input even numbers').split()))
set1 = set(list1)
list2 = list(set1)
for i in range(len(list2)):
    n = list1.count(list2[i])
    if n > 1:
        print(f'number {list2[i]} at {i} position in array repeats {n} times ')
print(set1)

# 14
tuple1 = tuple(map(int, input('input even numbers separated by spaces').split()))
for i in tuple1:
    if tuple1.count(i) == 1:
        print(i)

# 15
tuple1 = tuple(map(int, input('input even numbers separated by spaces').split()))
i = 0
j = 0
while i < len(tuple1):
    print(tuple1[i:i + j + 1])
    j = j + 1
    i = i + j

# 16
tuple1 = tuple(map(int, input('input 4-digit numbers separated by spaces').split()))
list1 = list(tuple1)
list2 = list()
for i in list1:
    element = list(map(int, str(i)))
    a = element.index(max(element))
    b = element.index(min(element))
    element[a], element[b] = element[b], element[a]
    element = int(''.join(map(str, element)))
    list2.append(element)
tuple2 = tuple(list2)
print(tuple2)

# 17


n = int(input('input cortege length >5'))
if n < 5:
    n = int(input('it should be greater than 5'))
else:
    list1 = list()
    for i in range(n):
        a = random.randint(0, 100)
        list1.append(a)
        tuple1 = tuple(list1)
a, *b, c = tuple1
print(a)
print(b)
print(c)

# 18


str1 = ''
for i in range(25):
    a = string.ascii_letters
    b = random.choice(a)
    str1 = str1 + b
print('string -', str1)
frozenset1 = frozenset(str1)
print('array -', frozenset1)

# 19
n = int(input('input cortege length'))
list1 = list()
for i in range(n):
    if i == 0 or i == n - 1:
        list1.append(1)
    else:
        list1.append(0)
tuple1 = tuple(list1)
print(tuple1)

# 20

dict1 = dict()
n = int(input('input the amount of login-password pairs you wish to get'))
for i in range(n):
    len_login = random.randint(6, 20)
    len_password = random.randint(6, 20)
    login = ''
    password = ''
    for j in range(len_login):
        login = login + str(random.randint(0, 9))
    for k in range(len_password):
        password = password + str(random.randint(0, 9))
    print(f'login {i + 1} - {login}, password {i + 1} - {password}')
    dict1[login] = password
