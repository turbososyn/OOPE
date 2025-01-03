import sys
import tkinter as tk
from tkinter import messagebox

sys.path.append("./shape")
from editor import Editor

class ShapeEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графічний редактор")

        # Canvas
        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Editor
        self.editor = Editor(self.canvas)

        # Main menu
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        # "Об'єкти" menu
        self.shape_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Об'єкти", menu=self.shape_menu)
        self.shape_menu.add_command(label="Точка", command=lambda: self.editor.set_mode("Point"))
        self.shape_menu.add_command(label="Лінія", command=lambda: self.editor.set_mode("Line"))
        self.shape_menu.add_command(label="Прямокутник", command=lambda: self.editor.set_mode("Rect"))
        self.shape_menu.add_command(label="Еліпс", command=lambda: self.editor.set_mode("Ellipse"))

        # "Файл" menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Новий", command=self.new_file)
        self.file_menu.add_command(label="Вийти", command=self.root.quit)

        # "Довідка" menu
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Довідка", menu=self.help_menu)
        self.help_menu.add_command(label="Про програму", command=self.show_about)

        # Toolbar
        self.toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Add toolbar buttons with drawn icons
        self.add_toolbar_button(self.create_point_icon, "Point", "Режим малювання точки")
        self.add_toolbar_button(self.create_line_icon, "Line", "Режим малювання лінії")
        self.add_toolbar_button(self.create_rect_icon, "Rect", "Режим малювання прямокутника")
        self.add_toolbar_button(self.create_ellipse_icon, "Ellipse", "Режим малювання еліпса")

        self.update_window_title()
        self.canvas.bind("<ButtonPress-1>", self.editor.on_left_button_down)
        self.canvas.bind("<B1-Motion>", self.editor.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.editor.on_left_button_up)

    def add_toolbar_button(self, icon_draw_func, mode, tooltip):
        """Add a button to the toolbar with a drawn icon."""
        icon_canvas = tk.Canvas(self.toolbar, width=24, height=24, bg="white", highlightthickness=0)
        icon_draw_func(icon_canvas)
        icon_canvas.pack(side=tk.LEFT, padx=2, pady=2)
        icon_canvas.bind("<Button-1>", lambda e: self.editor.set_mode(mode))
        self.create_tooltip(icon_canvas, tooltip)

    def create_tooltip(self, widget, text):
        """Create a tooltip for a widget."""
        tooltip = tk.Label(self.root, text=text, bg="yellow", fg="black", relief=tk.SOLID, bd=1)
        tooltip.pack_forget()

        def on_enter(event):
            x, y = event.widget.winfo_pointerxy()
            tooltip.place(x=x, y=y+20)
            tooltip.lift()

        def on_leave(event):
            tooltip.place_forget()

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def create_point_icon(self, canvas):
        canvas.create_oval(10, 10, 14, 14, fill="black")

    def create_line_icon(self, canvas):
        canvas.create_line(4, 20, 20, 4, fill="black")

    def create_rect_icon(self, canvas):
        canvas.create_rectangle(6, 6, 18, 18, outline="black")

    def create_ellipse_icon(self, canvas):
        canvas.create_oval(6, 10, 18, 18, outline="black")

    def update_window_title(self):
        self.root.title(f"Режим вводу: {self.editor.mode}")

    def new_file(self):
        """Очищення полотна для створення нового файлу."""
        self.canvas.delete("all")
        self.editor.reset()

    def show_about(self):
        """Відображення інформації про програму."""
        messagebox.showinfo("Про програму", "Графічний редактор\nВерсія 1.0\nРозроблено у 2025 році")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeEditorApp(root)
    root.mainloop()
