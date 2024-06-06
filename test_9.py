#структруирование кода
list_ = [1, 2, 3, 4, 5]
a = list_[len(list_) // 3]

for b in range(len(list_)):
    if list_[b] < a:
        a = list_[b]
print(a)

def min_(list_):
    a = list_[len(list_) // 3]

for b in range(len(list_)):
    if list_[b] < a:
        a = list_[b]

return a

list_ = [1, 2, 3, 4, 5]
min_(list_)

#задача1
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

min_1 = list_1[0]
for value in list_1:
    if value < min_1:
        min_1 = value

min_2 = list_2[0]
for value in list_2:
    if value < min_2:
        min_2 = value

result = min_1 + min_2
result


def min_(list_):
    min_value = list_[0]
for value in list_:
    if value < min_value:
        min_value = value

    return min_value

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
result = min_(list_1) + min_(list_2)
result

#функции возвращающие значения
def return_hello_world():
    return "Hello World" + "!!!"

return_value = return_hello_world()
print(return_value)
