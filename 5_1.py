from collections import namedtuple
from statistics import mean

company = namedtuple('company', 'name profit avg')

company_list = []
for i in range(int(input('Количество компаний: '))):
    arg = input('Введите имя и поквартальную прибыль компании через '
                'пробел:\n').split()
    company_list.append(company(arg[0], arg[1:], mean(map(int, arg[1:5]))))

avg = mean([i.avg for i in company_list])

for i in company_list:
    print(f'Компания: {i.name} - Средняя прибыль за год: {i.avg}')

print('*' * 50)

print('Предприятия, чья прибыль ниже среднего:')
for i in company_list:
    if i.avg < avg:
        print(i.name)

print('Предприятия, чья прибыль выше среднего:')
for i in company_list:
    if i.avg > avg:
        print(i.name)
