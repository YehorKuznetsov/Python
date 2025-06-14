def calculate_cosmic_distance(speed_of_light_fraction, time_years):
    return speed_of_light_fraction * time_years

def calculate_simplified_gravity(mass1, mass2, cosmic_factor=1.0):
    return mass1 * mass2 * cosmic_factor

def calculate_time_dilation_approximation(speed_of_light_fraction, time_seconds):
    if speed_of_light_fraction >= 1:
        raise ValueError("Частка швидкості світла має бути меншою за 1.")
    return time_seconds / (1 - speed_of_light_fraction)

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Помилка: введіть дійсне число.")

def main():
    while True:
        print("1 - Розрахунок космічної відстані")
        print("2 - Гравітаційне взаємодіяння")
        print("3 - Наближення сповільнення часу")
        print("0 - Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            print("\nОбрано: Космічна відстань")
            speed = get_float_input("Введіть частку швидкості світла (від 0 до 1): ")
            while not (0 <= speed <= 1):
                print("Частка має бути між 0 і 1.")
                speed = get_float_input("Спробуйте ще раз: ")
            time = get_float_input("Введіть час у роках: ")
            result = calculate_cosmic_distance(speed, time)
            print(f"Приблизна космічна відстань становить: {result} світлових років.")

        elif choice == "2":
            print("\nОбрано: Спрощена гравітація")
            mass1 = get_float_input("Введіть масу першого об'єкта: ")
            mass2 = get_float_input("Введіть масу другого об'єкта: ")
            cosmic_factor = input("Введіть космічний фактор (або натисніть Enter для значення за замовчуванням 1.0): ")
            if cosmic_factor.strip() == "":
                result = calculate_simplified_gravity(mass1, mass2)
            else:
                try:
                    factor = float(cosmic_factor)
                    result = calculate_simplified_gravity(mass1, mass2, factor)
                except ValueError:
                    print("Недійсний фактор. Використовується значення за замовчуванням 1.0.")
                    result = calculate_simplified_gravity(mass1, mass2)
            print(f"Спрощена гравітаційна взаємодія: {result}")

        elif choice == "3":
            print("\nОбрано: Наближення сповільнення часу")
            speed = get_float_input("Введіть частку швидкості світла (менше 1): ")
            while not (0 <= speed < 1):
                print("Частка має бути в межах від 0 до менше 1.")
                speed = get_float_input("Спробуйте ще раз: ")
            time_sec = get_float_input("Введіть час у секундах: ")
            try:
                result = calculate_time_dilation_approximation(speed, time_sec)
                print(f"Сповільнений час: {result} секунд.")
            except ZeroDivisionError:
                print("Неможливо розрахувати. Частка не повинна дорівнювати 1.")
            except ValueError as e:
                print(f"{e}")

        elif choice == "0":
            print("\nВихід з космічного калькулятора. До нових подорожей Всесвітом!")
            break
        else:
            print("Невірна опція. Будь ласка, оберіть з меню.")

        again = input("\nБажаєте виконати ще один розрахунок? (так/ні): ").strip().lower()
        if again not in ("так", "y", "yes", "т", "1"):
            print("\nДо побачення, космічний досліднику!")
            break

if __name__ == "__main__":
    main()
