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

class Cube(Rect):
    """Cube shape.""" 
    def draw(self, canvas):
        # Draw the front face (rectangle)
        super().draw(canvas)

        # Draw the back face (offset)
        offset = 10
        canvas.create_rectangle(self.x1 + offset, self.y1 - offset, self.x2 + offset, self.y2 - offset, outline="black")

        # Connect the corners of the front and back faces to form the cube
        canvas.create_line(self.x1, self.y1, self.x1 + offset, self.y1 - offset, fill="black")
        canvas.create_line(self.x2, self.y1, self.x2 + offset, self.y1 - offset, fill="black")
        canvas.create_line(self.x1, self.y2, self.x1 + offset, self.y2 - offset, fill="black")
        canvas.create_line(self.x2, self.y2, self.x2 + offset, self.y2 - offset, fill="black")


class Segment(Shape):
    """Segment shape that consists of a line and a circle at the endpoint."""
    def draw(self, canvas):
        # Draw the line
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")

        # Draw the circle at the endpoint
        radius = 5  # Radius of the circle
        canvas.create_oval(self.x2 - radius, self.y2 - radius, self.x2 + radius, self.y2 + radius, outline="black", fill="black")

