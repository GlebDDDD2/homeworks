def find_change(coins, amount):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        while amount >= coin:
            change.append(coin)
            amount -= coin
        return change


products = {
    "молоко": 20,
    "хлеб": 30,
    "кофе": 15,
    "сигареты": 50,
    "вода": 90,
    "сахар": 80,
    "соль": 45,
    "лотерейный билет": 10,
}
print("Список доступных продкутов: ")
for product in products:
    print(product)

product = input("\nВыберите товар: ").lower()
if product in products:
    price = products[product]
    payment = int(input("Введите сумму: "))

    if payment >= price:
        change_due = payment - price
        coins = [1, 5, 7, 10, 15]
        change_coins = find_change(coins, change_due)

        print(f"Сдача: {change_due}p")
        print("Минимальное количество монет для сдачи:")
        for coin in change_coins:
            print(coin, end="р ")
        if payment == price:
            print("Без сдачи")
    else:
        print("Недостаточно средств")
else:
    print("Товар отсутствует ")