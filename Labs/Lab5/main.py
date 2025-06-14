import random

def game_1_simple_code():
    """Гра 1: Вгадування числа від 1 до 10 з підказками 'більше' або 'менше'"""
    secret_number = random.randint(1, 10)  # Генеруємо випадкове число
    print("\n[Гра 1] Вгадай число від 1 до 10!")

    while True:  # Нескінченний цикл до вгадування
        try:
            guess = int(input("Твоє число: "))  # Користувач вводить число
            if guess < secret_number:
                print("Більше.")  # Якщо введене число менше
            elif guess > secret_number:
                print("Менше.")  # Якщо введене число більше
            else:
                print("Вітаю! Ти вгадав число.")  # Успішне вгадування
                break
        except ValueError:
            print("Введи ціле число.")  # Обробка неправильного вводу

def game_2_code_with_hints():
    """Гра 2: Підказки залежно від близькості до секретного числа"""
    secret_number = random.randint(1, 50)
    print("\n[Гра 2] Вгадай число від 1 до 50!")

    while True:
        try:
            guess = int(input("Твоя спроба: "))
            diff = abs(secret_number - guess)  # Різниця між вгадуванням і правильним числом
            if guess == secret_number:
                print("Вітаю! Ти вгадав!")
                break
            elif diff <= 3:
                print("Дуже близько!")  # Підказка, якщо дуже близько
            elif diff <= 10:
                print("Близько.")  # Якщо не дуже близько, але в межах 10
            else:
                print("Далеко.")  # Якщо далеко від правильного числа
        except ValueError:
            print("Введи ціле число.")

def game_3_no_mistakes():
    """Гра 3: Тільки 3 спроби на вгадування числа від 1 до 20"""
    secret_number = random.randint(1, 20)
    attempts = 3  # Кількість спроб
    print("\n[Гра 3] Вгадай число від 1 до 20. У тебе лише 3 спроби")

    while attempts > 0:
        try:
            guess = int(input("Спроба: "))
            if guess == secret_number:
                print("Ти вгадав!")
                break
            else:
                attempts -= 1  # Зменшуємо кількість спроб
                if attempts > 0:
                    print(f"Невірно. Залишилось спроб: {attempts}")
                else:
                    print(f"Гру завершено. Правильне число: {secret_number}")
        except ValueError:
            print("Введи ціле число.")

def game_4_secret_pin():
    """Гра 4: Вгадування 4-значного PIN-коду з підказками по цифрам"""

    # Внутрішня функція для генерації випадкового PIN-коду з 4 цифр
    def generate_pin():
        return ''.join(str(random.randint(0, 9)) for _ in range(4))

    pin = generate_pin()  # Генеруємо PIN
    attempts = 5
    print("\n[Гра 4] Вгадай 4-значний PIN-код. У тебе 5 спроб.")

    while attempts > 0:
        guess = input("Введи PIN: ")
        # Перевірка формату вводу
        if not guess.isdigit() or len(guess) != 4:
            print("Невірний формат. Введи 4 цифри.")
            continue

        if guess == pin:
            print("Вітаю! Ти вгадав PIN!")
            break
        else:
            # Підрахунок правильних цифр на правильних позиціях
            correct_digits = sum(1 for i in range(4) if guess[i] == pin[i])
            attempts -= 1
            print(f"Правильно на місці: {correct_digits}. Залишилось спроб: {attempts}")
            if attempts == 0:
                print(f"Спроби вичерпано. PIN був: {pin}")

def game_5_color_code():
    """Гра 5: Вгадай колір за 3 спроби з підказкою про групу кольору"""
    colors = ["червоний", "синій", "зелений", "жовтий", "фіолетовий"]
    warm_colors = {"червоний", "жовтий"}  # Теплі кольори
    cold_colors = {"синій", "зелений", "фіолетовий"}  # Холодні кольори
    secret_color = random.choice(colors)  # Випадковий вибір кольору
    attempts = 3

    print("\n[Гра 5] Вгадай колір. Доступні:")
    print(", ".join(colors))

    while attempts > 0:
        guess = input("Твоя спроба: ").strip().lower()
        if guess not in colors:
            print("Цей колір не входить у список.")
            continue
        if guess == secret_color:
            print("Ти вгадав!")
            break
        else:
            # Підказка по групі кольору (теплий/холодний)
            group = "теплих" if secret_color in warm_colors else "холодних"
            attempts -= 1
            print(f"Невірно. Загаданий колір із групи {group}. Залишилось спроб: {attempts}")
            if attempts == 0:
                print(f"Гру завершено. Колір був: {secret_color}")

def main():
    """Головне меню для вибору гри"""
    while True:
        print("\nГРА 'ТАЄМНИЙ КОД' ")
        print("1. Простий код")
        print("2. Код із підказками")
        print("3. Код без права на помилку")
        print("4. Таємний PIN-код")
        print("5. Кольоровий код")
        print("0. Вийти")
        choice = input("Оберіть гру (0-5): ")

        # Викликаємо відповідну гру за вибором користувача
        if choice == "1":
            game_1_simple_code()
        elif choice == "2":
            game_2_code_with_hints()
        elif choice == "3":
            game_3_no_mistakes()
        elif choice == "4":
            game_4_secret_pin()
        elif choice == "5":
            game_5_color_code()
        elif choice == "0":
            print("До зустрічі!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
