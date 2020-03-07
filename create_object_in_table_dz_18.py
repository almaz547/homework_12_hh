from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from create_table_sqlalchemy_dz_18 import Region, Vacancy, Key_skill, Salary, Numbers_vacancy
from create_table_sqlalchemy_dz_18 import All_number_key_skills, Numbers_key_skill, Numbers_salary
from create_table_sqlalchemy_dz_18 import Numbers_show_salary, Percent_key_skill
from create_table_sqlalchemy_dz_18 import Statistics_key_skills_hh, Statistics_salary_hh, General_indicators

engine = create_engine('sqlite:///hh_18.sqlite', echo=True, pool_recycle=3600)

Session = sessionmaker(bind=engine)
session = Session()




def object_check_in_database(object, table):
    object_in_base = False
    if object:
        objects_table = session.query(table).all()
        if objects_table:
            for object_table in objects_table:
                if object_table.name == object:
                    object_in_base = True
    return object_in_base


def write_region_in_database():
    name_region = get_name_region()
    name_table = Region
    object_in_base = object_check_in_database(name_region, name_table)
    if not object_in_base:
        region = Region(name_region)
        session.add(region)
        session.commit()
    return


def write_vacancy_in_database():
    name_vacancy = get_name_vacancy()
    name_table = Vacancy
    object_in_base = object_check_in_database(name_vacancy, name_table)
    if not object_in_base:
        vacancy = Vacancy(name_vacancy)
        session.add(vacancy)
        session.commit()
    return

def get_name_region():
    try:
        with open('name_id.txt', 'r', encoding='utf-8') as f:
            name_region = f.read()
    except FileNotFoundError:
        name_region = ''
    return name_region

def get_name_vacancy():
    try:
        with open('name_vacancy.txt', 'r', encoding='utf-8') as f:
            name_vacancy = f.read()
    except FileNotFoundError:
        name_vacancy = ''
    return name_vacancy

def get_id_region_of_database():
    name_region = get_name_region()
    region_base = session.query(Region).filter(Region.name == name_region)
    region_id = region_base[0].id
    return region_id

def get_id_vacancy_of_database():
    name_vacancy = get_name_vacancy()
    vacancy_base = session.query(Vacancy).filter(Vacancy.name == name_vacancy).all()
    vacancy_id = vacancy_base[0].id
    return vacancy_id

def write_key_skill_in_database(key_skill):
    name_table = Key_skill
    object_in_base = object_check_in_database(key_skill, name_table)
    if not object_in_base:
        key_skill_base = Key_skill(key_skill)
        session.add(key_skill_base)
        session.commit()
    return

def get_id_key_skill_of_database(key_skill):
    key_skill_base = session.query(Key_skill).filter(Key_skill.name == key_skill)
    key_skill_id = key_skill_base[0].id
    return key_skill_id

def write_salary_in_database(salary):
    name_table = Salary
    object_in_base = object_check_in_database(salary, name_table)
    if not object_in_base:
        salary_base = Salary(salary)
        session.add(salary_base)
        session.commit()
    return

def get_id_salary_of_database(salary):
    salary_base = session.query(Salary).filter(Salary.name == salary).all()
    salary_id = salary_base[0].id
    return salary_id

def write_numbers_vacancy_in_database(numbers_vacancy, vacancy_id, region_id):
    numbers_vacancy_base = Numbers_vacancy(numbers_vacancy, vacancy_id, region_id)
    session.add(numbers_vacancy_base)
    session.commit()
    return

def get_id_numbers_vacancy_of_database(numbers_vacancy, vacancy_id, region_id):
    numbers_vacancy_base = session.query(Numbers_vacancy).filter(Numbers_vacancy.name == numbers_vacancy,
                                                                 Numbers_vacancy.vacancy_id == vacancy_id,
                                                                 Numbers_vacancy.region_id == region_id)
    numbers_vacancy_id = numbers_vacancy_base[0].id
    return numbers_vacancy_id

def write_all_number_key_skills_in_database(all_number_key_skills, vacancy_id, region_id):
    all_number_key_skills_base = All_number_key_skills(all_number_key_skills, vacancy_id, region_id)
    session.add(all_number_key_skills_base)
    session.commit()
    return

def get_id_all_number_key_skills_of_database(all_number_key_skills, vacancy_id, region_id):
    all_number_key_skills_base = session.query(All_number_key_skills).\
        filter(All_number_key_skills.name == all_number_key_skills,
               All_number_key_skills.vacancy_id == vacancy_id,
               All_number_key_skills.region_id == region_id)
    all_number_key_skills_id = all_number_key_skills_base[0].id
    return all_number_key_skills_id

def write_numbers_key_skill_in_database(numbers_key_skill, key_skill_id, vacancy_id, region_id):
    numbers_key_skill_base = Numbers_key_skill(numbers_key_skill, key_skill_id, vacancy_id, region_id)
    session.add(numbers_key_skill_base)
    session.commit()
    return

def get_id_numbers_key_skill_of_database(numbers_key_skill, key_skill_id, vacancy_id, region_id):
    numbers_key_skill_base = session.query(Numbers_key_skill).\
        filter(Numbers_key_skill.name == numbers_key_skill,
               Numbers_key_skill.key_skill_id == key_skill_id,
               Numbers_key_skill.vacancy_id == vacancy_id,
               Numbers_key_skill.region_id == region_id)
    numbers_key_skill_id = numbers_key_skill_base[0].id
    return numbers_key_skill_id


def write_numbers_salary_in_database(numbers_salary, salary_id, vacancy_id, region_id):
    numbers_salary_base = Numbers_salary(numbers_salary, salary_id, vacancy_id, region_id)
    session.add(numbers_salary_base)
    session.commit()
    return

def get_id_numbers_salary_of_database(numbers_salary, salary_id, vacancy_id, region_id):
    numbers_salary_base = session.query(Numbers_salary).\
        filter(Numbers_salary.name == numbers_salary,
               Numbers_salary.salary_id == salary_id,
               Numbers_salary.vacancy_id == vacancy_id,
               Numbers_salary.region_id == region_id).all()
    numbers_salary_id = numbers_salary_base[0].id
    return numbers_salary_id

def write_numbers_show_salary_in_database(numbers_show_salary, salary_id, vacancy_id, region_id):
    numbers_show_salary_base = Numbers_show_salary(numbers_show_salary, salary_id, vacancy_id, region_id)
    session.add(numbers_show_salary_base)
    session.commit()
    return

def get_id_numbers_show_salary_of_database(numbers_show_salary, salary_id, vacancy_id, region_id):
    numbers_show_salary_base = session.query(Numbers_show_salary).\
        filter(Numbers_show_salary.name == numbers_show_salary,
               Numbers_show_salary.salary_id == salary_id,
               Numbers_show_salary.vacancy_id == vacancy_id,
               Numbers_show_salary.region_id == region_id)
    numbers_show_salary_id = numbers_show_salary_base[0].id
    return numbers_show_salary_id


def write_percent_key_skill_in_database(percent_key_skill, key_skill_id, numbers_key_skill_id, vacancy_id, region_id):
    percent_key_skill_base = Percent_key_skill(percent_key_skill, key_skill_id, numbers_key_skill_id, vacancy_id, region_id)
    session.add(percent_key_skill_base)
    session.commit()
    return

def get_id_percent_key_skill_of_database(percent_key_skill, key_skill_id, numbers_key_skill_id, vacancy_id, region_id):
    percent_key_skill_base = session.query(Percent_key_skill).\
        filter(Percent_key_skill.name == percent_key_skill,
               Percent_key_skill.key_skill_id == key_skill_id,
               Percent_key_skill.numbers_key_skill_id == numbers_key_skill_id,
               Percent_key_skill.vacancy_id == vacancy_id,
               Percent_key_skill.region_id == region_id)
    percent_key_skill_id = percent_key_skill_base[0].id
    return percent_key_skill_id


def write_statistics_key_skills_hh_in_database(list_skills):
    vacancy_id = get_id_vacancy_of_database()
    region_id = get_id_region_of_database()
    replay_indicators_delete(Statistics_key_skills_hh, region_id, vacancy_id)
    for show_key_skill in list_skills:            # show  -->  показатель
        key_skill = show_key_skill[0]
        numbers_key_skill = show_key_skill[1]
        percent_key_skill = show_key_skill[2]
        write_key_skill_in_database(key_skill)
        key_skill_id = get_id_key_skill_of_database(key_skill)
        write_numbers_key_skill_in_database(numbers_key_skill, key_skill_id, vacancy_id, region_id)
        numbers_key_skill_id = get_id_numbers_key_skill_of_database(numbers_key_skill, key_skill_id, vacancy_id, region_id)
        write_percent_key_skill_in_database(percent_key_skill, key_skill_id, numbers_key_skill_id, vacancy_id,
                                            region_id)
        percent_key_skill_id = get_id_percent_key_skill_of_database(percent_key_skill, key_skill_id, numbers_key_skill_id, vacancy_id, region_id)
        statistics_key_skills_hh_base = Statistics_key_skills_hh('statistics_key_skills_hh', region_id, vacancy_id, key_skill_id, numbers_key_skill_id, percent_key_skill_id)
        session.add(statistics_key_skills_hh_base)
    session.commit()
    return

def get_statistics_key_skills_hh_of_database():
    vacancy_id = get_id_vacancy_of_database()
    region_id = get_id_region_of_database()
    list_statistics_key_skills = []
    statistics_key_skills_hh = session.query(Statistics_key_skills_hh).\
        filter(Statistics_key_skills_hh.region_id == region_id,
               Statistics_key_skills_hh.vacancy_id == vacancy_id).all()
    for element in statistics_key_skills_hh:
        key_skill_id = element.key_skill_id
        numbers_key_skill_id = element.numbers_key_skill_id
        percent_key_skill_id = element.percent_key_skill_id
        key_skill = session.query(Key_skill).filter(Key_skill.id == key_skill_id)
        name_key_skill = key_skill[0].name
        numbers_key_skill = session.query(Numbers_key_skill).filter(Numbers_key_skill.id == numbers_key_skill_id)
        name_numbers_key_skill = numbers_key_skill[0].name
        percent_key_skill = session.query(Percent_key_skill).filter(Percent_key_skill.id == percent_key_skill_id)
        name_percent_key_skill = percent_key_skill[0].name
        list_statistics_key_skills.append((name_key_skill, name_numbers_key_skill, name_percent_key_skill))
    return list_statistics_key_skills


def replay_indicators_delete(statistics, region_id, vacancy_id):
    statistics_base = session.query(statistics).all()
    if statistics_base:
        for statistics_base_one in statistics_base:
            if statistics_base_one.region_id == region_id and statistics_base_one.vacancy_id == vacancy_id:
                session.delete(statistics_base_one)
        session.commit()
    return

def write_statistics_salary_hh_in_database(list_salary):
    vacancy_id = get_id_vacancy_of_database()
    region_id = get_id_region_of_database()
    replay_indicators_delete(Statistics_salary_hh, region_id, vacancy_id)
    for view_salary in list_salary:
        salary = view_salary[0]              # view  -->  вид
        numbers_salary = view_salary[1]
        numbers_show_salary = view_salary[2]
        write_salary_in_database(salary)
        salary_id = get_id_salary_of_database(salary)
        write_numbers_salary_in_database(numbers_salary, salary_id, vacancy_id, region_id)
        numbers_salary_id = get_id_numbers_salary_of_database(numbers_salary, salary_id, vacancy_id, region_id)
        write_numbers_show_salary_in_database(numbers_show_salary, salary_id, vacancy_id, region_id)
        numbers_show_salary_id = get_id_numbers_show_salary_of_database(numbers_show_salary, salary_id, vacancy_id, region_id)
        statistics_salary_hh = Statistics_salary_hh('statistics_salary_hh', region_id, vacancy_id, salary_id, numbers_salary_id, numbers_show_salary_id)
        session.add(statistics_salary_hh)
    session.commit()
    return

def get_statistics_salary_hh_of_database():
    vacancy_id = get_id_vacancy_of_database()
    region_id = get_id_region_of_database()
    list_statistics_salary = []
    statistics_salary_hh = session.query(Statistics_salary_hh).\
        filter(Statistics_salary_hh.region_id == region_id,
               Statistics_salary_hh.vacancy_id == vacancy_id).all()
    for element in statistics_salary_hh:
        salary_id = element.salary_id
        salary = session.query(Salary).filter(Salary.id == salary_id)
        name_salary = salary[0].name
        numbers_salary_id = element.numbers_salary_id
        numbers_salary = session.query(Numbers_salary).filter(Numbers_salary.id == numbers_salary_id)
        name_numbers_salary = numbers_salary[0].name
        numbers_show_salary_id = element.numbers_show_salary_id
        numbers_show_salary = session.query(Numbers_show_salary).filter(Numbers_show_salary.id == numbers_show_salary_id)
        name_numbers_show_salary = numbers_show_salary[0].name
        list_statistics_salary.append((name_salary, name_numbers_salary, name_numbers_show_salary))
    return list_statistics_salary


def get_numbers_vacancy(general_indicators):
    numbers_vacancy = general_indicators['numbers_vacancy']
    return numbers_vacancy

def get_all_number_key_skills(general_indicators):
    all_number_key_skills = general_indicators['all_numbers_key_skills']
    return all_number_key_skills

def write_general_indicators_in_database(general_indicators):
    vacancy_id = get_id_vacancy_of_database()
    region_id = get_id_region_of_database()
    replay_indicators_delete(General_indicators, region_id, vacancy_id)
    numbers_vacancy = get_numbers_vacancy(general_indicators)
    write_numbers_vacancy_in_database(numbers_vacancy, vacancy_id, region_id)
    numbers_vacancy_id = get_id_numbers_vacancy_of_database(numbers_vacancy, vacancy_id, region_id)
    all_number_key_skills = get_all_number_key_skills(general_indicators)
    write_all_number_key_skills_in_database(all_number_key_skills, vacancy_id, region_id)
    all_number_key_skills_id = get_id_all_number_key_skills_of_database(all_number_key_skills, vacancy_id, region_id)
    general_indicators_base = General_indicators('general_indicators', region_id, vacancy_id, numbers_vacancy_id, all_number_key_skills_id)
    session.add(general_indicators_base)
    session.commit()
    return

def get_general_indicators_hh_of_database():
    vacancy_id = get_id_vacancy_of_database()
    region_id = get_id_region_of_database()
    general_indicators_hh = session.query(General_indicators).\
        filter(General_indicators.region_id == region_id,
               General_indicators.vacancy_id == vacancy_id).all()
    vacancy_id = general_indicators_hh[0].vacancy_id
    vacancy = session.query(Vacancy).filter(Vacancy.id == vacancy_id)
    name_vacancy = vacancy[0].name
    region_id = general_indicators_hh[0].region_id
    region = session.query(Region).filter(Region.id == region_id)
    name_region = region[0].name
    numbers_vacancy_id = general_indicators_hh[0].numbers_vacancy_id
    numbers_vacancy = session.query(Numbers_vacancy).filter(Numbers_vacancy.id == numbers_vacancy_id)
    name_numbers_vacancy = numbers_vacancy[0].name
    all_number_key_skills_id = general_indicators_hh[0].all_number_key_skills_id
    all_number_key_skills = session.query(All_number_key_skills).\
        filter(All_number_key_skills.id == all_number_key_skills_id).all()
    name_all_number_key_skills = all_number_key_skills[0].name
    dict_general_indicators = {}
    dict_general_indicators['name_vacancy'] = name_vacancy
    dict_general_indicators['name_region'] = name_region
    dict_general_indicators['numbers_vacancy'] = name_numbers_vacancy
    dict_general_indicators['all_numbers_key_skills'] = name_all_number_key_skills
    return dict_general_indicators

