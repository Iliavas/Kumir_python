import tkinter as tk
from MapScene import MapScene



def main():

    root = tk.Tk()
    app = MapScene(root)
    root.mainloop()

if __name__ == '__main__':
    main()
