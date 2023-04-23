# a = 5
# b = 5.89
# c = 'hello'
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# print('введите первую строку')
# a = input()
# print(a)

# print('Введите первое число: ')
# a = input()
# b = input('Введите второе число: ')

# print(a, ' + ', b, ' = ', a + b)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))
# c = str(c)
# print(c)
# print(type(c))

# c = 0
# print (c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# Иногда нельзя перевести в другой тип (строку к число)
# v = 'Tanya'
# v = int(v)

# print('Введите первое число: ')
# a = int(input())
# b = int(input2('Введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)

# a = 5.8879
# b = 6.5587
# print(round(a * b, 3))


# iter = 2
# iter += 3 #iter = iter + 3
# iter -= 4 #iter = iter - 4
# iter *= 5 #iter = iter * 5
# iter /= 5 #iter = iter / 5
# iter //= 5 #iter = iter // 5
# iter %= 5 #iter = iter % 5
# iter **= 5 #iter = iter ** 5

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это Маша')
# elif username == 'Марина':
#     print('Я так ждал вас, Марина')
# elif username == 'Татьяна':
#     print('Татьяна - красотка наша')
# else:
#     print('Привет,', username )

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:               # в else не заходим, т.к. сработала операция 'break'
#     print('Пожалуй')
#     print('хватит')
# print(i)

# метод флажка вместо break
# находим минимальный делитель числа с помощью флажка
# n = int(input())
# flag = True
# i = 2
# while flag: # т.е. цикл будет повторяться до тех пор, пока flag = true
#     if n % i == 0: # если остаток от деления числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленое на 2
#         print(n)
#         flag = False
#     i +=1

# for i in range(1, 10, 2):
#     print(i)

# a = 'qwerty'
# for i in a:
#     print(i)

# вывести 5 раз строку, которая будет состоять из 5 звездочек
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line+= "*"
#     print(line)

# text = 'Все даже очень неплохо, пошла уже хорошо, идем дальше , мы с тобой'
# print(len(text)) # позволяет узнать длину строки
# print('мы с тобой' in text) # проверяем есть ли строка в тексте
# print(text.lower()) # переводит текст в нижний регистр
# print(text.upper()) # переводит текст в верхний регистр
# print(text.replace('Все', 'ВСЕ')) # позволяет менять текст: что изменить, на что изменить

text = 'Начинается новая жизнь'
# print(text[0]) # первая буква текста
# print(text[1]) # вторая буква текста
# print(text[len(text)-1]) # последняя буква текста
# print(text[-1]) # последняя буква текста
# print(text[-5]) # пятая буква текста с конца
# print(text[:]) # весь текст
# print(text[:2])  # первые две буквы
# print(text[2:])  # с буквы с индексом 2 до конца
# print(text[len(text)-2:]) # последние две буквы
# # print(text[2:9]) # со 2 по 9 буквы 
# # print(text[6:-5])  # 
# print(text[0:len(text):6]) # идем от 0 индекса до конца строки с шагом 6
# print(text[::6]) # идем от 0 индекса до конца строки с шагом 6
text = text[2:9] + text[-5] + text[2]
print(text)
text = text[2:9] + text[-5] + text[2]
print(text)