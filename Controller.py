from utils import get_img

class Controller():
    def __init__(self, canv, hero):
        self.canv = canv
        self.hero = hero

    def move_one_forward(self, pos):
        get_img(self.canv, pos=(pos[0] + 30, pos[1]))
        return [pos[0] + 30, pos[1]]
    def move_one_backward(self, pos):
        get_img(self.canv, pos=(pos[0] - 30, pos[1]))
        return [pos[0] - 30, pos[1]]
    def move_one_up(self, pos):
        get_img(self.canv, pos=(pos[0], pos[1] - 30))
        return [pos[0], pos[1] - 30]
    def move_one_down(self, pos):
        get_img(self.canv, pos=(pos[0], pos[1] + 30))
        return [pos[0], pos[1] + 30]
    def fill(self):
        self.canv.create_rectangle(*self.hero.pos, self.hero.pos[0]+30, self.hero.pos[1]+30, fill='red', outline='red')
        get_img(self.canv, self.hero.pos)