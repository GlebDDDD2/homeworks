import random
import string

def generate_password(length, include_digits=True, include_symbols=True, include_uppercase=True):
    characters = []
    if include_digits:
        characters.extend(string.digits)
    if include_symbols:
        characters.extend(string.punctuation)
    if include_uppercase:
        characters.extend(string.ascii_uppercase)

    # Генерация случайного пароля
    password = ''.join(random.choices(characters, k=length))

    return password

def generate_unique_passwords(length, num_passwords, include_digits=True, include_symbols=True, include_uppercase=True):
    passwords = []
    while len(passwords) < num_passwords:
        password = generate_password(length, include_digits, include_symbols, include_uppercase)
        if password not in passwords:
            passwords.append(password)

    return passwords

# Запрос параметров
length = int(input("Введите желаемую длину пароля: "))
num_passwords = int(input("Введите количество паролей для генерации: "))
include_digits = input("Включать ли цифры в пароли? (да/нет): ") == "да"
include_symbols = input("Включать ли символы в пароли? (y/n): ") == "да"
include_uppercase = input("Включать ли заглавные буквы в пароли? (да/нет): ") == "да"

# Генерация уникальных случайных паролей
passwords = generate_unique_passwords(length, num_passwords, include_digits, include_symbols, include_uppercase)

# Вывод паролей
print("Сгенерированные пароли:")
for password in passwords:
    print(password)