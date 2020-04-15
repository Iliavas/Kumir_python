import math
import re
from utils import split_string
from math import *
from tkinter import END
from time import sleep

CHARCH = [
    '+',
    '-',
    '*',
    '/',
]


to_replace = {

    'не' : 'not',
    'и' : 'and',
    'или' : 'or'

}

class Parser:
    def __init__(self, hero):
        for i in dir(math):
            CHARCH.append(i)
        self.hero = hero

    def parse(self, string):
        counter = 0
        is_if = False
        text = string.split('\n')
        for i in text:
            i = self.insert_nl(i)
            for j in i.split():
                if j == 'если':
                    self.if_parse(i, string.split('\n')[counter+1:], self.get_spaces(i))
                    is_if = True
                elif j == 'пока':
                    text = self.while_parse(string.split('\n')[counter+1:], i, self.get_spaces(i), text, counter)
                elif j == ':=':
                    self.parse_equal(i)
                    break
                elif j == 'вывод':
                    self.printing(i)
                    break
                elif j == 'цел':
                    self.get_var(i.split('цел')[-1])
                    break
                elif j == 'ввод':
                    self.parsing_input(i.split('ввод')[-1])
                    break
                else:
                    self.parsing_comands(i)
            counter += 1
            if is_if: break

    def solving(self, string):
        from MapScene import walls
        for i in enumerate(list(self.hero.vars.print_var())):
            try:
                it = re.finditer('[^A-z](' + i[1] + ')[^A-z]', string)
                for i in it:
                    string = split_string(string, i.start() + 1, str(self.hero.vars.get_var(''.join(list(i.group())[1:-1]))), i.end() - 1)
            except: pass
        for i in CHARCH:
            try:
                string = re.sub(i, ' ' + i + ' ', string)
            except: pass
        s = string.split()
        f = False
        Hor_dir = False
        for i in enumerate(s):
            if i[1] == 'сверху':
                f = True
                Hor_dir = True
                s[i[0]] = str([self.hero.pos[0], self.hero.pos[1]])
            elif i[1] == 'справа':
                f = True
                s[i[0]] = str([self.hero.pos[0] + 30, self.hero.pos[1]])
            elif i[1] == 'слева':
                f = True
                s[i[0]] = str([self.hero.pos[0], self.hero.pos[1]])
            elif i[1] == 'снизу':
                f = True
                Hor_dir = True
                s[i[0]] = str([self.hero.pos[0], self.hero.pos[1] + 30])
            elif f == True:
                f = False
                if i[1] == 'не':
                    s[i[0]] = str(' not in ')
                else:
                    s.insert(i[0], ' in ')
        for i in enumerate(s):
            if i[1] == 'стена':
                if Hor_dir:
                    s[i[0]] = str(walls['horizontal'])
                else:
                    s[i[0]] = str(walls['vertical'])
        string = ' '.join(s)
        print(string)
        st = ''
        if '\n' in string:
            return '\n'
        try:
            if string[0] == ' ':
                st += ' '
        except: pass
        for i in string.split():
            if i in list(self.hero.vars.print_var()):
                st += str(self.hero.vars.get_var(i))
            elif i in list(to_replace.keys()):
                st += to_replace.get(i)
            else:
                st += i
            st += ' '

        try:
            return str(eval(st))
        except:
            return st

    def parse_equal(self, i):
        res = i.split(':=')[1]
        for j in i.split(':=')[1].split(' '):
            if j in CHARCH:
                res = self.solving(i.split(':=')[1])
                break
        self.hero.vars.set_var(i.split(':=')[0], res)

    def printing(self, string):
        res = ''
        q = []
        c = 0
        for i in string + ' ':
            if i == '"':
                q.append(c)
                if len(q) == 2:
                    self.hero.console.write(string[q[0]+1:q[1]])
            if len(q) >= 2:
                q = []
            c += 1
        string = re.sub(r'".*"', '', string)
        a = string.split('вывод')[-1]
        a = re.split(r',', a)
        for j in a:
            res += self.solving(j)
        self.hero.console.write(res)

    def parsing_comands(self, string):
        for j in string.split(' '):
            if j == 'вправо':
                self.hero.pos = self.hero.controller.move_one_forward(self.hero.pos)
                print(self.hero.pos)
            elif j == 'вниз':
                self.hero.pos = self.hero.controller.move_one_down(self.hero.pos)
            elif j == 'влево':
                self.hero.pos = self.hero.controller.move_one_backward(self.hero.pos)
            elif j == 'вверх':
                self.hero.pos = self.hero.controller.move_one_up(self.hero.pos)
            elif j == 'закрасить':
                self.hero.controller.fill()
                print('asldf')
            #sleep(0.5)

    def parsing_input(self, string):
        f = False
        string = re.sub(' ', '', string)
        string = string.split(',')
        if string[0][0] == '"':
            a = string[0]
            del string[0]
            self.printing(a)
        buffer = string[0]
        for i in string[1:]:
            if i == 'нс':
                self.printing('\n')
                self.parsing_input(buffer)
                f = True
            buffer = i
        if f: return 0
        self.hero.console.curr_val = string
        self.hero.console.pre_string = self.hero.console.get_string()
        self.hero.vars.set_var(string[-1], 'Non-Recognised')
        while self.hero.vars.get_var(string[-1]) == 'Non-Recognised':
            sleep(1)

    def insert_nl(self, string):
        nl = re.sub('нс', '\n', string)
        return nl

    def get_var(self, string):
        a = re.sub(' ', '', string)
        a = a.split(',')
        for i in a:
            self.hero.vars.set_var(i, '')

    def get_spaces(self, string):
        return len(re.split('\S', string)[0])

    def if_parse(self, string, program, spaces=2):
        string = string.split()
        del string[0], string[-1]
        boolean = self.solving(' '.join(string))
        if boolean == 'False':
            for i in range(len(program)):
                try:
                    del program[0]
                    if 'кц' in program[0] and self.get_spaces(program[0]) == spaces:
                        break
                except: pass
        if boolean == 'True':
            min_, max_ = 0, 0
            for i in range(len(program)):
                if 'иначе' in program[i] and spaces == self.get_spaces(program[i]):
                    min_ = i
                elif 'кц' in program[i] and spaces == self.get_spaces(program[i]) and min_:
                    max_ = i
            program[min_: max_] = ''
        self.parse('\n'.join(program))

    def while_parse(self, program, s, spaces, text, counter):
        end = 0
        for i in enumerate(program):
            if 'кц' in i[1] and self.get_spaces(i[1]) == spaces:
                program = program[:i[0]]
                break
            end += 1
        while True:
            self.parse('\n'.join(program))
            if self.solving(' '.join(s.split()[1:-1])) == 'False': break
        for i in range(counter, counter+end):
            del text[i]
        print(text)
        print(counter, end)
        return text