from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///hh_18.sqlite', echo=True, pool_recycle=3600)

Base = declarative_base()


class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'id = {self.id}, {self.name}'


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'id = {self.id}, {self.name}'


class Key_skill(Base):
    __tablename__ = 'key_skill'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'id = {self.id}, {self.name}'


class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'id = {self.id}, {self.name}'


class Numbers_vacancy(Base):
    __tablename__ = 'numbers_vacancy'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    region_id = Column(Integer, ForeignKey('region.id'))

    def __init__(self, name, vacancy_id, region_id):
        self.name = name
        self.vacancy_id = vacancy_id
        self.region_id = region_id

    def __str__(self):
        return f'id = {self.id}, {self.name}'


class All_number_key_skills(Base):
    __tablename__ = 'all_number_key_skills'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    region_id = Column(Integer, ForeignKey('region.id'))

    def __init__(self, name, vacancy_id, region_id):
        self.name = name
        self.vacancy_id = vacancy_id
        self.region_id = region_id

    def __str__(self):
        return f'id = {self.id}, {self.name}'


class Numbers_key_skill(Base):
    __tablename__ = 'numbers_key_skill'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    key_skill_id = Column(Integer, ForeignKey('key_skill.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    region_id = Column(Integer, ForeignKey('region.id'))

    def __init__(self, name, key_skill_id, vacancy_id, region_id):
        self.name = name
        self.key_skill_id = key_skill_id
        self.vacancy_id = vacancy_id
        self.region_id = region_id

    def __str__(self):
        return f'id = {self.id}, {self.name}'


class Numbers_salary(Base):
    __tablename__ = 'numbers_salary'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    salary_id = Column(Integer, ForeignKey('salary.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    region_id = Column(Integer, ForeignKey('region.id'))

    def __init__(self, name, salary_id, vacancy_id, region_id):
        self.name = name
        self.region_id = region_id
        self.vacancy_id = vacancy_id
        self.salary_id = salary_id

    def __str__(self):
        return f'id = {self.id}, {self.name}'


class Numbers_show_salary(Base):
    __tablename__ = 'numbers_show_salary'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    salary_id = Column(Integer, ForeignKey('salary.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    region_id = Column(Integer, ForeignKey('region.id'))

    def __init__(self, name, salary_id, vacancy_id, region_id):
        self.name = name
        self.region_id = region_id
        self.vacancy_id = vacancy_id
        self.salary_id = salary_id

    def __str__(self):
        return f'id = {self.id}, {self.name}'


class Percent_key_skill(Base):
    __tablename__ = 'percent_key_skill'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    key_skill_id = Column(Integer, ForeignKey('key_skill.id'))
    numbers_key_skill_id = Column(Integer, ForeignKey('numbers_key_skill.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    region_id = Column(Integer, ForeignKey('region.id'))

    def __init__(self, name, key_skill_id, numbers_key_skill_id, vacancy_id, region_id):
        self.name = name
        self.region_id = region_id
        self.vacancy_id = vacancy_id
        self.key_skill_id = key_skill_id
        self.numbers_key_skill_id = numbers_key_skill_id


    def __str__(self):
        return f'id = {self.id}, {self.name}'

class Statistics_key_skills_hh(Base):
    __tablename__ = 'statistics_key_skills_hh'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    key_skill_id = Column(Integer, ForeignKey('key_skill.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    region_id = Column(Integer, ForeignKey('region.id'))
    numbers_key_skill_id = Column(Integer, ForeignKey('numbers_key_skill.id'))
    percent_key_skill_id = Column(Integer, ForeignKey('percent_key_skill.id'))

    def __init__(self, name, region_id, vacancy_id, key_skill_id, numbers_key_skill_id, percent_key_skill_id):
        self.name = name
        self.region_id = region_id
        self.vacancy_id = vacancy_id
        self.key_skill_id = key_skill_id
        self.numbers_key_skill_id = numbers_key_skill_id
        self.percent_key_skill_id = percent_key_skill_id

    def __str__(self):
        return f'id = {self.id}, {self.name}'



class Statistics_salary_hh(Base):
    __tablename__ = 'statistics_salary_hh'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary_id = Column(Integer, ForeignKey('salary.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    region_id = Column(Integer, ForeignKey('region.id'))
    numbers_salary_id = Column(Integer, ForeignKey('numbers_salary.id'))
    numbers_show_salary_id = Column(Integer, ForeignKey('numbers_show_salary.id'))

    def __init__(self, name, region_id, vacancy_id, salary_id, numbers_salary_id, numbers_show_salary_id):
        self.name = name
        self.region_id = region_id
        self.vacancy_id = vacancy_id
        self.salary_id = salary_id
        self.numbers_salary_id = numbers_salary_id
        self.numbers_show_salary_id = numbers_show_salary_id

    def __str__(self):
        return f'id = {self.id}, {self.name}'



class General_indicators(Base):
    __tablename__ = 'general_indicators'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    region_id = Column(Integer, ForeignKey('region.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    numbers_vacancy_id = Column(Integer, ForeignKey('numbers_vacancy.id'))
    all_number_key_skills_id = Column(Integer, ForeignKey('all_number_key_skills.id'))

    def __init__(self, name, region_id, vacancy_id, numbers_vacancy_id, all_number_key_skills_id):
        self.name = name
        self.region_id = region_id
        self.vacancy_id = vacancy_id
        self.numbers_vacancy_id = numbers_vacancy_id
        self.all_number_key_skills_id = all_number_key_skills_id

    def __str__(self):
        return f'id = {self.id}, {self.name}'


# Создание таблицы
Base.metadata.create_all(engine)