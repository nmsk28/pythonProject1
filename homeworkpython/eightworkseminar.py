'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
 Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
'''

from csv import reader, DictReader
from os.path import exists


def creating():
    file = 'phone.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия,Имя,Номер\n')


def writing_csv(info):
    file = 'phone.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n')


def reading_csv(file):
    # возвращает данные в виде строки
    # with open(file, encoding='utf-8') as data:
    # content = data.read()
    # return content

    # возвращает данные в виде списка
    with open(file, encoding='utf-8') as data:
        res = list(reader(data))
    return res

    # with open(file, encoding='utf-8') as data:
    #     res = list(DictReader(data))
    # return res


def get_info():
    info = []
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    info.append(last_name)
    info.append(first_name)
    phone_number = ''
    flag = False
    while not flag:
        try:
            phone_number = input("Введите номер: ")
            if len(phone_number) != 11:
                print("В номере должно быть 11 цифр")
            else:
                phone_number = int(phone_number)
                flag = True

        except:
            print("В номере должны быть только цифры")

    info.append(phone_number)
    return info

# Добавлена возможность удаления данных
def delete_info():
    file = reading_csv('phone.csv')
    last_name = ''.join(list(input("Введите фамилию: ")))
    first_name = ''.join(list(input("Введите имя: ")))
    phone_number = ''.join(list(input("Введите номер: ")))
    info_delete = []
    info_delete.append(last_name)
    info_delete.append(first_name)
    info_delete.append(phone_number)
    index = 0
    for item in file:
        if (item == info_delete):
            print('Абонент найден: %d' % index)
            break
        index += 1
    delete_by_index(index)


def delete_by_index(index):
    print('Удаляем абонента по индексу %d' % index)
    with open('phone.csv', encoding='utf-8') as filedata:
        inputFilelines = filedata.readlines()
        lineindex = 0

        with open('phone.csv', encoding='utf-8', mode='w') as filedata:
            for textline in inputFilelines:
                if lineindex != index:
                    filedata.write(textline)
                lineindex += 1
    filedata.close()

#Добавлена возможность изменения данных
def change_info():
    delete_info()
    record_info()
    print('Абонент заменен')


def record_info():
    info = get_info()
    writing_csv(info)


# record_info()


def view():
    print(reading_csv('phone.csv'))


# view()


def main():
    while True:
        step = input("Введите действие: ")
        if step == 'q':
            break
        elif step == 'w':
            path = 'phone.csv'
            flag = exists(path)
            if not flag:
                creating()
                record_info()
            else:
                record_info()
        elif step == 'd':
            delete_info()
        elif step == 'c':
            change_info()
        elif step == 'r':
            view()


main()