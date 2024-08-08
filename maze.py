from cell import Cell
from time import sleep


class Maze():
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None):

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for i in range(self.num_rows)] for i in range(self.num_cols)]

        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        col = i
        row = j
        x1 = self.x1+col*self.cell_size_x
        y1 = self.y1+row*self.cell_size_y
        x2 = x1+self.cell_size_x
        y2 = y1+self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw(self._cells[0][0]._x1,
                               self._cells[0][0]._y1,
                               self._cells[0][0]._x2,
                               self._cells[0][0]._y2)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._cells[self.num_cols-1].draw(self._cells[self.num_cols-1][self.num_rows-1]._x1,
                                          self._cells[self.num_cols-1][self.num_rows-1]._y1,
                                          self._cells[self.num_cols-1][self.num_rows-1]._x2,
                                          self._cells[self.num_cols-1][self.num_rows-1]._y2,
                                          "white")
        
