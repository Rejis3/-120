#1
a, s, p = 1, 150, 200
while a <=10:
 a += 2
 p += a
 s += p
print("Конец алгоритма!")
print(f'Переменна s = {s}')


#2
s = 1
for n in range (1, 6):
    s *= n
print('Конец')

print(f"...")


#3
m, n = 12,5
while m != n:
 if m > n:
    m -= 2*n
 else:
    n -= 3
print(f"m:{m}xnn:{n}")


#4
c, d = 750, 90
while d > 0:
    d = d - 10
    c = c/2 + 50
print("Конец алгоритма")
print(f'Переменная с = {c}')


#5
k, l = [], []
for i in range (1, 11):
    k.append(10 -i)
for i in range(1, 11):
    l.appened(k[5] - k[i - 1])
print(k)
print(l)


k, l = list(range(1, 11)), list(range(1, 11))

for i in range(1, 11):
    k[i -1] = 10 - i
for i in range(1, 11):
    l[i - 1] = k[5] - k[i -1]
print(k)
print(l)
print(f'Колличество отрицательных элементов массива l = {len([value for value in l if value < 0])}')

k, l = list(range(1, 11)), list(range(1, 11))

for i in range(1, 11):
    k[i - 1] = 10 - i
for i in range(1, 11):
    l[i - 1] = k[5] - k[i - 1]
print(k)
print(l)
count_k = 0
for value in k:
    if value < 0
        count_k += 1
count_l - 0
for value in l:
    if value < 0:
        count_l += 1
print(f'Количество отрицательных элементов = {count_k + count_l}')
