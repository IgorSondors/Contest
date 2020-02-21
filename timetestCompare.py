import timeit# сравним различные методы генерации списков и их эффективность
def test1():# конкатенация
    l = []
    for i in range(1000):
        l = l + [i]

def test2():# добавление в конец списка
    l = []
    for i in range(1000):
        l.append(i)

def test3():# генератор списков
    l = [i for i in range(1000)]

def test4():# функция range, обёрнутая в конструктор списка
    l = list(range(1000))
t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")