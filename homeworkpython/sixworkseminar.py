'''
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
# '''
a = int(input('Введите первый элемент массива:  '))
d = int(input('Введите разность елементов массива:  '))
n = int(input('Введите количество элементов  массива:  '))
a_mass = []
for i in range(n):
    a_mass.append(a + i*d)
print(a_mass)

'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
'''
n = int(input('Введите количество элементов массива:  '))
a_mass = input('Введите через пробел элементы массива: ').split()
new_mass = list(map(int, a_mass))
m_min = int(input('Введите первый элемент диапозона: '))
m_max = int(input('Введите последний элемент диапозона: '))
for i in range(len(new_mass)):
    if new_mass[i] <= m_max and m_min <= new_mass[i]:
        print( i , end=' ' )