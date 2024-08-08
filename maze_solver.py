from graphics import Window

from cell import Cell

def main():
    main_window = Window(800, 600)
    # point1 = Point(2, 2)
    # point2 = Point(50, 50)
    # line = Line(point1, point2)

    # main_window.draw_line(line, "black")

    cell1 = Cell(main_window)
    cell2 = Cell(main_window)

    cell1.has_right_wall = False
    cell2.has_left_wall = False

    cell1.draw(50, 50, 100, 100)

    cell2.draw(100, 50, 150, 100)

    cell1.draw_move(cell2)

    main_window.wait_for_close()


if __name__ == "__main__":
    main()

