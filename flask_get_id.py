import requests


def get_data_countrys_areas():
    DOMAIN = 'https://api.hh.ru'  # Адрес домена
    url_areas = f'{DOMAIN}/areas'
    data_countrys_areas = requests.get(url_areas).json()
    return data_countrys_areas

def get_name_id_countrys():
    data_countrys_areas = get_data_countrys_areas()
    dict_name_id_country = {}
    for country in data_countrys_areas:
        dict_name_id_country[country['name']] = country['id']
    return dict_name_id_country

def get_id_country(name_country):
    data_countrys_areas = get_data_countrys_areas()
    for country in data_countrys_areas:
        if name_country == country['name']:
            id_country = country['id']
            return id_country

def get_list_name_contry():
    data_countrys_areas = get_data_countrys_areas()
    list_name_country = []
    for country in data_countrys_areas:
        list_name_country.append(country['name'])
    return list_name_country



def get_data_areas(name_country):
    data_countrys_areas = get_data_countrys_areas()
    for country in data_countrys_areas:
        if name_country == country['name']:
            dict_country_areas = country['areas']
            return dict_country_areas



def get_name_id_regions(name_country):
    dict_country_areas = get_data_areas(name_country)
    dict_name_id_regions = {}
    for region in dict_country_areas:
        dict_name_id_regions[region['name']] = region['id']
    return dict_name_id_regions

def get_list_name_regions(name_country):
    dict_country_areas = get_data_areas(name_country)
    list_name_regions = []
    for region in dict_country_areas:
        list_name_regions.append(region['name'])
    return list_name_regions


def get_id_region(name_region, name_country):
    dict_country_areas = get_data_areas(name_country)
    for region in dict_country_areas:
        if name_region == region['name']:
            id_region = region['id']
            return id_region

def get_data_region_areas(name_country, name_region):
    dict_country_areas = get_data_areas(name_country)
    for region in dict_country_areas:
        if name_region == region['name']:
            dict_region_areas = region['areas']
            return dict_region_areas


def get_name_id_citys(dict_region_areas):
    dict_name_id_citys = {}
    for city in dict_region_areas:
        dict_name_id_citys[city['name']] = city['id']
    return dict_name_id_citys

def get_list_name_citys(name_country, name_region):
    dict_region_areas = get_data_region_areas(name_country, name_region)
    list_name_citys = []
    for city in dict_region_areas:
        list_name_citys.append(city['name'])
    return list_name_citys

def get_id_city(name_city, name_country, name_region):
    dict_region_areas = get_data_region_areas(name_country, name_region)
    for city in dict_region_areas:
        if name_city == city['name']:
            id_city = city['id']
            return id_city