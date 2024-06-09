def find_max_min(array):
    max_num = max(array)
    min_num = min(array)
    return max_num, min_num

numbers = [-22, 45, -67, 34, -89, 100, -23, 5, -34, 78]
max_num, min_num = find_max_min(numbers)
print("Наибольшее число:", max_num)
print("Наименьшее число:", min_num)