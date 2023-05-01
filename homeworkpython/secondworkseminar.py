n = int(input('Введите количество монет: '))
c_o = 0
c_o = int(input('Введите количество монет "орлом"'))
if c_o < n - c_o :
    print('Перевернуть "орлов"', c_o)
elif c_o > n - c_o:
    print('Перевернуть "решек"',n - c_o)
else:
    print('Перевернуть монет', n//2)


s = int(input())
p = int(input())
found = False
for x in range(s):
    for y in range(p):
        if s == x + y \
                and p == x * y \
                and x <= 1000 \
                and y <= 1000:
            print(x, y)
            found = True
if not(found):
    print('Такой пары чисел не существует')


N = int(input())
i = 0
while 2 ** i <= N:
    print(2 ** i)
    i += 1
