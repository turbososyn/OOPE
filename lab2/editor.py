from shape.shape_types import Point, Line, Rect, Ellipse

class Editor:
    """Клас редактора, який відповідає за малювання фігур та обробку подій."""
    def __init__(self, canvas):
        self.canvas = canvas
        self.shapes = []  # Список для збереження малюнків
        self.mode = "Point"  # Початковий режим малювання
        self.current_shape = None

    def set_mode(self, mode):
        """Змінити поточний режим малювання."""
        self.mode = mode

    def on_left_button_down(self, event):
        """Обробка натискання лівої кнопки миші."""
        self.x1, self.y1 = event.x, event.y
        self.x2, self.y2 = event.x, event.y

    def on_mouse_move(self, event):
        """Обробка руху миші."""
        self.x2, self.y2 = event.x, event.y
        self.canvas.delete("temp")  # Видалити попередній "гумовий слід"
        self.draw_temp()  # Малюємо тимчасову фігуру

    def on_left_button_up(self, event):
        """Обробка відпускання лівої кнопки миші."""
        self.x2, self.y2 = event.x, event.y
        self.add_shape()  # Додати об'єкт у масив
        self.canvas.delete("temp")  # Очистити "гумовий слід"
        self.draw_all_shapes()  # Перемалювати всі об'єкти

    def draw_temp(self):
        """Малювання тимчасової фігури (під час руху миші)."""
        if self.mode == "Point":
            self.canvas.create_oval(self.x1-2, self.y1-2, self.x2+2, self.y2+2, fill="black", tags="temp")
        elif self.mode == "Line":
            self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black", tags="temp")
        elif self.mode == "Rect":
            self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black", tags="temp")
        elif self.mode == "Ellipse":
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline="black", tags="temp")

    def add_shape(self):
        """Додавання об'єкта в масив в залежності від поточного режиму."""
        if self.mode == "Point":
            shape = Point(self.x1, self.y1, self.x2, self.y2)
        elif self.mode == "Line":
            shape = Line(self.x1, self.y1, self.x2, self.y2)
        elif self.mode == "Rect":
            shape = Rect(self.x1, self.y1, self.x2, self.y2)
        elif self.mode == "Ellipse":
            shape = Ellipse(self.x1, self.y1, self.x2, self.y2)
        self.shapes.append(shape)

    def draw_all_shapes(self):
        """Перемалювання всіх об'єктів з масиву."""
        for shape in self.shapes:
            shape.draw(self.canvas)
