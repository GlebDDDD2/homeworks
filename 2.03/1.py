import random

class Questions:
    def __init__(self):
        self.questions = []

    def add_question(self, question, answer):
        self.questions.append((question, answer))
        print("Вопрос успешно добавлен!")

    def show_random_question(self):
        if self.questions:
            random_question = random.choice(self.questions)
            user_answer = input(f"Вопрос: {random_question[0]}\nОтвет: ").strip()
            if user_answer.lower() == random_question[1].lower():
                print("Правильно!")
            else:
                print(f"Неправильно. Правильный ответ: {random_question[1]}")
        else:
            print("Список вопросов пуст.")

app = Questions()

while True:
    print("Меню:")
    print("1. Добавить вопрос")
    print("2. Показать случайный вопрос")
    print("3. Выход")

    choice = input("Введите номер действия (1-3): ")

    if choice == "1":
        question = input("Введите вопрос: ")
        answer = input("Введите ответ: ")
        app.add_question(question, answer)
    elif choice == "2":
        app.show_random_question()
    elif choice == "3":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, введите номер от 1 до 3.")