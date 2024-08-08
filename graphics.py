from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):

        self.root_widget = Tk()
        self.root_widget.title('Maze Solver!')
        self.is_running = False

        self.canvas = Canvas(self.root_widget,
                             height=height,
                             width=width)

        self.canvas.pack()

        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.is_running = True
        while (self.is_running is True):
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color) -> None:
        canvas.create_line(self.point1.x,
                           self.point1.y,
                           self.point2.x,
                           self.point2.y,
                           fill=fill_color,
                           width=2)