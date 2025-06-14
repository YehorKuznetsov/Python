def task1(input_str):
    vowels = "аеиіоуяюєїАЕИІОУЯЮЄЇaeiouAEIOU"
    vowel_count = 0
    vowel_list = []
    vowel_freq = {}

    for char in input_str:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)
            vowel_freq[char] = vowel_freq.get(char, 0) + 1

    unique_vowels = sorted(set(vowel_list))
    return {
        "vowel_count": vowel_count,
        "unique_vowels": unique_vowels,
        "vowel_frequency": vowel_freq
    }


def task2(list1, list2):
    combined = list1 + list2
    if not combined:
        return []
    unique_sorted = sorted(set(combined))
    return unique_sorted


def task3(text):
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1

    repeated_chars = [char for char, count in char_freq.items() if count > 1]
    return {
        "all_characters_frequency": char_freq,
        "repeated_characters": sorted(repeated_chars)
    }


def input_numbers(prompt):
    while True:
        try:
            data = input(prompt)
            if not data:
                return []
            return [float(x) if '.' in x or 'e' in x.lower() else int(x)
                    for x in data.split()]
        except ValueError:
            print("Помилка! Введіть числа, розділені пробілами. Спробуйте ще раз.")


def main():
    print("=" * 50)
    print("Завдання 1: Аналіз голосних літер у тексті")
    input_str = input("Введіть текст для аналізу: ")

    print("\n" + "=" * 50)
    print("Завдання 2: Обробка числових списків")
    print("Введіть перший список чисел (розділіть пробілами):")
    list1 = input_numbers("> ")
    print("Введіть другий список чисел (розділіть пробілами):")
    list2 = input_numbers("> ")

    print("\n" + "=" * 50)
    print("Завдання 3: Аналіз частоти символів")
    text = input("Введіть текст для аналізу символів: ")

    # Виконання завдань
    result1 = task1(input_str)
    result2 = task2(list1, list2)
    result3 = task3(text)

    # Виведення результатів
    print("\n" + "=" * 50)
    print("Результати завдання 1:")
    print(f"Загальна кількість голосних літер: {result1['vowel_count']}")
    print(f"Унікальні голосні літери: {', '.join(result1['unique_vowels'])}")
    print("Частота голосних літер:")
    for char, count in result1['vowel_frequency'].items():
        print(f"  '{char}': {count}")

    print("\n" + "=" * 50)
    print("Результати завдання 2:")
    if result2:
        print("Об'єднаний відсортований список без дублікатів:")
        print(result2)
    else:
        print("Отримано порожній список (обидва вхідні списки були порожніми)")

    print("\n" + "=" * 50)
    print("Результати завдання 3:")
    print(f"Усього унікальних символів: {len(result3['all_characters_frequency'])}")
    print(f"Символи, що повторюються (> 1 разу): {', '.join(result3['repeated_characters'])}")
    print("\nПовна частота символів:")
    for char, count in sorted(result3['all_characters_frequency'].items()):
        char_repr = repr(char)[1:-1]  # Для коректного відображення спецсимволів
        print(f"  '{char_repr}': {count}")
    print("=" * 50)


if __name__ == "__main__":
    main()