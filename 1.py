import random


print("Введите размерность массива:")
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
print(element_number, max_elenent)
for a in range(element_number + 1, kolvo_elementov):
    array[a] = 0

print("Изменённый массив:")
print(array)
    