from .shape_base import Shape

class Point(Shape):
    """Point shape."""
    def draw(self, canvas):
        canvas.create_oval(self.x1-2, self.y1-2, self.x1+2, self.y1+2, fill="black")

class Line(Shape):
    def draw(self, canvas):
        """Draw the line using current coordinates."""
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")

    def draw_line_with_coords(self, canvas, x1, y1, x2, y2, dash=None):
        """Draw a line directly with the provided coordinates, optionally dashed."""
        canvas.create_line(x1, y1, x2, y2, fill="black", dash=dash)


class Rect(Shape):
    """Rectangle shape."""
    def draw(self, canvas):
        """Draw the rectangle using current coordinates."""
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black")

    def draw_rect_with_coords(self, canvas, x1, y1, x2, y2, dash=None):
        """Draw a rectangle directly with the provided coordinates, optionally dashed."""
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", dash=dash)


class Ellipse(Shape):
    """Ellipse shape."""
    def draw(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline="black")

class Segment(Shape):
    """Segment shape, inherited from Line and uses Ellipse for both endpoints."""
    def draw(self, canvas):
        radius = 5  # Circle radius
        canvas.create_oval(self.x1 - radius, self.y1 - radius, self.x1 + radius, self.y1 + radius, outline="black", fill="black")
        line = Line(self.x1, self.y1, self.x2, self.y2)
        line.draw_line(canvas)
        canvas.create_oval(self.x2 - radius, self.y2 - radius, self.x2 + radius, self.y2 + radius, outline="black", fill="black")

class Cube(Rect, Line):
    """Cube shape, inheriting from Rect and Line."""
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.offset = 20  # Depth of the cube

    def draw(self, canvas):
        # Draw the front face using Rect's method
        self.draw_rect_with_coords(canvas, self.x1, self.y1, self.x2, self.y2)

        # Coordinates for the back face
        back_x1 = self.x1 + self.offset
        back_y1 = self.y1 + self.offset
        back_x2 = self.x2 + self.offset
        back_y2 = self.y2 + self.offset

        # Draw the back face using the new method
        self.draw_rect_with_coords(canvas, back_x1, back_y1, back_x2, back_y2)

        # Draw connecting edges using Line's new method
        self.draw_line_with_coords(canvas, self.x1, self.y1, back_x1, back_y1)
        self.draw_line_with_coords(canvas, self.x2, self.y1, back_x2, back_y1)
        self.draw_line_with_coords(canvas, self.x1, self.y2, back_x1, back_y2)
        self.draw_line_with_coords(canvas, self.x2, self.y2, back_x2, back_y2)
