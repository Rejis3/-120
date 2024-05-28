a, s, p = 1, 150, 200
while a<=10:
 a+= 2
 p+= a
 s+= p
print("Конец алгоритма!")
print(f'Переменна s = {s}')


s = 1
for n in range (1, 6):
    s *= n
print('Конец')

print(f"...")


m, n = 12,5
while m!= n:
 if m>n:
    m -= 2*n
 else:
    n -= 3
    print(f"m:{m}xnn:{n}")


c, d = 750, 90
while d > 0:
    d = d - 10
    c = c/2 + 50
    print("Конец алгоритма")
    print(f'Переменная с = {c}')
