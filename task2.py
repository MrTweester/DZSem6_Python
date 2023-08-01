# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
n = int(input("Введите размер массива: "))
list1 = [randint(0,10) for _ in range(n)]
print(list1)
mini = int(input("Введите минимум индексов массива: "))
maxi = int(input("Введите максимум индексов массива: "))
for i in range(len(list1)):
    if mini <= list1[i] and list1[i] <= maxi:
        print(i, end=' ')

# 




