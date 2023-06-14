'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''
n = int(input('Введите количество элементов первого множества:  '))
m = int(input('Введите количество элементов вторго множества:  '))
mass_1 = input('Введите через пробел n элементов первого множества: ').split()
mass_2 = input('Введите через пробел m элементов иторого множества: ').split()
new_mass = mass_1 + mass_2
new_numb = list(map(int, new_mass))
new_numb.sort()
numbs = set(new_numb)
print(*numbs)


'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены 
только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте
 выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из 
 управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед
некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
'''

n = int( input( 'Введите количество кустов:  ' ) )
lis = [ int(x) for x in input( 'Введите через пробел количество ягод на кустах n: ' ).split() ]
n = len(lis)
lis = lis + lis[:2]
ma = 0
for i in range(n):
    ma = max( ma, lis[i] + lis[i+1] + lis[i+2] )
print(ma)

