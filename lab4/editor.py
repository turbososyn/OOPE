from shape.shape_types import Point, Line, Rect, Ellipse, Cube, Segment

class Editor:
    """Handles drawing and event processing."""
    def __init__(self, canvas):
        self.canvas = canvas
        self.shapes = []
        self.mode = "Point"
        self.current_shape = None

    def set_mode(self, mode):
        self.mode = mode

    def on_left_button_down(self, event):
        self.x1, self.y1 = event.x, event.y
        self.x2, self.y2 = event.x, event.y

    def on_mouse_move(self, event):
        self.x2, self.y2 = event.x, event.y
        self.canvas.delete("temp")
        self.draw_temp()

    def on_left_button_up(self, event):
        self.x2, self.y2 = event.x, event.y
        self.add_shape()
        self.canvas.delete("temp")
        self.draw_all_shapes()

    def draw_temp(self):
        """Draw temporary shape with dashed outline."""
        if self.mode == "Point":
            self.canvas.create_oval(
                self.x1 - 2, self.y1 - 2, self.x2 + 2, self.y2 + 2,
                outline="black", dash=(4, 2), tags="temp", fill=""  # Додано fill=""
            )
        elif self.mode == "Line":
            self.canvas.create_line(
                self.x1, self.y1, self.x2, self.y2,
                fill="", outline="black", dash=(4, 2), tags="temp"
            )
        elif self.mode == "Rect":
            self.canvas.create_rectangle(
                self.x1, self.y1, self.x2, self.y2,
                outline="black", dash=(4, 2), tags="temp"
            )
        elif self.mode == "Ellipse":
            self.canvas.create_oval(
                self.x1, self.y1, self.x2, self.y2,
                outline="black", dash=(4, 2), tags="temp"
            )
        elif self.mode == "Cube":
            offset = 10
            # Передня грань
            self.canvas.create_rectangle(
                self.x1, self.y1, self.x2, self.y2,
                outline="black", dash=(4, 2), tags="temp"
            )
            # Задня грань
            self.canvas.create_rectangle(
                self.x1 + offset, self.y1 + offset, self.x2 + offset, self.y2 + offset,
                outline="black", dash=(4, 2), tags="temp"
            )
            # Сполучні лінії
            self.canvas.create_line(self.x1, self.y1, self.x1 + offset, self.y1 + offset, fill="", outline="black", dash=(4, 2), tags="temp")
            self.canvas.create_line(self.x2, self.y1, self.x2 + offset, self.y1 + offset, fill="", outline="black", dash=(4, 2), tags="temp")
            self.canvas.create_line(self.x1, self.y2, self.x1 + offset, self.y2 + offset, fill="", outline="black", dash=(4, 2), tags="temp")
            self.canvas.create_line(self.x2, self.y2, self.x2 + offset, self.y2 + offset, fill="", outline="black", dash=(4, 2), tags="temp")
        elif self.mode == "Segment":
            radius = 2
            # Коло на початку
            self.canvas.create_oval(
                self.x1 - radius, self.y1 - radius, self.x1 + radius, self.y1 + radius,
                outline="black", dash=(4, 2), tags="temp", fill="" # Додано fill=""
            )
            # Лінія
            self.canvas.create_line(
                self.x1, self.y1, self.x2, self.y2,
                fill="", outline="black", dash=(4, 2), tags="temp"
            )
            # Коло на кінці
            self.canvas.create_oval(
                self.x2 - radius, self.y2 - radius, self.x2 + radius, self.y2 + radius,
                outline="black", dash=(4, 2), tags="temp", fill="" # Додано fill=""
            )

    def add_shape(self):
        """Add the final shape to the shapes list."""
        shape = None

        if self.mode == "Point":
            shape = Point(self.x1, self.y1, self.x2, self.y2)
        elif self.mode == "Line":
            shape = Line(self.x1, self.y1, self.x2, self.y2)
        elif self.mode == "Rect":
            shape = Rect(self.x1, self.y1, self.x2, self.y2)
        elif self.mode == "Ellipse":
            shape = Ellipse(self.x1, self.y1, self.x2, self.y2)
        elif self.mode == "Cube":
            shape = Cube(self.x1, self.y1, self.x2, self.y2)
        elif self.mode == "Segment":
            shape = Segment(self.x1, self.y1, self.x2, self.y2)

        if shape:
            self.shapes.append(shape)
        else:
            print(f"Error: Invalid mode {self.mode}")

    def draw_all_shapes(self):
        """Redraw all the shapes on the canvas."""
        self.canvas.delete("all")
        for shape in self.shapes:
            shape.draw(self.canvas)