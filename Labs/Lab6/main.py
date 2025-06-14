import random

#Завдання 1: Гра "Скарбниця короля"
print("=== Гра 1: Скарбниця короля ===")
try:
    coins = random.randint(1, 1000)  # Генеруємо випадкову кількість монет
    print(f"Ви знайшли {coins} золотих монет!")
    team = input("Скільки людей у вашій команді? ")
    team = int(team)  # Може викликати ValueError
    coins_per_person = coins // team  # Може викликати ZeroDivisionError
    print(f"Кожен отримав по {coins_per_person} монет.")
except ValueError:
    print("Помилка: введено нечислове значення для кількості людей!")
except ZeroDivisionError:
    print("Помилка: не можна ділити на нуль!")
finally:
    print("Пригоди тривають!\n")

#Завдання 2: Гра "Код сейфу з таймером"
print("=== Гра 2: Код сейфу з таймером ===")
code = random.randint(100, 999)  # Генеруємо тризначний код
attempts = 5

while attempts > 0:
    try:
        guess = input("Введіть код сейфу (тризначне число): ")
        guess = int(guess)
        if 100<=guess <= 999:
            if guess == code:
                print("Ви зламали сейф! Вітаємо!")
                break
            elif guess < code:
                print("Код більший.")
            else:
                print("Код менший.")
        else: print("Код має бути з 3х чисел")
    except ValueError:
        print("Помилка: потрібно вводити лише числа!")
    finally:
        attempts -= 1
        print(f"Спроб залишилось: {attempts}\n")

if attempts == 0:
    print(f"Ви не зламали сейф. Правильний код був: {code}\n")

#Завдання 3: Розширена гра "Камінь-ножиці-папір-ящірка-Спок"
print("=== Гра 3: Камінь-ножиці-папір-ящірка-Спок ===")
options = ["камінь", "ножиці", "папір", "ящірка", "спок"]
wins = {
    "камінь": ["ножиці", "ящірка"],
    "ножиці": ["папір", "ящірка"],
    "папір": ["камінь", "спок"],
    "ящірка": ["папір", "спок"],
    "спок": ["ножиці", "камінь"]
}

try:
    user_choice = input("Зробіть вибір (камінь, ножиці, папір, ящірка, спок): ").lower()
    if user_choice not in options:
        raise ValueError("Некоректний вибір!")

    computer_choice = random.choice(options)
    print(f"Комп'ютер обрав: {computer_choice}")

    if user_choice == computer_choice:
        print("Нічия!")
    elif computer_choice in wins[user_choice]:
        print("Ви перемогли!")
    else:
        print("Ви програли!")

except ValueError as e:
    print(f"Помилка: {e} Спробуйте ще раз.")

finally:
    print("Гра завершена.\n")

#Завдання 4: Система нарахування бонусів із множниками
print("=== Гра 4: Бонусна система ===")
try:
    points = int(input("Введіть кількість набраних очок (0–100): "))
    if points < 0 or points > 100:
        raise ValueError("Кількість очок повинна бути в межах від 0 до 100")

    if points < 50:
        rating = "Початківець"
        multiplier = 1
    elif points < 70:
        rating = "Срібний гравець"
        multiplier = 1.5
    elif points < 90:
        rating = "Золотий гравець"
        multiplier = 2
    else:
        rating = "Платиновий гравець"
        multiplier = 3

    total = points * multiplier
    print(f"Ваш рейтинг: {rating}! Ви отримали {total} балів (множник ×{multiplier})!\n")
except ValueError as ve:
    print(f"Некоректне введення! {ve}\n")

#Завдання 5: Гра "Втеча з острова піратів"
print("=== Гра 5: Втеча з острова піратів ===")
try:
    # Етап 1: Перетин річки
    print("Перетин річки")
    wood = input("Скільки одиниць деревини ви зібрали (1-10)? ")
    wood = int(wood)
    if wood < 3:
        print("Деревини замало, пліт затонув! Гру завершено.")
    else:
        # Етап 2: Втеча від піратів
        print("Втеча від піратів")
        escape = input("Оберіть спосіб втечі (бігти / сховатися / битися): ")
        if escape not in ["бігти", "сховатися", "битися"]:
            raise ValueError("Такого варіанту немає, пірати вас спіймали! Гру завершено.")
        else:
            # Етап 3: Відкриття скрині
            print("Відкриття скрині")
            secret_code = random.randint(10, 99)
            try:
                guess_code = int(input("Введіть секретний код (двозначне число): "))
                if guess_code == secret_code:
                    print("Скарб ваш, ви врятовані!")
                else:
                    print("Неправильний код, скриня вибухнула! Гру завершено.")
            except ValueError:
                print("Це не число!")
except ValueError as e:
    print(e)
except Exception as e:
    print("Невідома помилка:", e)
finally:
    print("Гра завершена. Дякуємо за участь у пригоді!")
