from PIL import Image, ImageTk
import threading


def get_img(canv, pos=(0, 0)):
    img = Image.open('s.png')
    img = img.resize((27, 27))
    canv.image = ImageTk.PhotoImage(img)
    canv.create_image(*pos, image=canv.image, anchor='nw')

def basic(x):
    print(x)

def start_th(func, args):
    t = threading.Thread(target=func, args=args)
    t.start()

def split_string(string, start, substring, end):
    start_string = string[:start]
    start_string += substring
    start_string += string[end:]

    return start_string