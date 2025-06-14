import requests

api = "https://api.breakingbadquotes.xyz/v1/quotes"
try:
    response = requests.get(api)
    response.raise_for_status()
    quote = response.json()[0].get('quote')
    print(quote)

    with open("quote.txt", "w", encoding="utf-8") as file:
        file.write(quote)
except requests.exceptions.RequestException as e:
    print(f"Помилка отримання цитати: {e}")
except Exception as e:
    print(f"Невідома помилка: {e}")

try:
    with open("quote.txt", "r", encoding="utf-8") as file:
        words = file.read().split()
        print(f"У цьому текстовому файлі: {len(words)} слів.")
except FileNotFoundError:
    print("Файл quote.txt не знайдено.")
except Exception as e:
    print(f"Помилка при читанні файлу: {e}")
