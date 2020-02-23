from flask_get_id import get_list_name_regions
from flask_get_id import get_id_city
from flask_get_id import get_id_region
from flask_get_id import get_list_name_citys
from flask_get_id import get_id_country
import json
from flask_vacancy_search_params import get_id_params
from flask_hh import get_and_analitik_skills_flask


def get_clear_search():
    with open('name_vacancy.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('name_country.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('choose_region.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('list_name_regions.json', 'w', encoding='utf-8') as f:
        json.dump('', f)
    with open('list_name_citys.json', 'w', encoding='utf-8') as f:
        json.dump('', f)
    with open('choose_city.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('business_trip_readiness.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('experience.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('employment.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('education_level.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('language_level.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('id.txt', 'w', encoding='utf-8') as f:
        f.write('')
    with open('list_skills.json', 'w', encoding='utf-8') as f:
        json.dump('', f)
    with open('list_salary.json', 'w', encoding='utf-8') as f:
        json.dump('', f)
    with open('general_indicators.json', 'w', encoding='utf-8') as f:
        json.dump('', f)
    with open('expectation_result.txt', 'w', encoding='utf-8') as f:
        f.write('')
    return

get_clear_search()

def treatment_name_country():
    with open('name_country.txt', 'r', encoding='utf-8') as f:
        name_country = f.read()
    if name_country:
        list_name_regions = get_list_name_regions(name_country)
        with open('list_name_regions.json', 'w', encoding='utf-8') as f:
            json.dump(list_name_regions, f)
    return

def choos_region():
    try:
        with open('choose_region.txt', 'r', encoding='utf-8') as f:
            choose_region = f.read()
            choose_region = str(choose_region)
    except FileNotFoundError:
        choose_region = ''

    with open('name_country.txt', 'r', encoding='utf-8') as f:
        name_country = f.read()

    if choose_region == 'all_country':
        id_country = get_id_country(name_country)
        with open('name_id.txt', 'w', encoding='utf-8') as f:
            f.write(name_country)
        with open('id.txt', 'w', encoding='utf-8') as f:
            f.write(id_country)
    else:
        name_region = choose_region
        with open('name_region.txt', 'w', encoding='utf-8') as f:
            f.write(name_region)
        list_name_citys = get_list_name_citys(name_country, name_region)
        with open('list_name_citys.json', 'w', encoding='utf-8') as f:
            json.dump(list_name_citys, f)
    return

def choos_city():
    with open('name_country.txt', 'r', encoding='utf-8') as f:
        name_country = f.read()
    with open('name_region.txt', 'r', encoding='utf-8') as f:
        name_region = f.read()
    with open('choose_city.txt', 'r', encoding='utf-8') as f:
        choose_city = f.read()

    if choose_city == 'all_region':
        id_region = get_id_region(name_region, name_country)

        with open('name_id.txt', 'w', encoding='utf-8') as f:
            f.write(name_region)
        with open('id.txt', 'w', encoding='utf-8') as f:
            f.write(id_region)
    else:
        name_city = choose_city
        id_city = get_id_city(name_city, name_country, name_region)

        with open('name_id.txt', 'w', encoding='utf-8') as f:
            f.write(name_city)
        with open('id.txt', 'w', encoding='utf-8') as f:
            f.write(id_city)
    return


def treatment_params():
    params = {}
    with open('business_trip_readiness.txt', 'r', encoding='utf-8') as f:
        business_trip_readiness = f.read()
    if business_trip_readiness != 'all_готовность к командировкам':
        params_element = get_id_params('business_trip_readiness', business_trip_readiness)
        params.update(params_element)

    with open('experience.txt', 'r', encoding='utf-8') as f:
        experience = f.read()
    if experience != 'all_опыт':
        params_element = get_id_params('experience', experience)
        params.update(params_element)

    with open('employment.txt', 'r', encoding='utf-8') as f:
        employment = f.read()
    if employment != 'all_тип трудоустройства':
        params_element = get_id_params('employment', employment)
        params.update(params_element)

    with open('education_level.txt', 'r', encoding='utf-8') as f:
        education_level = f.read()
    if education_level != 'all_уровень образования':
        params_element = get_id_params('education_level', education_level)
        params.update(params_element)

    with open('language_level.txt', 'r', encoding='utf-8') as f:
        language_level = f.read()
    if language_level != 'all_языковой уровень':
        params_element = get_id_params('language_level', language_level)
        params.update(params_element)
    return params


def get_result():
    params = {}
    try:
        with open('choose_result.txt', 'r', encoding='utf-8') as f:
            choose_result = f.read()
    except FileNotFoundError:
        choose_result = ''

    if choose_result:
        if choose_result == 'clear search':
            get_clear_search()
        else:
            with open('name_id.txt', 'r', encoding='utf-8') as f:
                name_id = f.read()
            try:
                with open('name_vacancy.txt', 'r', encoding='utf-8') as f:
                    name_vacancy = f.read()
            except FileNotFoundError:
                name_vacancy = ''

            try:
                with open('id.txt', 'r', encoding='utf-8') as f:
                    id = f.read()
            except FileNotFoundError:
                id = ''

            if name_vacancy:
                params['text'] = name_vacancy
                if id:
                    params['area'] = id
                params_vacancy = treatment_params()
                params.update(params_vacancy)

                list_skills, list_salary, general_indicators = get_and_analitik_skills_flask(params)
                general_indicators.update({'name_id': name_id})

                with open('list_skills.json', 'w', encoding='utf-8') as f:
                    json.dump(list_skills, f)
                with open('list_salary.json', 'w', encoding='utf-8') as f:
                    json.dump(list_salary, f)
                with open('general_indicators.json', 'w', encoding='utf-8') as f:
                    json.dump(general_indicators, f)
            else:
                pass





