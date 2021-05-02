import tkinter
import random
import time

WINDOW_SIZE = 20
RAIN_RATE = 0.1
DROP_INCREASE = 5
RESET_SIZE = 50
CANVAS_SIZE = 1000

if __name__ == '__main__':
    main_window = tkinter.Tk()
    main_window.geometry("1000x1000")
    main_window.title("Rain drops simulation")

    canvas = tkinter.Canvas(main_window)
    canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    coordinate_step = int(CANVAS_SIZE / (WINDOW_SIZE + 1))

    for i in range(0, 1000, coordinate_step):
        canvas.create_line(i, 0, i, 1000)
        canvas.create_line(0, i, 1000, i)

    rain_drops = [[random.randint(1, 4) for j in range(0, 20)] for i in range(0, 20)]

    for i in range(0, 20):
        for j in range(0, 20):
            oval_y = (i+1) * coordinate_step
            oval_x = (j+1) * coordinate_step
            drop_size = rain_drops[i][j] * DROP_INCREASE
            canvas.create_oval(oval_y - drop_size, oval_x - drop_size, oval_y + drop_size, oval_x + drop_size)

    main_window.mainloop()

