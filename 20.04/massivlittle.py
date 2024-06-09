def find_divide_index(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == 1 and arr[mid - 1] == 0:
            return mid

        elif arr[mid] == 1:
            right = mid - 1

        else:
            left = mid + 1

    return -1


arr = [0, 0, 0, 0, 1, 1, 1, 1]
result = find_divide_index(arr)
if result != -1:
    print(f"Место разделения: Индекс {result}")
else:
    print("-1")