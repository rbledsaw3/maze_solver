from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c_0 = Cell(win)
    c_0.has_left_wall = False
    c_0.draw(50, 50, 100, 100)

    c_1 = Cell(win)
    c_1.has_right_wall = False
    c_1.draw(125, 125, 200, 200)

    c_1 = Cell(win)
    c_1.has_bottom_wall = False
    c_1.draw(255, 255, 250, 250)

    c_3 = Cell(win)
    c_3.has_top_wall = False
    c_3.draw(300, 300, 500, 500)

    win.wait_for_close()

main()
