from graphics import Line, Point


class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        tl_point = Point(self._x1, self._y1)
        tr_point = Point(self._x2, self._y1)
        bl_point = Point(self._x1, self._y2)
        br_point = Point(self._x2, self._y2)

        l_line = Line(tl_point, bl_point)
        t_line = Line(tl_point, tr_point)
        r_line = Line(tr_point, br_point)
        b_line = Line(bl_point, br_point)

        if self.has_left_wall:
            self._win.draw_line(l_line, "black")
        if self.has_top_wall:
            self._win.draw_line(t_line, "black")
        if self.has_right_wall:
            self._win.draw_line(r_line, "black")
        if self.has_bottom_wall:
            self._win.draw_line(b_line, "black")

    def draw_move(self, to_cell, undo=False):
        center_x1 = (self._x1 + self._x2)/2
        center_y1 = (self._y1 + self._y2)/2
        center_x2 = (to_cell._x1+to_cell._x2)/2
        center_y2 = (to_cell._y1+to_cell._y2)/2

        color = None
        if undo is False:
            color = "red"
        elif undo is True:
            color = "gray"

        self._win.draw_line(Line(Point(center_x1, center_y1),
                                 Point(center_x2, center_y2)), color)
