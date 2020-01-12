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
print('2   Ввести id регионa вручную')

choise = input('Введите пункт меня "Регион":  ')

if choise == '1':
    id = get_and_choose_id()
    # print(f'id =>  {id}')                                        # Тест принт
    str_id = ''.join(str(i) if i is id[0] and str_id == '' else f', {i}' for i in id)
    # print(f'str_id С каталога  =>  {str_id}')                      # Тест принт
elif choise == '2':
    str_id = input('Введите id региона/города для поиска:  ')
    # print(f'str_id Вручную =>  {str_id}')                          # Тест принт
else:
    print('Некорректный выбор регирна !')
params['area'] = str_id

choise = input('Выбрать остальные параметры в режиме  да/нет:  es   ,если нет нажмите  ENTER  ')
if choise == 'es':
    params_search = question_vacancy_search_fields()
    # print(f'params_search  =>  {params_search}')                         # Тест принт
    params.update(params_search)
get_and_analitik_skills(params)





