
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Предмет '{item.name}' добавлен в инвентарь.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Предмет '{item.name}' удалён из инвентаря.")
                return
        print(f"Предмет '{item_name}' не найден в инвентаре.")

    def display_inventory(self):
        if not self.items:
            print("Инвентарь пуст.")
            return
        print("Инвентарь:")
        for item in self.items:
            print(f"Название: {item.name} - Описание: {item.description}")

inventory = Inventory()

while True:
    print("Меню:")
    print("1. Добавить предмет в инвентарь")
    print("2. Удалить предмет из инвентаря")
    print("3. Просмотреть инвентарь")
    print("4. Выход")

    choice = input("Введите номер действия (1-4): ")

    if choice == "1":
        name = input("Введите название предмета: ")
        description = input("Введите описание предмета: ")
        item = Item(name, description)
        inventory.add_item(item)
    elif choice == "2":
        name = input("Введите название предмета, который хотите удалить: ")
        inventory.remove_item(name)
    elif choice == "3":
        inventory.display_inventory()
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, введите номер от 1 до 4.")