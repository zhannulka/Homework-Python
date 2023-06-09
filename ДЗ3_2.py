# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

n = abs(int(input('Введите количество элементов массива А: ')))
elements = input("Введите через пробел элементы массива: ").split()
A_elem= list(map(int, elements))
if len(A_elem) != n:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы массива: '))
    min = abs(X - A_elem[0])
    index = 0
    for i in range(1, n):
        count = abs(X - A_elem[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_elem[index]} в массиве A наиболее близко по величине к числу {X}')