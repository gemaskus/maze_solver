import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):

        num_cols = 10
        num_rows = 10
        win = Window(800, 600)

        m1 = Maze(10,10,num_rows, num_cols, 50, 50, win)

        m1._break_entrance_and_exit()

        self.assertNotEqual(win, None)

        self.assertEqual(len(m1._cells), num_cols,)

        self.assertEqual(len(m1._cells[0]), num_rows,)

if __name__ == "__main__":
    unittest.main()
