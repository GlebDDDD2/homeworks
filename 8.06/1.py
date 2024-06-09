def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [12, -45, 67, -34, 89, -100, 23, -5, 34]
prime_numbers = [num for num in numbers if is_prime(num)]
print("Простые числа:", prime_numbers)