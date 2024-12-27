from shape import Shape

class Point(Shape):
    """Клас для об'єкта точка."""
    def draw(self, canvas):
        canvas.create_oval(self.x1-2, self.y1-2, self.x1+2, self.y1+2, fill="black")

class Line(Shape):
    """Клас для об'єкта лінія."""
    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")

class Rect(Shape):
    """Клас для об'єкта прямокутник."""
    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black")

class Ellipse(Shape):
    """Клас для об'єкта еліпс."""
    def draw(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline="black")
