import telebot
import requests
import json
from hh import get_analitik_skills

params = {}
TOKEN = '998148212:AAFL1oU3_nvvGZxXy7yYVcrBN3vuD9rdPgg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добрый день! Что умеет этот бот?\n"
        " БОТ может парсить сайт hh по определенным вакансям и заданному региону.\n"
    "Выводит количество вакансий, 50 наиболее встречающихся требований по этой вакансии и количество их появлений,"
          "а так же аналитику размера зарплаты по указанным показателям.\n"
                " Команда  /help - описание работы БОТа.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Cледуйте подсказкам БОТа, он будет предлагать вам варианты действий.\n'
                'На предлагаемую команду достаточно просто нажать, а предлагаемые действия и названия  - \n'
                'Необходимо точно переносить ( а лучше копировать )  в строку ввода !!!\n'
                  'Команда -  /hhstart  -  старт работы hh парсера.')

@bot.message_handler(commands=['hhstart'])
def request_name_vacansy(message):  # запрос имя вакансии
    bot.reply_to(message, 'Введите название вакансии или несколько через запятую:  ')  # reply_to --> ответить на

@bot.message_handler(commands=['get_analitik'])
def get_analitik(message):
    bot.reply_to(message, 'Терпение, идет подсчет аналитики')
    str_skills, str_salary = get_analitik_skills(params)
    bot.reply_to(message, str_skills)
    bot.reply_to(message, str_salary)


@bot.message_handler(commands=['view_country'])
def view_country_id(message):
    DOMAIN = 'https://api.hh.ru'  # Адрес домена
    url_areas = f'{DOMAIN}/areas'
    result = requests.get(url_areas).json()
    with open('result.json', 'w') as f:
        json.dump(result, f)
    country_str = ''
    list_country = []
    for country in result:
        country_name = country["name"]
        list_country.append(country_name)
        country_str += f'{country_name}\n'
    with open('list_country.json', 'w') as f:
        json.dump(list_country, f)
    bot.reply_to(message, f'{country_str}\nВыберите страну для поиска')



@bot.message_handler(content_types=['text'])
def choose_country(message):
    try:
        with open('result.json', 'r') as f:
            result = json.load(f)
    except FileNotFoundError:
        result = []
    try:
        with open('list_country.json', 'r') as f:
            list_country = json.load(f)
    except FileNotFoundError:
        list_country = []
    try:
        with open('country.json', 'r') as f:
            dict_country = json.load(f)
            for key, value in dict_country.items():
                name_country = str(key)
                id_country = str(value)
    except FileNotFoundError:
        dict_country = {}
    try:
        with open('dict_regions.json', 'r') as f:
            dict_regions = json.load(f)
    except FileNotFoundError:
        dict_regions = {}
    try:
        with open('region.json', 'r') as f:
            region_d = json.load(f)
            for key, value in region_d.items():
                name_region = str(key)
                id_region = str(value)
    except FileNotFoundError:
        region_d = {}
    try:
        with open('dict_citys.json', 'r') as f:
            dict_citys = json.load(f)
    except FileNotFoundError:
        dict_citys = {}

    if message.text in list_country:
        for country in result:  # Записали имя и id страны
            if message.text == country['name']:
                with open('country.json', 'w') as f:
                    json.dump({country['name']: country['id']}, f)
                bot.reply_to(message, f'Поиск по всей стране\nВыбрать регион')
                break

    elif message.text == 'Поиск по всей стране':
        params['area'] = id_country
        bot.reply_to(message, '/get_analitik  Подсчет аналитики')

    elif message.text == 'Выбрать регион':
        for country in result:
            list_regions = []
            if country['name'] == name_country:
                dict_regions = {}
                for region in country['areas']:
                    name_region = region['name']
                    id_region = region['id']
                    dict_regions[name_region] = id_region
                with open('dict_regions.json', 'w') as f:
                    json.dump(dict_regions, f)
                str_regions = ''
                for key, value in dict_regions.items():
                    str_regions += f'{key}\n'
                bot.reply_to(message, str_regions)
                break

    elif message.text == 'Поиск по всему региону':
        params['area'] = id_region
        bot.reply_to(message, '/get_analitik  Подсчет аналитики')

    elif message.text == 'Выбрать город':
        for country in result:
            if country['name'] == name_country:
                for region in country['areas']:
                    if name_region == region['name']:
                        dict_citys = {}
                        for city in region['areas']:
                            name_city = city['name']
                            id_city = city['id']
                            dict_citys[name_city] = id_city
                        with open('dict_citys.json', 'w') as f:
                            json.dump(dict_citys, f)
                        str_citys = ''
                        for key, value in dict_citys.items():
                            str_citys += f'{key}\n'
                        bot.reply_to(message, str_citys)
                        break

    elif message.text in dict_regions:
        for key, value in dict_regions.items():
            if message.text == key:
                bot.reply_to(message, f'Поиск по всему региону\nВыбрать город')
                with open('region.json', 'w') as f:
                    json.dump({key: value}, f)
                break

    elif message.text in dict_citys:
        for key, value in dict_citys.items():
            if message.text == key:
                params['area'] = value
                bot.reply_to(message, '/get_analitik  Подсчет аналитики')
                break

    else:
        entering_vacancy = message.text
        params['text'] = entering_vacancy
        bot.reply_to(message, '/view_country  Выбор страны для поиска')

bot.polling()






