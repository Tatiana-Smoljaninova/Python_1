# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите трехзначное целое число')
number = int(input())
summa = 0
if number > 999:
    print('Ведите трехзначное число')
elif number < 100:
    print('Ведите трехзначное число')
else:
    number = int(number)
    while number > 0:
        summa = summa + number % 10
        number = number // 10
    print(summa)
    