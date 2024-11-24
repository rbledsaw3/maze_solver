from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.data = Canvas(self.root, width=width, height=height)
        self.data.pack(fill=BOTH, expand=1)
        self.data.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.data.running = True
        while self.data.running:
            self.redraw()

    def close(self):
        self.data.running = False
