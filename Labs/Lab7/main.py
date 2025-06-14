import random
import time

class GuessObjectGame:
    def __init__(self):
        self.objects = [
            ("русалка", "вигаданий", ["Я живу у воді", "Мене не існує в реальному світі", "У мене є риб'ячий хвіст"]),
            ("дерево", "неживий", ["Я не рухаюсь", "У мене є листя", "Я росту з землі"]),
            ("кіт", "живий", ["Я можу муркотіти", "Я люблю молоко", "У мене 4 лапи"]),
            ("робот", "неживий", ["Мене створила людина", "Я можу рухатись", "Я виконую команди"]),
            ("дракон", "вигаданий", ["Я дихаю вогнем", "Я літаю", "Я не існую в реальності"]),
            ("пес", "живий", ["Я — найкращий друг людини", "Я можу гавкати", "Маю нюх кращий за людський"]),
        ]
        self.secret_object = random.choice(self.objects)
        self.max_attempts = 7

    def play(self):
        answer, obj_type, hints = self.secret_object
        print("Вгадай, про що я думаю! Це може бути живий, неживий або вигаданий об'єкт.")
        print(f"Маєш до {self.max_attempts} спроб. Введи свою відповідь:")

        attempts = 0
        hint_index = 0

        while attempts < self.max_attempts:
            user_input = input(f"\nСпроба {attempts + 1}: ").strip().lower()
            if not user_input or len(user_input) < 2 or user_input.isdigit():
                print("Неправильний ввід. Спробуйте ще раз.")
                continue

            attempts += 1
            if user_input == answer:
                print("Вітаю! Ти вгадав!")
                return
            else:
                print("Ні, це не те.")
                if hint_index < len(hints):
                    print(f"Підказка: {hints[hint_index]}")
                    hint_index += 1
                else:
                    print("Підказок більше нема.")

        print(f"\nТи не вгадав. Правильна відповідь: {answer.upper()}. Це був {obj_type} об'єкт.")


class GuessFamousPersonGame:
    def __init__(self):
        self.mystery = {
            "answer": "Тарас Шевченко",
            "hints": [
                "Його ім'я пов'язане з вільнодумством.",
                "Мав важке дитинство і став сиротою дуже рано.",
                "Був заарештований за свою творчість.",
                "Його портрет є на українських грошах."
            ]
        }
        self.victory_messages = [
            "Неймовірно! Ти вгадав!",
            "Вау, в точку! Це саме те!",
            "Ти справжній детектив! Правильна відповідь!",
            "Гаряче! Ідеально! Ти виграв!"
        ]
        self.defeat_messages = [
            "О ні... Не вгадав.",
            "Нажаль, це не те.",
            "Спроби вичерпано. Програш.",
            "Хм, не вдалося розкрити загадку."
        ]

    def play(self):
        print("Вгадай, кого я загадав! Це відома особа.")
        used_hints = set()
        attempts = 5

        while attempts > 0:
            available_hints = [h for i, h in enumerate(self.mystery["hints"]) if i not in used_hints]
            if available_hints and random.choice([True, False]):
                hint = random.choice(available_hints)
                hint_index = self.mystery["hints"].index(hint)
                used_hints.add(hint_index)
                print(f"Підказка: {hint}")

            user_input = input("Хто це, як думаєш? ").strip()
            if not user_input:
                print("Ти нічого не ввів. Спробуй ще.")
                continue

            if user_input.lower() == self.mystery["answer"].lower():
                print(random.choice(self.victory_messages))
                return

            attempts -= 1
            print(f"Ні, це не {user_input}. Залишилось спроб: {attempts}\n")

        time.sleep(random.uniform(0.5, 1.5))
        print(random.choice(self.defeat_messages))
        print(f"Правильна відповідь була: {self.mystery['answer']}")


class AbstractGuessGame:
    def __init__(self):
        self.hidden_targets = {
            "колір": ["синій", "зелений", "червоний"],
            "тварина": ["кіт", "собака", "пінгвін"],
            "число": ["42", "7", "13"],
        }
        self.true_category = random.choice(list(self.hidden_targets.keys()))
        self.true_answer = random.choice(self.hidden_targets[self.true_category])
        self.start_time = time.time()
        self.max_duration = random.randint(20, 40)

    def play(self):
        print("Вітаємо у грі 'Вгадай ЩОСЬ'")
        print("Вибери, що ти хочеш вгадати: 'колір', 'тварина', 'число'")
        player_choice = input("Твій вибір: ").strip().lower()

        if player_choice not in self.hidden_targets:
            print("Хмм... це не зовсім те, що ми очікували... Але добре.")
            possible_answers = ["динозавр", "марс", "42.5", "нічого", "яблуко"]
        else:
            possible_answers = self.hidden_targets[player_choice]

        print("Починаємо гру. Введи свою здогадку.")

        while True:
            guess = input("Ваша здогадка: ").strip().lower()
            if not guess or any(c in guess for c in "!@#$%^&*()[]{}<>?/\\|"):
                print("Схоже, щось пішло не так...")
                continue

            give_real_hint = random.choice([True, False])
            if guess == self.true_answer:
                print("Можливо, ви близько... Або й ні.")
            elif give_real_hint:
                print(f"Це не {guess}, але можливо {random.choice(possible_answers)}")
            else:
                print(f"Підказка: {random.choice(['банан', 'павук', 'мука', 'всесвіт'])}")

            if time.time() - self.start_time > self.max_duration or random.random() < 0.1:
                print("\nЧас вичерпано. Гра завершується...")
                break

        self.subtle_hint()
        print("Гру завершено.")


def main_menu():
    games = {
        "1": ("Вгадай об'єкт", GuessObjectGame),
        "2": ("Вгадай відому особу", GuessFamousPersonGame),
        "3": ("Вгадай ЩОСЬ", AbstractGuessGame)
    }

    while True:
        print("\nОберіть гру:")
        for key, (title, _) in games.items():
            print(f"{key}. {title}")
        print("0. Вийти")

        choice = input("Ваш вибір: ").strip()
        if choice == "0":
            print("До зустрічі!")
            break
        elif choice in games:
            game = games[choice][1]()
            game.play()
        else:
            print("Невідомий вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main_menu()
