import requests


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


def get_result():           # Поиск вакансии выбор полей
    DOMAIN = 'https://api.hh.ru'                     # Адрес домена
    url_dictionaries = f'{DOMAIN}/dictionaries'
    result = requests.get(url_dictionaries).json()
    return result


def get_data_relevant_params_rus(relevant_params):
    result = get_result()
    dict_data_relevant_params_rus = {}
    for key, value in result.items():
        if key in relevant_params:
            if key in translation:
                name_rus = translation[key]
                dict_data_relevant_params_rus[name_rus] = value
    return dict_data_relevant_params_rus


def get_data_relevant_params(relevant_params):
    result = get_result()
    dict_data_relevant_params = {}
    for key, value in result.items():
        if key in relevant_params:
            dict_data_relevant_params[key] = value
    return dict_data_relevant_params


def get_id_params(name_params, param_label):
    dict_data_relevant_params = get_data_relevant_params(relevant_params)
    params = {}
    data_list_name_params = dict_data_relevant_params[name_params]
    for element in data_list_name_params:
        if param_label == element['name']:
            id_param = element['id']
            params[name_params] = id_param
            return params


def get_dict_name_relevant_params():
    dict_data_relevant_params = get_data_relevant_params_rus(relevant_params)
    dict_name_relevant_params = {}
    for name, data in dict_data_relevant_params.items():
        list_name_element = []
        for element in data:
            name_element = element['name']
            list_name_element.append(name_element)
        dict_name_relevant_params[name] = list_name_element
    return dict_name_relevant_params





