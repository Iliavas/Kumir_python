from utils import get_img
from tkinter import scrolledtext
import tkinter as tk
from tkinter import *
from utils import start_th

TEMPLATE = "алг а1 \n нач \n  \n кц"

class CodeScene:
    s = ''
    def __init__(self, master, hero):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.txt = scrolledtext.ScrolledText(master, width=30, height=30)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.do_button = tk.Button(self.frame, text='run code', width = 10, command=lambda : start_th(self.get_text, ()))
        self.quitButton.pack()
        self.do_button.pack()
        self.txt.insert('1.0', TEMPLATE)
        self.txt.pack()
        self.frame.pack()
        self.hero = hero
    def close_windows(self):
        self.master.destroy()
    def get_text(self):
        self.hero.canv.pack()
        get_img(self.hero.canv, pos=self.hero.first_pos)
        self.hero.pos = self.hero.first_pos
        self.s = self.txt.get("1.0", END)
        self.hero.Parser.parse(self.s)