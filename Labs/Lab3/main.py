import random

def generate_secret_code():
    digits = list(range(10))  # Список цифр від 0 до 9
    random.shuffle(digits)  # Перемішуємо для отримання випадкової послідовності
    return ''.join(map(str, digits[:4]))  # Беремо перші 4 цифри і перетворюємо їх у рядок


def analyze_guess(secret_code, user_guess):
    bulls = sum(1 for i in range(4) if user_guess[i] == secret_code[i])  # Підрахунок биків
    cows = sum(1 for digit in user_guess if digit in secret_code) - bulls  # Підрахунок корів
    return bulls, cows


def is_valid_guess(user_guess):
    """
    Перевіряє, чи введене число є 4-значним і складається з унікальних цифр.
    """
    return len(user_guess) == 4 and user_guess.isdigit() and len(set(user_guess)) == 4 #Перевіряє, чи введене число є 4-значним і складається з унікальних цифр.


def main():
    secret_code = generate_secret_code()  # Генерується секретний код
    print("Вгадай 4-значний код з унікальних цифр.")

    attempts = 0  # Лічильник спроб
    while True:
        user_guess = input("Введіть вашу спробу: ")

        if not is_valid_guess(user_guess):
            print("Некоректний ввід! Введіть 4 різні цифри.")
            continue

        attempts += 1
        bulls, cows = analyze_guess(secret_code, user_guess)
        print(f"Бики: {bulls}, Корови: {cows}")

        if bulls == 4:
            print(f"Ви відгадали код {secret_code} за {attempts} спроб!")
            break


if __name__ == "__main__":
    main()