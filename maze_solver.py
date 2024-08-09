from graphics import Window

from cell import Cell

from maze import Maze

def main():
    main_window = Window(800, 600)

    num_cols = 10
    num_rows = 10
    m1 = Maze(10,10,num_rows, num_cols, 50, 50, main_window)

    m1._break_entrance_and_exit()
    m1._break_walls_r(0,0)

    m1._reset_cells_visited()

    m1.solve()

    main_window.wait_for_close()


if __name__ == "__main__":
    main()
