import tkinter as tk
import tkinter.scrolledtext
from utils import get_img
from tkinter import *
from Hero import Hero
from CodeScene import CodeScene
from Console import Console
from time import sleep
WINDOW_SIZE_X = 30 * 30
WINDOW_SIZE_Y = 20 * 30

from Wall import Wall
walls = {

    'horizontal' : [],
    'vertical' : []

}
class MapScene:
    is_Create_mode = False
    is_repl_mode = False
    curr_pos = [300, 300]

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text='редактировать код', width = 25, command = self.new_window)
        self.button2 = tk.Button(self.frame, text='поставить стены', width=25, command = self.get_diff_mode)
        self.button3 = Button(self.frame, text='сброс', width=25, command=self.from_start)
        self.button4 = Button(self.frame, text='переместить', width=25, command=self.get_repl_mode)

        self.button1.pack()
        self.button2.pack()
        self.button4.pack()
        self.frame.pack()
        self.conf_canvas()
        self.button3.pack()
        hero = get_img(self.canv, pos=(300, 420))
        self.hero = Hero(self.canv, hero)
        self.cons = Console(self.hero)
        self.cons.txt.pack(side='bottom')
        self.hero.console = self.cons

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = CodeScene(self.newWindow, self.hero)

    def generate(self):
        for i in range(1, 41):
            for j in range(1, 41):
                self.canv.create_line(30 * i, 0, 30 * i, WINDOW_SIZE_Y)
                self.canv.create_line(0, i * 30, WINDOW_SIZE_X, 30 * i)

    def get_diff_mode(self):
        if not self.is_Create_mode:
            self.create_button = tk.Button(self.frame, text='quit', width=10, command=self.quit_from_edit_mode)
            self.create_button.pack()
            self.is_Create_mode = True

    def create_wall(self, pos=[24, 49, 16, 298]):
        mywal = Wall(self.canv, pos)
        for i in mywal.get_coords()[0]:
            if not mywal.get_coords()[1]:
                walls['horizontal'].append(i)
            else:
                walls['vertical'].append(i)
        print(walls)
    loc_pos = []

    def click(self, event):
        self.loc_pos.append(event.x)
        self.loc_pos.append(event.y)
        if len(self.loc_pos) == 4:
            if self.is_Create_mode:
                self.create_wall(self.loc_pos)
                self.loc_pos = []
        if self.is_repl_mode:
            ex, ey = event.x, event.y
            ex += 30 - ex % 30 if ex % 30 > 15 else -(ex % 30)
            ey += 30 - ey % 30 if ey % 30 > 15 else -(ey % 30)
            print(ex, ey)
            self.hero.pos = ex, ey
            self.hero.first_pos = ex, ey
            get_img(self.canv, self.hero.pos)
        if len(self.loc_pos) > 4: self.loc_pos = []

    def quit_from_edit_mode(self):
        self.create_button.destroy()
        self.is_Create_mode = False

    def from_start(self):
        self.conf_canvas()

    def conf_canvas(self, pos=(0, 0)):
        try:
            self.canv.destroy()
        except: pass
        self.canv = tk.Canvas(self.master, width=WINDOW_SIZE_X, height=WINDOW_SIZE_Y, bg='white')
        self.generate()
        self.canv.pack()
        hero = get_img(self.canv, pos=pos)
        self.hero = Hero(self.canv, hero)
        self.canv.bind('<Button-1>', lambda x: self.click(x))

    def get_repl_mode(self):
        self.is_repl_mode = True
        self.buttonq = Button(self.frame, width=10, text='quit', command=self.quit_from_repl_mode)
        self.buttonq.pack()
    def quit_from_repl_mode(self):
        self.is_repl_mode = False
        self.buttonq.destroy()
