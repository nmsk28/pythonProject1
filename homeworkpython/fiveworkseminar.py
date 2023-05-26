'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
 и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''
def exponent_numb(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / exponent_numb(a, -b)
    if b % 2 == 0:
        return exponent_numb(a, b // 2) * exponent_numb(a, b // 2)
    else:
        return exponent_numb(a, b - 1) * a

a = int(input('Введите число A:  '))
b = int(input('Введите число B:  '))
print(exponent_numb(a, b))

'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
4 
'''
def sum_numb(a, b):
    if a == 0:
        return b;
    return sum_numb(a - 1, b + 1)

a = int(input('Введите число A:  '))
b = int(input('Введите число B:  '))
print(sum_numb(a, b))


