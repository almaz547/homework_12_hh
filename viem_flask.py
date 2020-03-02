from flask import Flask, render_template, request
from flask_menu_hh import *
import json
from flask_vacancy_search_params import get_dict_name_relevant_params
from flask_get_id import get_list_name_contry




app = Flask(__name__)

@app.route("/")
def index_new():

    return render_template('index.html')


@app.route("/main_form/", methods=['GET'])
def main_form():
    list_name_country = get_list_name_contry()
    dict_name_relevant_params = get_dict_name_relevant_params()

    return render_template('main_form_new.html', countrys=list_name_country,
                           dict_name=dict_name_relevant_params)


@app.route("/main_form/", methods=['POST'])
def main_form_post():
    try:
        name_vacancy = request.form['name_vacancy']

        with open('name_vacancy.txt', 'w', encoding='utf-8') as f:
            f.write(name_vacancy)
    except KeyError:
        name_vacancy = ''
    list_name_country = get_list_name_contry()
    try:
        name_country = request.form['choose_country']

        with open('name_country.txt', 'w', encoding='utf-8') as f:
            f.write(name_country)
        treatment_name_country()
    except KeyError:
        name_country = ''

    try:
        choose_region = request.form['choose_region']

        with open('choose_region.txt', 'w', encoding='utf-8') as f:
            f.write(choose_region)
        choos_region()
    except KeyError:
        choose_region = ''

    try:
        choose_city = request.form['choose_city']
        with open('choose_city.txt', 'w', encoding='utf-8') as f:
            f.write(choose_city)
        choos_city()
    except KeyError:
        choose_city = ''

    dict_name_relevant_params = get_dict_name_relevant_params()

    try:
        business_trip_readiness = request.form['готовность к командировкам']
        with open('business_trip_readiness.txt', 'w', encoding='utf-8') as f:
            f.write(business_trip_readiness)
    except KeyError:
        pass

    try:
        experience = request.form['опыт']
        with open('experience.txt', 'w', encoding='utf-8') as f:
            f.write(experience)
    except KeyError:
        pass

    try:
        employment = request.form['тип трудоустройства']
        with open('employment.txt', 'w', encoding='utf-8') as f:
            f.write(employment)
    except KeyError:
        pass

    try:
        education_level = request.form['уровень образования']
        with open('education_level.txt', 'w', encoding='utf-8') as f:
            f.write(education_level)
    except KeyError:
        pass

    try:
        language_level = request.form['языковой уровень']
        with open('language_level.txt', 'w', encoding='utf-8') as f:
            f.write(language_level)
    except KeyError:
        pass

    try:
        choose_result = request.form['result']
        with open('choose_result.txt', 'w', encoding='utf-8') as f:
            f.write(choose_result)
        get_result()
    except KeyError:
        choose_result = ''


    with open('name_country.txt', 'r', encoding='utf-8') as f:
        name_country = f.read()
    try:
        with open('name_vacancy.txt', 'r', encoding='utf-8') as f:
            name_vacancy = f.read()
    except FileNotFoundError:
        name_vacancy = ''

    try:
        with open('list_name_regions.json', 'r', encoding='utf-8') as f:
            list_name_regions = json.load(f)
    except FileNotFoundError:
        list_name_regions = []

    try:
        with open('list_name_citys.json', 'r', encoding='utf-8') as f:
            list_name_citys = json.load(f)
    except FileNotFoundError:
        list_name_citys = []

    try:
        with open('id.txt', 'r', encoding='utf-8') as f:
            id = f.read()
    except FileNotFoundError:
        id = ''

    return render_template('main_form_new.html', name=name_vacancy, countrys=list_name_country,
                           choose_city=choose_city, regions=list_name_regions, citys=list_name_citys,
                           id=id, dict_name=dict_name_relevant_params)


@app.route("/contact/", methods=['GET'])
def get_contact():

    return render_template('contact.html')



@app.route("/contact/", methods=['POST'])
def contact():
    try:
        contact_name = request.form['name']
        with open('contact_name.txt', 'w', encoding='utf-8') as f:
            f.write(contact_name)
    except KeyError:
        contact_name = ''

    try:
        email = request.form['email']
        with open('email.txt', 'w', encoding='utf-8') as f:
            f.write(email)
    except KeyError:
        email = ''

    try:
        telefon = request.form['telefon']
        with open('telefon.txt', 'w', encoding='utf-8') as f:
            f.write(telefon)
    except KeyError:
        telefon = ''

    try:
        message = request.form['message']
        with open('message.txt', 'w', encoding='utf-8') as f:
            f.write(message)
    except KeyError:
        message = ''
    return render_template('contact.html')


@app.route("/result/")
def result():
    try:
        with open('data_output.txt', 'r', encoding='utf-8') as f:
            data_output = f.read()
    except FileNotFoundError:
        data_output = ''
    if data_output:
        list_skills = get_statistics_key_skills_hh_of_sqlite()
        list_salary = get_statistics_salary_hh_of_sqlite()
        dict_general_indicators = get_general_indicators_of_sqlite()
        get_clear_search()
    else:
        list_skills = []
        list_salary = []
        dict_general_indicators = {}
    return render_template('result_new.html', skills=list_skills, salary=list_salary, gen_ind=dict_general_indicators)

if __name__ == "__main__":
    app.run(debug=True)
