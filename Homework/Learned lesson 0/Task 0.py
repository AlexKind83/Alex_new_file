from tkinter import *

root = Tk()
root.title('PythonWay Snake')
root.mainloop()


class Snake(object):
    def __init__(self, segments):
        self.segments = segments
        self.mapping = {'down': (0, 1),
                        'up': (0, -1),
                        'left': (-1, 0),
                        'right': (1, 0)}
        self.vector = self.mapping['right']

    def move(self):
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)

        c.coords(self.segments[-1].instance,
            x1 + self.vector[0] * SEG_SIZE,
            y1 + self.vector[1] * SEG_SIZE,
            x2 + self.vector[0] * SEG_SIZE,
            y2 + self.vector[1] * SEG_SIZE,)

    def change_direction(self, event):
        if event.keys in self.mapping:
            self.vector = self.mapping[event.keys]

    def add_segment(self):
        last_seg = c.coords(self.segments[0].instance)

        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE

        self.segments.insert(0, segment(x, y))


segments = [segment(SEG_SIZE, SEG_SIZE),
            segment(SEG_SIZE * 2, SEG_SIZE),
            segment(SEG_SIZE * 3, SEG_SIZE)]

s = Snake(segments)


