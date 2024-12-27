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
