import sys
import tkinter as tk

sys.path.append("./shape")
from editor import Editor

class ShapeEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графічний редактор")

        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()

        self.editor = Editor(self.canvas)

        # Головне меню
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        # Меню "Об'єкти"
        self.shape_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Об'єкти", menu=self.shape_menu)
        self.shape_menu.add_command(label="Точка", command=lambda: self.editor.set_mode("Point"))
        self.shape_menu.add_command(label="Лінія", command=lambda: self.editor.set_mode("Line"))
        self.shape_menu.add_command(label="Прямокутник", command=lambda: self.editor.set_mode("Rect"))
        self.shape_menu.add_command(label="Еліпс", command=lambda: self.editor.set_mode("Ellipse"))

        # Меню "Файл"
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Новий", command=self.new_file)
        self.file_menu.add_command(label="Вийти", command=self.root.quit)

        # Меню "Довідка"
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Довідка", menu=self.help_menu)
        self.help_menu.add_command(label="Про програму", command=self.show_about)

        self.update_window_title()
        self.canvas.bind("<ButtonPress-1>", self.editor.on_left_button_down)
        self.canvas.bind("<B1-Motion>", self.editor.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.editor.on_left_button_up)

    def update_window_title(self):
        self.root.title(f"Режим вводу: {self.editor.mode}")

    def new_file(self):
        """Очищення полотна для створення нового файлу."""
        self.canvas.delete("all")
        self.editor.reset()

    def show_about(self):
        """Відображення інформації про програму."""
        tk.messagebox.showinfo("Про програму", "Графічний редактор\nВерсія 1.0\nРозроблено у 2025 році")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeEditorApp(root)
    root.mainloop()
