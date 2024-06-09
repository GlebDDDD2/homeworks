class Task:
    def __init__(self, name):
        self.name = name
        self.status = "Бэклог"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return
        print(f"Задача '{task_name}' не найдена.")

    def move_task(self, task_name, new_status):
        for task in self.tasks:
            if task.name == task_name:
                task.status = new_status
                return
        print(f"Задача '{task_name}' не найдена.")

    def display_tasks(self):
        for status in ["Бэклог", "В работе", "Выполнено"]:
            print(f"{status}:")
            for task in self.tasks:
                if task.status == status:
                    print(task.name)

    def mark_task_as_done(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.status = "Выполнено"
                return
        print(f"Задача '{task_name}' не найдена.")


def main():
    manager = TaskManager()

    while True:
        print("Выберите действие:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Переместить задачу")
        print("4. Отметить задачу как выполненную")
        print("5. Просмотреть задачи")
        print("6. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            name = input("Введите название задачи: ")
            task = Task(name)
            manager.add_task(task)
            print(f"Задача '{name}' добавлена.")
        elif choice == "2":
            name = input("Введите название задачи для удаления: ")
            manager.delete_task(name)
        elif choice == "3":
            name = input("Введите название задачи для перемещения: ")
            new_status = input("Введите новый статус (Бэклог, В работе, Выполнено): ")
            manager.move_task(name, new_status)
        elif choice == "4":
            name = input("Введите название задачи для отметки как выполненной: ")
            manager.mark_task_as_done(name)
        elif choice == "5":
            manager.display_tasks()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()