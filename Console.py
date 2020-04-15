import tkinter.scrolledtext as s
from tkinter import END
import re
from utils import basic
MEETING = "Welcome to my application I hope you enjoy it. For any questions you can write me on my email: il.vsl0110@gmail.com \n"

class Console:
    def __init__(self, hero):
        self.curr_val = []
        self.pre_string = None
        self.hero = hero
        self.txt = s.ScrolledText(width=100, height=15)
        self.txt.insert(1.0, MEETING)
        self.txt.bind('<Return>', lambda x: self.get_vals(x, self.curr_val if (len(self.curr_val) > 0) else None))
    def write(self, text):
        self.txt.insert(float(len(self.txt.get('1.0', END))), text)

    def get_string(self):
        return self.txt.get('1.0', END)

    def get_vals(self, event, names):
        if names != None:
            a = self.txt.get('1.0', END)
            data = []
            for i in a.split():
                if not i in self.pre_string:
                    data.append(i)
            for i in range(len(data)):
                self.hero.vars.set_var(names[i], data[i])
            self.curr_val = []
        else:
            a = self.txt.get('1.0', END).split('\n')[-2]
            if a == 'cls':
                self.txt.delete('1.0', END)
    def destroy(self):
        self.txt.destroy()