import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        # Ініціалізація головного вікна
        self.root = root
        self.root.title("Калькулятор")              # Назва вікна
        self.root.resizable(False, False)           # Заборона зміни розміру вікна

        self.expression = ""  # Змінна для зберігання введеного виразу

        # Поле введення для відображення виразу та результату
        self.entry = tk.Entry(
            root, font=("Arial", 20), bd=10,
            insertwidth=2, width=22, borderwidth=4,
            justify="right"  # Вирівнювання тексту праворуч
        )
        self.entry.grid(row=0, column=0, columnspan=4)  # Розміщення поля введення у вікні

        # Список кнопок у форматі: (текст, рядок, стовпець [, кількість стовпців])
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)  # Кнопка "=" розтягується на 4 стовпці
        ]

        # Створення і розміщення кнопок на формі
        for (text, row, col, colspan) in [btn if len(btn) == 4 else (*btn, 1) for btn in buttons]:
            button = tk.Button(
                root,
                text=text,  # Текст на кнопці
                padx=20, pady=20,
                font=("Arial", 16),
                command=lambda t=text: self.on_button_click(t)  # Обробка натискання кнопки
            )
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew")  # Розміщення кнопки

    def on_button_click(self, char):
        """Обробка натискань на кнопки калькулятора"""
        if char == "=":
            try:
                result = eval(self.expression)  # Обчислення виразу з використанням eval
                full_expression = f"{self.expression}={result}"  # Формування рядка "вираз=результат"
                self.entry.delete(0, tk.END)  # Очищення поля
                self.entry.insert(tk.END, full_expression)  # Виведення результату
                self.expression = str(result)  # Збереження результату для подальших обчислень
            except ZeroDivisionError:
                # Обробка помилки ділення на нуль
                messagebox.showerror("Помилка", "Ділення на нуль неможливе")
                self.clear_entry()
            except Exception:
                # Обробка будь-яких інших помилок
                messagebox.showerror("Помилка", "Некоректний вираз")
                self.clear_entry()
        elif char == "C":
            # Очищення поля при натисканні кнопки "C"
            self.clear_entry()
        else:
            # Додавання символу до виразу та оновлення поля
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def clear_entry(self):
        """Очищення поля введення та виразу"""
        self.expression = ""
        self.entry.delete(0, tk.END)

# Запуск програми
if __name__ == "__main__":
    root = tk.Tk()          # Створення головного вікна
    calc = Calculator(root) # Ініціалізація калькулятора
    root.mainloop()         # Запуск головного циклу програми
