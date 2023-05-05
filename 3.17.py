# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

# numbers = [input() for i in range(6)]
numbers = []
for i in range(6):
    numbers.append(input ())

print(len(set(numbers)))