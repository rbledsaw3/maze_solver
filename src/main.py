from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(100, 100), Point(200, 200))
    win.draw_line(line, "black")
    win.wait_for_close()

main()
