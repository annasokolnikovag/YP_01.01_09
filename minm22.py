'''Minmax22°. Дано целое число N (> 2) и набор из N чисел. Найти два наименьших элемента из
данного набора и вывести эти элементы в порядке возрастания их значений.
'''

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

print(a.pop(min(a)), min(a))
