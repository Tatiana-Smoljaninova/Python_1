# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов 
# в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

numbers = [int(input()) for _ in range(int(input()))]
print(numbers.count(int(input())))