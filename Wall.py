import tkinter as tk

class Wall:
    def __init__(self, canv, pos):
        self.is_hor = False
        self.canv = canv
        for i in range(len(pos)):
            print(pos[i] % 30)
            if (pos[i] % 30) >= 15:
                pos[i] += 30 - (pos[i] % 30)
            else:
                pos[i] -= pos[i] % 30
        if pos[0] == pos[2] or pos[1] == pos[3] and not (pos[1] == pos[2] == pos[3] == pos[0]):
            positions = []
            print(pos[0], pos[2])
            self.canv.create_line(pos[0], pos[1], pos[2], pos[3], fill='green', width=4)
            if pos[0] == pos[2]:
                self.is_hor = True
                for i in range(min([pos[1], pos[3]]), max([pos[1], pos[3]]), 30):
                    positions.append([pos[0], i])
            else:
                for i in range(min([pos[0], pos[2]]), max([pos[0], pos[2]]), 30):
                    positions.append([i, pos[1]])
                    print([pos[1], i])
            self.pos = positions
        else:
            self.pos = None
    def get_coords(self):
        return self.pos, self.is_hor