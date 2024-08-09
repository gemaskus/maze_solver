from time import sleep
from cell import Cell
import random

class Maze():
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None):

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

        if seed is not None:
            random.seed(seed)


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
        self._cells[i][j].draw(x1, y1, x2, y2,)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw(self._cells[0][0]._x1,
                               self._cells[0][0]._y1,
                               self._cells[0][0]._x2,
                               self._cells[0][0]._y2,
                               "#d9d9d9")
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._cells[self.num_cols-1][self.num_rows-1].draw(self._cells[self.num_cols-1][self.num_rows-1]._x1,
                                          self._cells[self.num_cols-1][self.num_rows-1]._y1,
                                          self._cells[self.num_cols-1][self.num_rows-1]._x2,
                                          self._cells[self.num_cols-1][self.num_rows-1]._y2,
                                          "#d9d9d9")
        
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            print(f"Checking the indexes from starting node of {i} {j}...")
            next_index_list = []
            if i > 0 and not self._cells[i - 1][j]._visited:
                print("checking left")
                next_index_list.append((i - 1, j))
 
            if i < self.num_cols - 1 and not self._cells[i + 1][j]._visited:
                print("checking right")
                next_index_list.append((i + 1, j))

            if j > 0 and not self._cells[i][j - 1]._visited:
                print("checking up")
                next_index_list.append((i, j - 1))

            if j < self.num_rows - 1 and not self._cells[i][j + 1]._visited:
                print("checking down")
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return
            
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell._visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j]._visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        if ( i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j]._visited):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (i < self.num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j]._visited):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1]._visited):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (j < self.num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1]._visited):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False