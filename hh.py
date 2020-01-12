import requests
import pprint
import json
import time

def calculating_average(value, quantity):
    try:
        result = int(value/quantity)
    except ZeroDivisionError:
        result = 0
    return result

def get_and_analitik_skills(params):
    domain='https://api.hh.ru/'
    url=f'{domain}vacancies'
    params['page'] = 0

    dict_skills = {}  # Словарь скилов и количества еге появлений
    qiantity_skill = 0  # Колисество скилов
    salary_min_gross_false = 0  # Минимальная зарплата с вычетом налогов
    count_salary_min_gross_false = 0  # Количество показателей минимальной зарплаты с вычетом налогов
    salary_max_gross_false = 0  # Максимальная зарплата с вычетом налогов
    count_salary_max_gross_false = 0  # Количество показателей максимальной зарплаты с вычетом налогов
    salary_min_gross_true = 0  # Минимальная зарплата без вычетов налогов
    count_salary_min_gross_true = 0  # Количество показателей минимальной зарплаты без  вычетов налогов
    salary_max_gross_true = 0  # Максимальная зарплата без вычетов налогов
    count_salary_max_gross_true = 0  # Количество показателей максимальной зарплаты без вычетов налогов
    x = 1
    result = requests.get(url, params=params).json()
    found = result['found']
    print(f'По запросу {params["text"]} найдеро количество вакансий:  {found}')

    while x <= found and params['page'] <= 99:
        print(f'Страница № {params["page"]}')     #  Тест принт
        result = requests.get(url, params=params).json()
        items = result['items']
        for item in items:
            url_vacansy = item['url']
            result_vacansy = requests.get(url_vacansy, params=params).json()
            salary = result_vacansy['salary']         #  Словарь зарплаты у данной вакансии
            # print(f'salary --> {salary}')    #  Тест принт
            if salary:
                if salary['gross']:
                    if salary['from']:
                        salary_min_gross_true += salary['from']
                        count_salary_min_gross_true += 1
                    if salary['to']:
                        salary_max_gross_true += salary['to']
                        count_salary_max_gross_true += 1
                else:
                    if salary['from']:
                        salary_min_gross_false += salary['from']
                        count_salary_min_gross_false += 1
                    if salary['to']:
                        salary_max_gross_false += salary['to']
                        count_salary_max_gross_false += 1
            key_skills = result_vacansy['key_skills']
            # print(f'Требования по вакансии № {x}')  #  Тест принт
            for skill in key_skills:
                sk = skill['name']
                if sk in dict_skills:
                    dict_skills[sk] += 1
                else:
                    dict_skills[sk] = 1
                    qiantity_skill += 1
            x += 1
        params['page'] += 1

    average_min_salary_gross_false = calculating_average(salary_min_gross_false, count_salary_min_gross_false)  # Средняя минимальная зарплата с вычетом налогов среди вакансий с указанной зп
    average_max_salary_gross_false = calculating_average(salary_max_gross_false, count_salary_max_gross_false)  # Средняя максимальная зарплата с вычетом налогов среди вакансий с указанной зп
    average_salary_gross_false = int((average_max_salary_gross_false + average_min_salary_gross_false) / 2)  # Средняя зарплата с вычетом налогов среди вакансий с указанной зп

    average_min_salary_gross_true = calculating_average(salary_min_gross_true, count_salary_min_gross_true)  # Средняя минимальная зарплата без вычетов налогов среди вакансий с указанной зп
    average_max_salary_gross_true = calculating_average(salary_max_gross_true, count_salary_max_gross_true)  # Средняя максимальная зарплата без вычетов налогов среди вакансий с указанной зп
    average_salary_gross_true = int((average_max_salary_gross_true + average_min_salary_gross_true) / 2)  # Средняя зарплата без вычетов налогов среди вакансий с указанной зп

    list_skills = []
    result = sorted(dict_skills.items(), key=lambda x:x[1], reverse=True)
    print(f'Всего требований:  {qiantity_skill}')
    for element in result:
        element_ = f'{element[0]} в {element[1]} вакансиях из {x} , {element[0]} Требуется в {round(element[1] / x * 100, 2)} % вакансий'
        list_skills.append(element_)
        print(element_)
    print('')
    list_salary = []
    salary_1 = (f'Средняя зарплата с вычетом налогов:  {average_salary_gross_false} ,это показатель по {(count_salary_min_gross_false + count_salary_max_gross_false) / 2} вакансиям из {x}')
    list_salary.append(salary_1)
    salary_2 = (f'Средняя зарплата без вычетов налогов:  {average_salary_gross_true}  ,это показатель по {(count_salary_min_gross_true + count_salary_max_gross_true) / 2} вакансиям из {x}')
    list_salary.append(salary_2)
    salary_3 = (f'Средняя минимальная зарплата с вычетом налогов  {average_min_salary_gross_false}  ,это показатель по {count_salary_min_gross_false} вакансиям  из {x}')
    list_salary.append(salary_3)
    salary_4 = (f'Средняя максимальная зарплата с вычетом налогов  {average_max_salary_gross_false}  ,это показатель по {count_salary_max_gross_false} вакансиям  из {x}')
    list_salary.append(salary_4)
    salary_5 = (f'Средняя минимальная зарплата без вычетов   {average_min_salary_gross_true}  ,это показатель по {count_salary_min_gross_true} вакансиям  из {x}')
    list_salary.append(salary_5)
    salary_6 = (f'Средняя максимальная зарплата без вычетов   {average_max_salary_gross_true}  ,это показатель по {count_salary_max_gross_true} вакансиям  из {x}')
    list_salary.append(salary_6)
    for element in list_salary:
        print(element)

    choose = input('Сохранить файл ?, если да:   es   , если нет:  ENTER  ')
    if choose == 'es':
        with open('search_option.json', 'w') as o:
            json.dump({'Параметры поиска': params}, o)
        with open('number_skils.json', 'w') as z:
            json.dump({'Всего требований':  qiantity_skill}, z)
        with open('list_stils.json', 'w') as s:
            json.dump({'Список требований': list_skills}, s)
        with open('salary_analytics', 'w') as f:
            json.dump({'аналитика зарплат': list_salary}, f)


