import tkinter as tk
from tkinter import messagebox

# Функція для відкриття діалогового вікна
def open_dialog():
    def on_ok():
        # Отримуємо значення з повзунка
        selected_value = scale.get()
        # Відображаємо число у головному вікні
        label.config(text=f"Вибране число: {selected_value}")
        dialog_window.destroy()

    def on_cancel():
        dialog_window.destroy()

    # Створюємо нове вікно для діалогу
    dialog_window = tk.Toplevel(root)
    dialog_window.title("Вибір числа")
    dialog_window.geometry("400x200")  # Збільшене розмір вікна

    # Додаємо горизонтальний скрол-бар
    scale = tk.Scale(dialog_window, from_=1, to=100, orient='horizontal', length=300)
    scale.pack(padx=20, pady=20)

    # Кнопки [Так] і [Відміна]
    button_yes = tk.Button(dialog_window, text="Так", command=on_ok)
    button_yes.pack(side="left", padx=40)

    button_no = tk.Button(dialog_window, text="Відміна", command=on_cancel)
    button_no.pack(side="right", padx=40)

# Створюємо основне вікно
root = tk.Tk()
root.title("Головне вікно")
root.geometry("500x300")  # Збільшене розмір вікна

# Кнопка для відкриття діалогу
open_dialog_button = tk.Button(root, text="Відкрити діалог", command=open_dialog)
open_dialog_button.pack(pady=40)

# Мітка для відображення вибраного числа
label = tk.Label(root, text="Вибране число: ", font=('Arial', 14))
label.pack(pady=40)

# Запуск головного циклу
root.mainloop()
