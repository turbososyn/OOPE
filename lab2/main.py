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

        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)
        self.shape_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Об'єкти", menu=self.shape_menu)

        self.shape_menu.add_command(label="Точка", command=lambda: self.editor.set_mode("Point"))
        self.shape_menu.add_command(label="Лінія", command=lambda: self.editor.set_mode("Line"))
        self.shape_menu.add_command(label="Прямокутник", command=lambda: self.editor.set_mode("Rect"))
        self.shape_menu.add_command(label="Еліпс", command=lambda: self.editor.set_mode("Ellipse"))

        self.update_window_title()
        self.canvas.bind("<ButtonPress-1>", self.editor.on_left_button_down)
        self.canvas.bind("<B1-Motion>", self.editor.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.editor.on_left_button_up)

    def update_window_title(self):
        self.root.title(f"Режим вводу: {self.editor.mode}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeEditorApp(root)
    root.mainloop()
