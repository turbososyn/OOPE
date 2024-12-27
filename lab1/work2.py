import tkinter as tk

def open_second_dialog():
    # Закриття першого вікна та відкриття другого
    def on_back():
        second_window.destroy()
        open_first_dialog()

    def on_yes():
        print("Ви натиснули 'Так'.")
        second_window.destroy()
        root.quit()  # Завершує виконання програми після закриття другого вікна

    def on_cancel():
        second_window.destroy()
        root.quit()  # Завершує виконання програми після закриття другого вікна

    # Створення другого діалогового вікна
    second_window = tk.Toplevel()
    second_window.title("Діалог 2")
    second_window.geometry("400x200")  # Розмір вікна

    # Кнопки у другому вікні
    button_back = tk.Button(second_window, text="< Назад", command=on_back)
    button_back.pack(side="left", padx=20, pady=40)

    button_yes = tk.Button(second_window, text="Так", command=on_yes)
    button_yes.pack(side="left", padx=20)

    button_cancel = tk.Button(second_window, text="Відміна", command=on_cancel)
    button_cancel.pack(side="right", padx=20)

def open_first_dialog():
    # Створення першого діалогового вікна
    def on_next():
        first_window.destroy()
        open_second_dialog()

    def on_cancel():
        first_window.destroy()
        root.quit()  # Завершує виконання програми після закриття першого вікна

    first_window = tk.Toplevel()
    first_window.title("Діалог 1")
    first_window.geometry("400x200")  # Розмір вікна

    # Кнопки у першому вікні
    button_next = tk.Button(first_window, text="Далі >", command=on_next)
    button_next.pack(side="left", padx=40, pady=40)

    button_cancel = tk.Button(first_window, text="Відміна", command=on_cancel)
    button_cancel.pack(side="right", padx=40)

# Створення основного вікна, яке приховується
root = tk.Tk()
root.withdraw()  # Приховуємо головне вікно, щоб воно не з'являлося

open_first_dialog()

# Запуск головного циклу Tkinter
root.mainloop()
