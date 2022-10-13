import random
try:
    print("Введите коливество элементов для массива A:")
    kolvo_elementov_a = int(input())
    print("Введите коливество элементов для массива B:")
    kolvo_elementov_b = int(input())

    massiv_a = ["Пусто"] * kolvo_elementov_a
    massiv_b = ["Пусто"] * kolvo_elementov_b
    massiv_c = ["Пусто"] * max(kolvo_elementov_a, kolvo_elementov_b)
    count = 0

    for i in range(kolvo_elementov_a):
        massiv_a[i] = random.randint(0,99)
    for j in range(kolvo_elementov_b):
        massiv_b[j] = random.randint(0,99) 



    print("Массив А:")
    print(massiv_a)

    print("Массив B:")
    print(massiv_b)
#Проверка на совпадения в массивах и на запрет использования одного элемента 2 раза
    for x in range(len(massiv_a)):
        for y in range(len(massiv_b)):
            if massiv_a[x] == massiv_b[y]:
                massiv_c[count] = massiv_b[y] 
                count +=1
                massiv_b[y] = "Использованный элемент"
                break

    if massiv_c[0] != "Пусто":
        print("Совпавшие элементы:")
        for element_c in massiv_c:
            if element_c != "Пусто":
                print(element_c)
    else:
        print("Совпавших элементов нет")
except ValueError:
    print("Введите целое число в качестве значения коливества элементов массива")
    quit()