import sqlite3

conn = sqlite3.connect('sqlite_hh_17.db', check_same_thread=False)
cursor = conn.cursor()


def get_name_vacancy():
    try:
        with open('name_vacancy.txt', 'r', encoding='utf-8') as f:
            name_vacancy = f.read()
    except FileNotFoundError:
        name_vacancy = ''
    if name_vacancy:
        return name_vacancy

def get_name_region():
    try:
        with open('name_id.txt', 'r', encoding='utf-8') as f:
            name_region = f.read()
    except FileNotFoundError:
        name_region = ''
    return name_region

def write_name_region_in_sqlite():
    name_region = get_name_region()
    cursor.execute("insert into region (name) values (?)", (name_region,))
    return

def get_id_region_of_sqlite():
    name_region = get_name_region()
    cursor.execute("SELECT id from region where region.name=?", (name_region,))
    region_id = cursor.fetchall()
    region_id = region_id[0][0]
    return region_id

def write_name_vacancy_in_sqlite():
    name_vacancy = get_name_vacancy()
    cursor.execute("insert into vacancy (name) values (?)", (name_vacancy,))
    return

def get_id_name_vacancy_of_sqlite():
    name_vacancy = get_name_vacancy()
    cursor.execute('select id from vacancy where vacancy.name=?', (name_vacancy,))
    id_vacancy = cursor.fetchall()[0][0]
    return id_vacancy

def write_key_skills_in_sqlite(name_key_skills):
    cursor.execute('insert into key_skills (name) values (?)', (name_key_skills,))
    return

def get_id_key_skills_of_sqlite(name_key_skills):
    cursor.execute('select id from key_skills where key_skills.name=?', (name_key_skills,))
    key_skills_id = cursor.fetchall()[0][0]
    return key_skills_id

def write_percent_key_skills_in_sqlite(percent_key_skills, name_key_skills, numbers_key_skills):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    key_skills_id = get_id_key_skills_of_sqlite(name_key_skills)
    numbers_key_skills_id = get_id_numbers_key_skills_of_sqlite(name_key_skills, numbers_key_skills)
    cursor.execute('insert into percent_key_skills (name, key_skills_id, numbers_key_skills_id, '
                   'vacancy_id, region_id) values (?,?,?,?,?)'
                   , (percent_key_skills, key_skills_id, numbers_key_skills_id, vacancy_id, region_id))
    return

def get_id_percent_key_skills_of_sqlite(percent_key_skills, name_key_skills, numbers_key_skills):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    key_skills_id = get_id_key_skills_of_sqlite(name_key_skills)
    numbers_key_skills_id = get_id_numbers_key_skills_of_sqlite(name_key_skills, numbers_key_skills)
    cursor.execute('select id from percent_key_skills pks where pks.name=? and pks.key_skills_id=? and '
                   'pks.numbers_key_skills_id=? and pks.vacancy_id=? and pks.region_id=?',
                   (percent_key_skills, key_skills_id, numbers_key_skills_id,
                                                                vacancy_id, region_id))
    percent_key_skills_id = cursor.fetchall()[0][0]
    return percent_key_skills_id



def write_numbers_key_skills_in_sqlite(numbers_key_skills, name_key_skills):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    key_skills_id = get_id_key_skills_of_sqlite(name_key_skills)
    cursor.execute('insert into numbers_key_skills (name, key_skills_id, vacancy_id, region_id) values (?,?,?,?)',
                   (numbers_key_skills, key_skills_id, vacancy_id, region_id))
    return



def get_id_numbers_key_skills_of_sqlite(name_key_skills, numbers_key_skills):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    key_skills_id = get_id_key_skills_of_sqlite(name_key_skills)
    cursor.execute('select id from numbers_key_skills nks where nks.name=? and nks.key_skills_id=? and nks.vacancy_id=? '
                   'and nks.region_id=?', (numbers_key_skills, key_skills_id, vacancy_id, region_id))
    numbers_key_skills_id = cursor.fetchall()[0][0]
    return numbers_key_skills_id

def write_name_salary_in_sqlite(name_salary):
    cursor.execute('insert into salary (name) values (?)', (name_salary,))
    return

def get_id_salary_of_sqlite(name_salary):
    cursor.execute('select id from salary where salary.name=?', (name_salary,))
    salary_id = cursor.fetchall()[0][0]
    return salary_id

def write_numbers_show_salary_in_sqlite(numbers_show_salary, name_salary):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    salary_id = get_id_salary_of_sqlite(name_salary)
    cursor.execute('insert into numbers_show_salary (name, salary_id, vacancy_id, region_id) values (?,?,?,?)',
                   (numbers_show_salary, salary_id, vacancy_id, region_id))
    return

def get_id_numbers_show_salary_of_sqlite(numbers_show_salary, name_salary):         # show  -->  показатель
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    salary_id = get_id_salary_of_sqlite(name_salary)
    cursor.execute('select id from numbers_show_salary nss where nss.name=? and nss.salary_id=? and '
                   'nss.vacancy_id=? and nss.region_id=?',
                   (numbers_show_salary, salary_id, vacancy_id, region_id))
    numbers_show_salary_id = cursor.fetchall()[0][0]
    return numbers_show_salary_id

def write_numbers_salary_in_sqlite(name_salary, numbers_salary):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    salary_id = get_id_salary_of_sqlite(name_salary)
    cursor.execute('insert into numbers_salary (name, salary_id, vacancy_id, region_id) values (?,?,?,?)',
                   (numbers_salary, salary_id, vacancy_id, region_id))
    return

def get_id_numbers_salary_of_sqlite(name_salary, numbers_salary):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    salary_id = get_id_salary_of_sqlite(name_salary)
    cursor.execute('select id from numbers_salary ns where ns.name=? and ns.salary_id=? and ns.vacancy_id=? '
                   'and ns.region_id=?', (numbers_salary, salary_id, vacancy_id, region_id))
    numbers_salary_id = cursor.fetchall()[0][0]
    return numbers_salary_id


def write_statistics_salary_hh_in_sqlite(list_salary):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    for view_salary in list_salary:
        name_salary = view_salary[0]              # view  -->  вид
        numbers_salary = view_salary[1]
        numbers_show_salary = view_salary[2]
        write_name_salary_in_sqlite(name_salary)
        salary_id = get_id_salary_of_sqlite(name_salary)
        write_numbers_salary_in_sqlite(name_salary, numbers_salary)
        numbers_salary_id = get_id_numbers_salary_of_sqlite(name_salary, numbers_salary)
        write_numbers_show_salary_in_sqlite(numbers_show_salary, name_salary)
        numbers_show_salary_id = get_id_numbers_show_salary_of_sqlite(numbers_show_salary, name_salary)
        cursor.execute('insert into statistics_salary_hh (region_id, vacancy_id, salary_id, numbers_salary_id,'
                       'numbers_show_salary_id) values (?,?,?,?,?)', (region_id, vacancy_id, salary_id,
                                                                      numbers_salary_id, numbers_show_salary_id))
    return


def get_statistics_salary_hh_of_sqlite():
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    cursor.execute('select s.name, ns.name, nss.name from statistics_salary_hh sshh, salary s, numbers_salary ns, '
                   'numbers_show_salary nss where sshh.salary_id == s.id and sshh.numbers_salary_id == ns.id and '
                   'sshh.numbers_show_salary_id == nss.id and sshh.vacancy_id=? and sshh.region_id=?',
                   (vacancy_id, region_id))
    result = cursor.fetchall()
    list_statistics_salary = []
    for tuple_salary in result:
        name_salary = tuple_salary[0]
        numbers_salary = tuple_salary[1]
        percent_numbers_salary = tuple_salary[2]
        statistics_salary = (name_salary, numbers_salary, percent_numbers_salary)
        list_statistics_salary.append(statistics_salary)
    return list_statistics_salary



def write_statistics_key_skills_hh_in_sqlite(list_skills):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    for show_key_skills in list_skills:            # show  -->  показатель
        name_key_skills = show_key_skills[0]
        numbers_key_skills = show_key_skills[1]
        percent_key_skills = show_key_skills[2]
        write_key_skills_in_sqlite(name_key_skills)
        key_skills_id = get_id_key_skills_of_sqlite(name_key_skills)
        write_numbers_key_skills_in_sqlite(numbers_key_skills, name_key_skills)
        numbers_key_skills_id = get_id_numbers_key_skills_of_sqlite(name_key_skills, numbers_key_skills)
        write_percent_key_skills_in_sqlite(percent_key_skills, name_key_skills, numbers_key_skills)
        percent_key_skills_id = get_id_percent_key_skills_of_sqlite(percent_key_skills, name_key_skills, numbers_key_skills)
        cursor.execute('insert into statistics_key_skills_hh (region_id, vacancy_id, '
                       'key_skills_id, numbers_key_skills_id, percent_key_skills_id) values (?,?,?,?,?)',
                       (region_id, vacancy_id, key_skills_id, numbers_key_skills_id, percent_key_skills_id))
    return

def get_statistics_key_skills_hh_of_sqlite():
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    cursor.execute('select ks.name, nks.name, pks.name from statistics_key_skills_hh skshh, key_skills ks, '
                   'numbers_key_skills nks, percent_key_skills pks where skshh.key_skills_id == ks.id and '
                   'skshh.numbers_key_skills_id == nks.id and skshh.percent_key_skills_id == pks.id and '
                   'skshh.vacancy_id=? and skshh.region_id=?', (vacancy_id, region_id))
    result = cursor.fetchall()
    list_statistics_key_skills = []
    for tuple_key_skills in result:
        name_key_skills = tuple_key_skills[0]
        numbers_key_skills = tuple_key_skills[1]
        percent_key_skills = tuple_key_skills[2]
        statistics_key_skills = (name_key_skills, numbers_key_skills, percent_key_skills)
        list_statistics_key_skills.append(statistics_key_skills)
    return list_statistics_key_skills


def write_general_indicators_in_sqlite(general_indicators):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    write_numbers_vacancy_in_sqlite(general_indicators)
    numbers_vacancy_id = get_id_numbers_vacancy_of_sqlite(general_indicators)
    write_all_numbers_key_skills_in_sqlite(general_indicators)
    all_numbers_key_skills_id = get_id_all_numbers_key_skills_of_sqlite(general_indicators)
    cursor.execute('insert into general_indicators (vacancy_id, region_id, numbers_vacancy_id, all_numbers_key_skills_id) '
                   'values (?,?,?,?)', (vacancy_id, region_id, numbers_vacancy_id, all_numbers_key_skills_id))
    return

def get_general_indicators_of_sqlite():
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    cursor.execute('select v.name, r.name, nv.name, anks.name from general_indicators gi, vacancy v, region r, numbers_vacancy nv, '
                   'all_numbers_key_skills anks where gi.vacancy_id == v.id and gi.region_id == r.id and '
                   'gi.numbers_vacancy_id == nv.id and gi.all_numbers_key_skills_id == anks.id and v.id=? and r.id=?',
                   (vacancy_id, region_id))
    list_general_indicators = cursor.fetchall()
    dict_general_indicators = {}
    dict_general_indicators['name_vacancy'] = list_general_indicators[0][0]
    dict_general_indicators['name_region'] = list_general_indicators[0][1]
    dict_general_indicators['numbers_vacancy'] = list_general_indicators[0][2]
    dict_general_indicators['all_numbers_key_skills'] = list_general_indicators[0][3]
    return dict_general_indicators


def get_numbers_vacancy(general_indicators):
    numbers_vacancy = general_indicators['numbers_vacancy']
    return numbers_vacancy

def get_all_numbers_key_skills(general_indicators):
    all_numbers_key_skills = general_indicators['all_numbers_key_skills']
    return all_numbers_key_skills

def write_all_numbers_key_skills_in_sqlite(general_indicators):
    all_numbers_key_skills = get_all_numbers_key_skills(general_indicators)
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    cursor.execute('insert into all_numbers_key_skills (name, vacancy_id, region_id) values (?,?,?)',
                   (all_numbers_key_skills, vacancy_id, region_id))
    return

def get_id_all_numbers_key_skills_of_sqlite(general_indicators):
    all_numbers_key_skills = get_all_numbers_key_skills(general_indicators)
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    cursor.execute('select id from all_numbers_key_skills anks where anks.name=? and anks.vacancy_id=? and anks.region_id=?',
                   (all_numbers_key_skills, vacancy_id, region_id))
    all_numbers_key_skills_id = cursor.fetchall()[0][0]
    return all_numbers_key_skills_id

def write_numbers_vacancy_in_sqlite(general_indicators):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    numbers_vacancy = get_numbers_vacancy(general_indicators)
    cursor.execute('insert into numbers_vacancy (name, vacancy_id, region_id) values (?,?,?)',
                   (numbers_vacancy, vacancy_id, region_id))
    return


def get_id_numbers_vacancy_of_sqlite(general_indicators):
    vacancy_id = get_id_name_vacancy_of_sqlite()
    region_id = get_id_region_of_sqlite()
    numbers_vacancy = get_numbers_vacancy(general_indicators)
    cursor.execute('select id from numbers_vacancy nv where nv.name=? and nv.vacancy_id=? and nv.region_id=?',
                   (numbers_vacancy, vacancy_id, region_id))
    numbers_vacancy_id = cursor.fetchall()[0][0]
    return numbers_vacancy_id





