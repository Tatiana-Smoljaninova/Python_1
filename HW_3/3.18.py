# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
numbers = [randint(1, 10) for _ in range(int(input()))]
           
print(numbers)
num = int(input())
rNum = numbers[0]

for i in numbers:
    if abs(num - i) < abs(num - rNum):
        rNum = i

print(rNum)

