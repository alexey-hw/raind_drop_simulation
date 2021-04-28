from tkinter import *
import random
import time

WINDOW_SIZE = 20
RAIN_RATE = 0.1
DROP_INCREASE = 5
RESET_SIZE = 50

if __name__ == '__main__':
    main_window = Tk()
    main_window.geometry("1000x1000")
    main_window.title("Rain drops simulation")

    canvas = Canvas(main_window)
    canvas.pack(fill=BOTH, expand=YES)

    for i in range(0, 1000, 50):
        canvas.create_line(i, 0, i, 1000)
        canvas.create_line(0, i, 1000, i)

    main_window.mainloop()

