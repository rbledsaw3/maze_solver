from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c_0 = Cell(win)
    c_0.has_right_wall = False
    c_0.draw(50, 50, 100, 100)

    c_1 = Cell(win)
    c_1.has_left_wall = False
    c_1.has_bottom_wall = False
    c_1.draw(100, 50, 150, 100)

    c_0.draw_move(c_1)

    c_2 = Cell(win)
    c_2.has_top_wall = False
    c_2.has_right_wall = False
    c_2.draw(100, 100, 150, 150)

    c_1.draw_move(c_2)

    c_3 = Cell(win)
    c_3.has_left_wall = False
    c_3.draw(150, 100, 200, 150)

    c_2.draw_move(c_3, True)

    win.wait_for_close()

main()
