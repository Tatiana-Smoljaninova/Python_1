# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая
# длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они
# называют период, в который среднесуточная температура ежедневно превышала 
# 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел. Каждое число – среднесуточная
# температура в соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

print('Введите общее количество дней (от 1 до 100): ')
N = int(input())
count = 0
warmPeriod1 = 0
warmPeriod2 = 0

print('Введите температуру первого дня: ')
tempDay1 = int(input())
if tempDay1 > 0:
   count += 1
   warmPeriod1 +=1
else: count += 1

print('Вводите поочередно данные температур: ')
for i in range(N-1): # пока i от 0 до N-1
    tempDay2 = int(input())
    if tempDay2 < 0 and tempDay1 > 0:
        count += 1
        temp = warmPeriod1 
    elif tempDay2 < 0 and tempDay1 < 0:
        count += 1
    elif tempDay2 > 0 and tempDay1 < 0:
        count += 1
        warmPeriod2 = 1
    else: 
        count += 1
        if tempDay1 > 0: 
            warmPeriod1 +=1 ## тогда мы продолжаем счетчик теплых дней
            tempDay2 = tempDay1
        elif 
        warmPeriod2 = 1
print



    temp = int(input(f'{i + 1}-день: '))

# print('Вводите среднедневную температуру первого дня: ')
# averageTemp1 = int(input())
# print('Вводите последовательно среднедневную температуру: ')
# averageTemp2 = int(input())

# count = 0

# while count == N
#     if averageTemp1 > 0
#         countDays += 1
#         count+=1
#     else count+=1
# if averageTemp1 > 0

# if averageTemp < 0
# while averageTemp :
#     print('Вводите последовательно среднедневную температуру: ')
#     averageTemp = int(input())
#     if verageTemp > 0



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
