import requests

def get_and_choose_id():
    DOMAIN = 'https://api.hh.ru'  # Адрес домена
    url_areas = f'{DOMAIN}/areas'
    result = requests.get(url_areas).json()
    id = []
    for country in result:
        print(country['name'])
        choose_country = input(f'Просмотр id по стране <  {country["name"]}  > введите   yes   ,если пропустить страну:   INTER  ')
        if choose_country == 'yes':
            how_to_search = input('Поиск по всей стране целиком введите   yes   ,выбрать регион:   INTER ')
            if how_to_search == 'yes':
                id.append(country['id'])
                return id
            else:
                for regions in country['areas']:
                    print(regions['name'])
                    if regions['areas'] != []:
                        choose = input('Поиск по всему региону   es   ,выбрать город  INTER,   nn   перейти к следующему региону,  stop  Закончить поиск по стране  ')
                    else:
                        choose = input('Добавить регион в поиск   es   ,   nn   перейти к следующему региону,  stop   выйти из страны  ')
                    if choose == 'es':
                        id.append(regions['id'])
                        return id
                    elif choose == 'nn':
                        continue
                    elif choose == 'stop':
                        break
                    else:
                        for city in regions['areas']:
                            print(city['name'])
                            choose = input('Ввыбрать город для поиска введите   es   ,пропустить  INTER,  nn   выйти из региона ')
                            if choose == 'es':
                                id.append(city['id'])
                                return id
                            elif choose == 'nn':
                                break


translation = {'vacancy_label': 'метка вакансии', 'resume_access_type': 'видимость вакансии',
               'vacancy_search_order': 'приоритет выбора вакансии', 'vacancy_search_fields': 'выбор полей поиска вакансии',
               'vacancy_type': 'тип вакансии', 'gender': 'пол', 'preferred_contact_type': 'предпочтетельный тип контакта',
               'travel_time': 'время поездки', 'relocation_type': 'тип переселения',
               'business_trip_readiness': 'готовность к командировкам', 'resume_contacts_site_type': 'продолжить контакты тип сайта',
               'employer_type': 'тип работодателя', 'employer_relation': 'отношения с работодателем',
               'negotiations_state': 'состояние переговоров', 'negotiations_participant_type': 'тип участника переговоров',
               'negotiations_order': 'старшинство переговоров', 'resume_moderation_note': 'примечание о возобновлении модерации',
               'vacancy_relation': 'соотношение вакансий', 'resume_status': 'состояние резюме',
               'resume_search_logic': 'логика поиска резюме', 'resume_search_fields': 'где искать вакансию',
               'messaging_status': 'состояние обмена сообщериями', 'employer_active_vacancies_order': 'заказ активных вакансий работодателя',
               'employer_archived_vacancies_order': 'работодатель заархивировал заказ вакансий',
               'employer_hidden_vacancies_order': 'заказ закрытых вакансий работодателя',
               'applicant_comments_order': 'порядок коментариев заявителя', 'vacancy_not_prolonged_reason': 'вакансия не затянулась причина',
               'vacancy_site': 'сайт вакансии', 'resume_hidden_fields': 'возобновление скрытых файлов', 'experience': 'опыт',
               'employment': 'тип трудоустройства', 'schedule': 'график', 'education_level': 'уровень образования',
               'currency': 'валюта', 'vacancy_billing_type': 'тип выставления счетов за вакансии',
               'applicant_comment_access_type': 'тип доступа к комертариям заявателя', 'vacancy_cluster': 'кластер заявителя',
               'driver_license_types': 'типы водительских прав', 'language_level': 'языковой уровень',
               'resume_search_label': 'ярлык поиска резюме', 'resume_search_relocation': 'резюме поиск перемещение',
               'resume_search_order': 'порядок поиска резюме', 'resume_search_experience_period': 'период опыта поиска резюме',
               }

relevant_params = ['business_trip_readiness', 'experience', 'language_level', 'education_level', 'employment']

def question_vacancy_search_fields():           # Поиск вакансии выбор полей
    DOMAIN = 'https://api.hh.ru'                     # Адрес домена
    url_dictionaries = f'{DOMAIN}/dictionaries'
    result = requests.get(url_dictionaries).json()
    params = {}
    choose = input('Просмотреть актуальные параметры:  1   ,все параметры:   2  ')
    for el in result:
        if el == 'vacancy_cluster':
            continue
        if choose == '1':
            if not el in relevant_params:
                continue
        if el in translation:
            name_rus = translation[el]
            print(name_rus,str('-->'), result[el])
            question = input(f'Просмотреть параметры < {name_rus} >  нажтите:  es   если нет нажмите  INTER ')
        else:
            print(el,str('-->'), result[el])
            question = input(f'Просмотреть параметры < {el} >  нажтите:  es   если нет нажмите  INTER ')
        if question == 'es':
            params_element = []
            params_element_str = ''
            for element in result[el]:
                print(element)
                try:
                    question = input(f'Выбрать параметр < {element["name"]} >  у  < {name_rus} >  нажмите:  es   если нет нажмите  INTER ')
                except KeyError:
                    question = input(f'Выбрать параметр < {element["id"]} >  у  < {name_rus} >  нажмите:  es   если нет нажмите  INTER ')
                if question == 'es':
                    if el == 'currency':
                        params_element.append(element['code'])
                    else:
                        params_element.append(element['id'])
                    params_element_str = ''.join(str(i) if params_element_str == '' and i is params_element[0] else f', {i}' for i in params_element)
                    params[el] = params_element_str
                    break
    return params
