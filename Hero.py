from Controller import Controller
from Parser import Parser
from VarSystem import VarSystem

class Hero:
    first_pos = [300, 420]
    def __init__(self, canv, img):
        self.pos = self.first_pos
        self.canv = canv
        self.controller = Controller(self.canv, self)
        self.Parser = Parser(self)
        self.vars = VarSystem()
        self.console = None
        self.img = img