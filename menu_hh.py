from search_params import get_and_choose_id
from hh import get_and_analitik_skills
from search_params import question_vacancy_search_fields

params = {}
str_id = ''
entering_vacancy = input('Введите название вакансии или несколько через запятую:  ')
params['text'] = entering_vacancy

print('Выбор региона')
print('Выберите вариант ввода:  ')
print('1   Выбрать регион из каталога в режиме да/нет')
print('2   Ввести id регионa (одного) вручную')

how_to_choose = input('Как выбирать ?  1   или   2  :   ')

if how_to_choose == '1':
    id = get_and_choose_id()
    str_id = ''.join(str(i) if i is id[0] and str_id == '' else f', {i}' for i in id)
elif how_to_choose == '2':
    str_id = input('Введите id региона/города для поиска:  ')
else:
    print('Некорректный выбор регирна !')
params['area'] = str_id

choise = input('Выбрать остальные параметры в режиме  да/нет:  yes   ,если нет нажмите  ENTER  ')
if choise == 'yes':
    params_search = question_vacancy_search_fields()
    params.update(params_search)
get_and_analitik_skills(params)





