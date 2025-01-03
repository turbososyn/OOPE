from .shape_base import Shape

class Point(Shape):
    """Point shape."""
    def draw(self, canvas):
        canvas.create_oval(self.x1-2, self.y1-2, self.x1+2, self.y1+2, fill="black")

class Line(Shape):
    """Line shape."""
    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")

class Rect(Shape):
    """Rectangle shape."""
    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black")

class Ellipse(Shape):
    """Ellipse shape."""
    def draw(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline="black")

class Segment(Shape):
    """Segment shape, inherited from Line and uses Ellipse for both endpoints."""
    def draw(self, canvas):
        radius = 5  # Радіус кола
        canvas.create_oval(self.x1 - radius, self.y1 - radius, self.x1 + radius, self.y1 + radius, outline="black", fill="black")
        Line(self.x1, self.y1, self.x2, self.y2).draw(canvas)
        canvas.create_oval(self.x2 - radius, self.y2 - radius, self.x2 + radius, self.y2 + radius, outline="black", fill="black")

class Cube(Rect):  # Наслідуємо від Rect, щоб отримати властивості прямокутника
    """Cube shape, inheriting from Rect and using Line for edges."""
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.offset = 20  # Глибина куба

    def draw(self, canvas):
        # Малюємо передню грань як прямокутник, використовуючи метод Rect
        super().draw(canvas)

        # Координати задньої грані
        back_x1 = self.x1 + self.offset
        back_y1 = self.y1 + self.offset
        back_x2 = self.x2 + self.offset
        back_y2 = self.y2 + self.offset

        # Малюємо задню грань як прямокутник
        canvas.create_rectangle(back_x1, back_y1, back_x2, back_y2, outline="black")

        # Малюємо сполучні лінії, використовуючи метод Line
        line1 = Line(self.x1, self.y1, back_x1, back_y1)
        line2 = Line(self.x2, self.y1, back_x2, back_y1)
        line3 = Line(self.x1, self.y2, back_x1, back_y2)
        line4 = Line(self.x2, self.y2, back_x2, back_y2)

        line1.draw(canvas)
        line2.draw(canvas)
        line3.draw(canvas)
        line4.draw(canvas)