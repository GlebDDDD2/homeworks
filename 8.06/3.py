def count_pos_neg(array):
    pos_count = sum(1 for num in array if num > 0)
    neg_count = sum(1 for num in array if num < 0)
    return pos_count, neg_count

numbers = [3, -15, 27, -48, 59, -6, 14, -38, 72, -94, 18, -12]
pos_count, neg_count = count_pos_neg(numbers)
print("Кол-во положительных чисел:", pos_count)
print("Кол-во отрицательных чисел:", neg_count)