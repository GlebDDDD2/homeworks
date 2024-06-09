available_coins = {1: 100, 5: 100, 7: 100, 10: 100, 15: 100}


def calculate_change(price, payment):
    change_due = payment - price
    coins = sorted(available_coins.keys(), reverse=True)
    change_coins = []

    for coin in coins:
        while change_due >= coin and available_coins[coin] > 0:
            change_due -= coin
            change_coins.append(coin)
            available_coins[coin] -= 1

    if change_due > 0:
        print("Недостаточно монет для сдачи.")
    else:
        return change_coins


def update_available_coins(change_coins):
    for coin in change_coins:
        available_coins[coin] += 1


products = {
    "молоко": 20,
    "хлеб": 15,
}
print("Доступные продукты и цены:")
for product, price in products.items():
    print(f"{product}: {price}р")

product = input("\nВыберите продукт: ").lower()
if product in products:
    price = products[product]
    payment = int(input("Введите сумму оплаты в рублях: "))

    if payment >= price:
        change_coins = calculate_change(price, payment)
        if change_coins:
            print(f"Сдача: {sum(change_coins)}р. Монеты для сдачи: {', '.join(map(str, change_coins))}")
            update_available_coins(change_coins)
            print("Обновленное количество монет в кассе:")
            for coin, quantity in available_coins.items():
                print(f"{coin}р: {quantity}")
    else:
        print("Недостаточно средств")
else:
    print("Товар отсутствует")