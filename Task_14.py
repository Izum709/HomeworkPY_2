# Задача 14: Требуется вывести все целые степени двойки (т.е. числавида 2k), 
# не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input('введите число -> '))
number = 0
while  2 ** number <= n:
    print( 2 ** number)
    number += 1