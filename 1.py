import random

try:
    print("Введите количество элементов массива:")
    kolvo_elementov = int(input())

    array = [0] * kolvo_elementov
    max_elenent = 0

    for i in range(kolvo_elementov):
        array[i] = random.randint(100,10000) / 100
    print("Изначальный массив:")
    print(array)

    for j in range(kolvo_elementov):
        if array[j] > max_elenent:
            max_elenent = array[j]
            element_number = j
    for a in range(element_number + 1, kolvo_elementov):
        array[a] = 0

    print("Изменённый массив:")
    print(array)
except ValueError:
    print("Введите целое число в качестве количества эллементов массива")
    quit()