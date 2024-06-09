import time

#Сортировка пузырьком.
#соседние элементы списка сравниваются и меняют положение, если  находятся не в нужном порядке, процесс будет повторяеться, пока список не отсортируется.
#является элементарным, потому используется для маленьких списков или в целях обучения.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

file_path = "C:\\Users\\79144\\Desktop\\Новая папка (5)\\pythonProject\\Массив\\massiv.txt"

with open(file_path, "r") as file:
    data = file.read()
    arr = [int(x) for x in data.strip('[]\n').split(',')]

start_time = time.time()
bubble_sort(arr)
end_time = time.time()

itogo = end_time - start_time

print("Сортировка пузырьком %s секунд" % itogo)

#Cортировка вставками
#неплох для небольших списков
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

with open(file_path, "r") as file:
    data = file.read()
    arr = [int(x) for x in data.strip('[]\n').split(',')]

start_time2 = time.time()
insertion_sort(arr)
end_time2 = time.time()

itogo2= end_time2 - start_time2

print("Сортирвовка вставмками %s секунд" % itogo2)

#Сортировка слиянием
#разделяет список на половины, сортирует каждую половину отдельно, а затем сливает их вместе.
#часто используется в реальных приложениях из-за своей эффективности
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

with open(file_path, "r") as file:
    data = file.read()
    arr = [int(x) for x in data.strip('[]\n').split(',')]

start_time3 = time.time()
merge_sort(arr)
end_time3 = time.time()

itogo3 = end_time3 - start_time3

print("Сортировка слиянием заняла %s секунд" % itogo3)

#Быстрая сортировка (QuickSort
#выбирает опорный элемент из списка, разбивает список на две части вокруг опорного элемента и затем рекурсивно сортирует каждую часть.
#используется в реальных приложениях благодаря своей скорости
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

with open(file_path, "r") as file:
    data = file.read()
    arr = [int(x) for x in data.strip('[]\n').split(',')]

start_time4 = time.time()
quick_sort(arr)
end_time4 = time.time()

itogo4 = end_time4 - start_time4

print("Быстрая сортировка заняла %s секунд" % itogo4)

#Сортировка подсчетом
#создает массив счетчиков, чтобы подсчитать кол-во каждого элемента, а затем использует эту информацию для правильного расположения элементов в отсортированном списке.
#используется там, где диапозон чисел ограниченЮ например, при сортировке оценок или ID пользователей.
def counting_sort(arr):
    max_element = max(arr)
    min_element = min(arr)
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
with open(file_path, "r") as file:
    data = file.read()
    arr = [int(x) for x in data.strip('[]\n').split(',')]

start_time5 = time.time()
counting_sort(arr)
end_time5 = time.time()

itogo5 = end_time5 - start_time5
print("Cортировка подсчетом заняла %s секунд" % itogo5)
min_value = min(end_time, end_time2, end_time3, end_time4, itogo5)
print("Наименьшее значение среди пяти:", min_value)