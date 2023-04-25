'''
Задание 1.
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
'''

name = 'Maxim'
password_m = 'klmn'
age_m = 22
print(name)
print(password_m)
print(int(age_m))

a = input('Введите Ваше имя:')
b = input('Введите Ваш пароль:')
c = int(input('Введите Ваш возраст:'))

print('Ваши данные для входа в аккаунт:' +'имя - ' + a + ', ' + 'пароль -' + b +', ' + 'возраст - ' + str(c))

'''
Задание 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
'''
time_sec = float(input('Введите время в секундах:' ))
h = round((time_sec/360),0)
min = round((time_sec/60),0)

print('Время в формате ч: м: с -', str(f"{h}:{min}:{int(time_sec)}"))

'''
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
'''
n = int(input('Введите целое положительное число:' ))
sum_n = n + (10*n + n) + (100*n + 10*n +n)
print(sum_n)

'''
Задание 4.
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
'''

company_revenue = int(input('Введите выручку фирмы:' ))
company_costs = int(input('Введите издержки фирмы:' ))
fin_results = company_revenue - company_costs
return_revenue = round((fin_results/company_revenue),2)
if fin_results>0:
    print('Прибыль:','Ее величина:', fin_results)
    print("Рентабельность выручки:",return_revenue)
    number_employees = int(input('Введите численность сотрудников:'))
    fin_results_empl = round((fin_results/number_employees),2)
    print('Прибыль фирмы в расчете на одного сотрудника:',fin_results_empl)
elif fin_results<0:
    print('Убытки')
else:
    print('Нет прибыли')

'''
    ДОПОЛНИТЕЛЬНЫЕ:
Задача 2: Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''
# Вариант 1
n = int(input('Введите трехзначное число:' ))
n_1 = n//100
n_2 = (n - n_1*100)//10
n_3 = n - n_1*100 - n_2*10
sum_n = n_1 + n_2 + n_3
print(sum_n)

# Вариант 2
n = input('Введите трехзначное число:' )
n_1 = int(n[0])
n_2 = int(n[1])
n_3 = int(n[2])
sum_n = n_1 + n_2 + n_3
print(sum_n)
'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов./
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое/
количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
'''
s = int(input('Введите число:' ))
n = s/(1+1+2*(1+1))
if s%n == 0:
    print('Петя сделал:',n,'Катя сделала:',2*2*n, 'Сережа сделал:',n )
else:
    print('Введите правильное число:')

'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – 
счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
счастливость билета.
Пример:
385916 -> yes
123456 -> no
'''
s = input('Введите шестизначное число:' )
s_1 = int(s[0])
s_2 = int(s[1])
s_3 = int(s[2])
s_4 = int(s[3])
s_5 = int(s[4])
s_6 = int(s[5])
sum_1 = s_1 + s_2 + s_3
sum_2 = s_4 + s_5 + s_6
if sum_1 == sum_2:
    print('yes - happy ticket')
else:
    print('no - change transport')

'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на
 два прямоугольника).
Пример:
3 2 4 -> yes
3 2 1 -> no
'''
n = int(input('Введите число:' ))
m = int(input('Введите число:' ))
k = int(input('Введите число:' ))
if k%n == 0 or k%m == 0 :
    print('Можно разломить шоколадку')
else:
    print('Не так ломаешь')
