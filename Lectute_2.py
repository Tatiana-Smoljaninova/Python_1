# list_1 = [] # создаем пустой список
# list_2 = list() # создаем пустой список функцией list
# list_1 = [1, 2, 3, 4, 5]
# print(list_1) # напечатать список в скобках [1, 2, 3, 4, 5]
# print(*list_1) # напечатать список без скобок 1, 2, 3, 4, 5 - поставить *
# 
# for i in list_1:
#     print(i) # все значения списка выведутся в столбец

# print(len(list_1)) # функция len выводит длину списка

# print(list_1[0]) # напечатать первый элемент списка (индекс - 0)
# print(list_1[3]) # напечатать червертый элемент списка (индекс - 3)
# print(list_1[-1]) # счет индекса идет с конца - будет выведено последнее число
# print(list_1[-2]) # счет индекса идет с конца - будет выведено ПРЕДпоследнее число

# добавляем значения в список
# list_1 = [1, 2, 3, 4, 5]
# print(list_1)
# list_1.append(8) # функция append добавляет значения в конец списка 
# print(list_1)
# list_1.append(85)
# print(list_1)

# создаем пустой список и при кажд итерации цикла добавим значение i
# list_1 = []
# for i in range(5):
#     list_1.append(i) # значение i примет значение от 0 до 4? можно (i+1), тогда 1 2 3 4 5
#     print(list_1) 

# удаление последнего элемента списка
# list_1 = [1, 2, 3, 4, 5]
# print(list_1.pop()) # напечатает (вернет) последний элемент списка и удалит его
# print(list_1) # напечатает список уже без последнего элемента
# print(list_1.pop()) # напечатает уже ПРЕДпоследний элемент списка и удалит его
# print(list_1) 
# print(list_1.pop())
# print(list_1) 

# list_1 = [1, 2, 3, 4, 5]
# a = list_1.pop(3) # a = 4; a = значению элемента с индексом удаляемого элемента
# print(list_1)

# list_1 = [1, 2, 3, 4, 5]
# print(list_1.insert(2,11)) # функция insert вставляет значение: первый аргумент -
#                            # индекс куда вставить,второй - значение
#                            # [1, 2, 11, 3, 4, 5]
# print(list_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7]
# print(list_1[0]) # первый элемент списка
# print(list_1[1]) # второй элемент списка
# print(list_1[len(list_1)-1]) # последний элемент
# print(list_1[-1]) # последний элемент
# print(list_1[-5]) # пятый с конца элемент
# print(list_1[:]) # если перед двоеточием ничего нет - начинаем с начала списка, 
#                  # если после двоеточия ничего нет - заканчиваем в конце списка
#                  # т.е. тут выводим весь список
# print(list_1[:2]) # перед двоеточием ничего нет - начинаем с начала списка, 
#                   # после двоеточия 2 - заканчиваем на втором элементе списка
#                   # смотрим на индекс (т.е. третье число), но последнее число не берем
# print(list_1[len(list_1)-2:]) # начинаем с конца 2 элемента до конца списка
#                   # т.е. последние 2 элемента [6, 7]
# print(list_1[2:9]) # выводим с элемента с инжексом 3 до элеиента с индексом 9 
#                     #(последний не берем) [3, 4, 5, 6, 7]
# print(list_1[6:-18]) # начинаем с элемента с индексом 6, заканчиваем на элементе 
#                      # 18 с конца []
# print(list_1[0:len(list_1):6]) # идем с начала до конца С ШАГОМ 6 [1, 7]
# print(list_1[::6]) # то же самое: идем с начала до конца С ШАГОМ 6 [1, 7]

# # КОРТЕЖИ - неизменяемые списки
# t = () # создание пустого кортежа
# print(type(t)) # вывести тип переменной <class 'tuple'> (англ - кортеж)
# t = (1) # в кортеже хранится число 1
# print(type(t)) # тут уже тип переменной (1) - <class 'int'>
# t = (1, ) # в кортеже хранится число 1 - НАПИСАЛИ С ","
# print(type(t)) # тут уже тип переменной (1, ) - <class 'tuple'>
# # !! т.е. в конце всегда ставить ЗАПЯТУЮ, тогда будет тип кортеж 'tuple'

# #преобразовать список в кортеж:
# v = [1,2,3,4,5]
# print(v) # [1, 2, 3, 4, 5] скобки указывают на список
# print(type(v)) # <class 'list'>
# v = tuple(v)
# print(v) # (1, 2, 3, 4, 5) скобки указывают на кортеж
# print(type(v))

# множественное присваивание
# a = 1
# b = 2
# a,b = 1,2 # то же самое, что вверху
# print(a,b) # 1 2
# a = b = 1
# print(a,b) # 1 1

# v = ()
# v = (1,2,3,)
# a,b,c = v
# print(a,b,c) # 1 2 3

# отличия кортежа от списка
t = (1,2,3,) # создаем кортеж
print(t[1]) # можно вывести элемент кортежа, указав индекс # 2

for i in t:
    print(i) # выводим поочередно в столбик все значения кортежа

for i in range(len(t)):
    print(t[i]) # выводим поочередно в столбик все значения кортежа (то же, что и выше)

# # тип tuple не поддерживает изменение аргументов:
# t[0] = 2 # TypeError: 'tuple' object does not support item assignment
# а список поддерживает:
# t = [1,2,3]
# t[0] = 2
# print(t) # [2, 2, 3]
# # Т.Е. КОРТЕЖ ТОТ ЖЕ САМЫЙ СПИСОК, НО В ОТЛИЧИЕ ОТ СПИСКА В КОРТЕЖЕ МЫ НЕ М. 
# # ИЗМЕНЯТЬ ЭЛЕМЕНТЫ, ТОЛЬКО ВЫВОДИТЬ

# # СЛОВАРИ
# d = {} # создали пустой словарь
# d = dict() # то же самое - создали пустой словарь
# d['q'] = 'qwerty' # чтобы добавлять какие-то значения, необх в словаре указать ключ, по кот мы 
#                 # хотим получить q и какое-то значение
# d['w'] = 'werty'
# print(d) # {'q': 'qwerty'} т.е. в словаре d есть ключ q, по которому если мы обратимся,
#         # будем получать qwerty
#         # {'q': 'qwerty', 'w': 'werty'} - тут в словаре есть два значения с ключами
# print(d['q']) # qwerty - из словаря d выводим значение с ключем q

dictionary = {} # есть пустой словарь

