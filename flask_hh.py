import requests
import json


def calculating_average(value, quantity):
    try:
        result = int(value/quantity)
    except ZeroDivisionError:
        result = 0
    return result


def get_and_analitik_skills_flask(params):
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
    x = 0
    result = requests.get(url, params=params).json()
    found = result['found']

    print(f'По запросу {params["text"]} найдено: {found} вакансий')

    while x <= found and params['page'] <= 99:
        # print(f'Страница № {params["page"]}')     #  Тест принт
        result = requests.get(url, params=params).json()
        items = result['items']
        for item in items:
            x += 1
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
        element_ = [element[0], element[1], round(element[1] / x * 100, 2)]
        list_skills.append(element_)

    list_salary = []
    salary_1 = ['Средн зп с выч налг', average_salary_gross_false, (count_salary_min_gross_false + count_salary_max_gross_false) / 2]
    list_salary.append(salary_1)
    salary_2 = ['Сред зп без выч налг', average_salary_gross_true, (count_salary_min_gross_true + count_salary_max_gross_true) / 2]
    list_salary.append(salary_2)
    salary_3 = ['Сред мин зп с выч налг', average_min_salary_gross_false, count_salary_min_gross_false]
    list_salary.append(salary_3)
    salary_4 = ['Сред макс зп с выч налг', average_max_salary_gross_false, count_salary_max_gross_false]
    list_salary.append(salary_4)
    salary_5 = ['Сред мин зп без выч налг', average_min_salary_gross_true, count_salary_min_gross_true]
    list_salary.append(salary_5)
    salary_6 = ['Сред макс зп без выч налг', average_max_salary_gross_true, count_salary_max_gross_true]
    list_salary.append(salary_6)

    general_indicators = {
        'name_vacancy': params["text"],
        'numbers_vacancy': found,
        'all_numbers_key_skills': qiantity_skill

    }

    return list_skills, list_salary, general_indicators

