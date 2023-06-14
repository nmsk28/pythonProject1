'''
Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
'''
import pandas as pd

data = pd.read_csv('california_housing_train.csv')

print(data[(0 < data['population']) & (data['population'] < 500)]['median_house_value'])

'''
Задача 42: Узнать какая максимальная households в зоне минимального значения population
'''
print(data[data['population'] == data['population'].min()]['households'].max())
