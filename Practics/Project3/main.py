# Завдання 1: Перетворення рядка в число та зворотне перетворення
def task1():
    try:
        number_str = input("Завдання 1: Введіть число: ")
        number = float(number_str)  # Перетворюємо рядок в число
        result = number + 5  # Додаємо 5 до числа
        print(f"Результат: {str(result)}")  # Виводимо результат
    except ValueError:  # Обробляємо помилку, якщо введено не число
        print("Невірний формат числа.")

# Завдання 2: Арифметичні операції з введеними даними
def task2():
    try:
        num1_str = input("Завдання 2: Введіть перше число: ")
        num2_str = input("Введіть друге число: ")

        num1 = float(num1_str)  # Перетворюємо перше число в тип float
        num2 = float(num2_str)  # Перетворюємо друге число в тип float

        sum_result = num1 + num2  # Обчислюємо суму
        diff_result = num1 - num2  # Обчислюємо різницю
        prod_result = num1 * num2  # Обчислюємо добуток
        div_result = num1 / num2 if num2 != 0 else "Неможливо поділити на нуль"  # Перевіряємо на поділ на нуль

        # Виводимо результати
        print(f"Сума: {sum_result}")
        print(f"Різниця: {diff_result}")
        print(f"Добуток: {prod_result}")
        print(f"Частка: {div_result}")
    except ValueError:  # Обробляємо помилку, якщо введено не число
        print("Невірний формат числа.")
    except ZeroDivisionError:  # Обробляємо помилку, якщо спробували поділити на нуль
        print("Помилка: спроба поділу на нуль.")

# Завдання 3: Конвертація списку рядків у список чисел
def task3():
    try:
        numbers_str = input("Завдання 3: Введіть числа через кому: ")
        numbers_list = [float(num) for num in numbers_str.split(",")]  # Розділяємо рядок за комами та перетворюємо на числа

        sum_result = sum(numbers_list)  # Обчислюємо суму чисел
        average_result = sum_result / len(numbers_list) if numbers_list else 0  # Обчислюємо середнє значення

        # Виводимо результати
        print(f"Сума чисел: {sum_result}")
        print(f"Середнє значення: {average_result}")
    except ValueError:  # Обробляємо помилку, якщо введено не число
        print("Невірний формат числа.")

# Завдання 4: Форматування числових значень
def task4():
    try:
        number = float(input("Завдання 4: Введіть число з плаваючою комою: "))
        formatted_number = f"{number:.2f}"  # Форматуємо число з двома знаками після коми
        print(f"Число з двома десятковими знаками: {formatted_number}")
    except ValueError:  # Обробляємо помилку, якщо введено не число

        print("Невірний формат числа.")

# Головна програма
def main():
    while True:  # Нескінченний цикл для повторного виконання завдань
        print("Оберіть завдання:")
        print("1. Перетворення рядка в число та зворотне перетворення")
        print("2. Арифметичні операції з введеними даними")
        print("3. Конвертація списку рядків у список чисел")
        print("4. Форматування числових значень")
        print("0. Вийти")  # Додаємо можливість вийти з програми

        task_choice = input("Введіть номер завдання (1-4) або 0 для виходу: ")

        if task_choice == '1':
            task1()
        elif task_choice == '2':
            task2()
        elif task_choice == '3':
            task3()
        elif task_choice == '4':
            task4()
        elif task_choice == '0':  # Якщо вибрано 0, виходимо з програми
            print("Вихід з програми.")
            break  # Виходимо з циклу
        else:
            print("Некоректний вибір!")  # Якщо введено некоректний номер завдання

if __name__ == "__main__":
    main()