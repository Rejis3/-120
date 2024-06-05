#set; create
a = {}
b = set()
c = frozenset()

a = {1, 11, 'a', (1, 1.1), None, True, print}
a = {1, 1.1< [1, 2]}

#create
a = frozenset({1, 1.1})

a = [1, 'abc', 1]
set(a)
b = set('слово')
c = frozenset('hello')
d = set([1, [2.1], 1])

#retrive, update, delete

a = {1, 1.1, 'a'}
a.add('привет')
b = 1
a.add(b)

a = {1, 2, 3}
a.update({5, 2})

a = {1, 1.1, 'a'}
a[0]

a = {1, 1.1, 'a'}
a[0] = 'a'
a = {1, 2, 3}

a = {1, 1.1, 'a'}
del a[0]
del a


a = {1, 2, 3}
a.clear()
a = {1, 2, 3, 4}
a.pop()
a.remove(3)
a.discard(5)

a = {1, 2, 3}
b = {3, 5, 6}
c = a - b
print(c)
a -= b

#множество set

help(set)
a = {1, 2, 3}
a.copy()
a.isdisjoint({4, 5, 6})
a.isdisjoint({4, 3, 1, 2})
a.isdisjoint({2, 1})
a = frozenset({1, 2, 3})
a.copy()

#обращение к методу через "."
a = {'сыр', 'помидор', 'молоко'}
b = {'яблоко', 'хлеб', 'молоко'}
a.intersection(b)
a.intersection_update(b)

a = {'сыр', 'помидор', 'молоко'}
b = {'яблоко', 'хлеб', 'молоко'}
a.union(b)
a.union_update(b)

a = {'сыр', 'помидор', 'молоко'}
b = {'яблоко', 'хлеб', 'молоко'}
a.difference(b)
a.difference_update(b)

a = {'сыр', 'помидор', 'молоко'}
b = {'яблоко', 'хлеб', 'молоко'}
a.symmetric_difference(b)
a.symmetric_difference_update(b)

a = {'сыр', 'помидор', 'молоко'}
b = {'яблоко', 'хлеб', 'молоко'}
a_b = a.intersection(b)
a_b_c = a_b.intersection(c)
a.intersection(b).intersection(c)
c.difference(b).difference(a)
c.difference(b.union(a))
