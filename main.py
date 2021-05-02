import tkinter
import random
import time

WINDOW_SIZE = 20
RAIN_RATE = 0.1
DROP_INCREASE = 5
RESET_SIZE = 50
CANVAS_SIZE = 1000


def draw_drops(canvas, rain_drops):
    canvas.delete("all")
    for i in range(0, WINDOW_SIZE):
        for j in range(0, WINDOW_SIZE):
            if random.random() <= RAIN_RATE:
                rain_drops[i][j] += 1

    coordinate_step = int(CANVAS_SIZE / (WINDOW_SIZE + 1))

    for i in range(0, CANVAS_SIZE, coordinate_step):
        canvas.create_line(i, 0, i, CANVAS_SIZE)
        canvas.create_line(0, i, CANVAS_SIZE, i)

    for i in range(0, WINDOW_SIZE):
        for j in range(0, WINDOW_SIZE):
            oval_y = (i + 1) * coordinate_step
            oval_x = (j + 1) * coordinate_step
            drop_size = rain_drops[i][j] * DROP_INCREASE
            canvas.create_oval(oval_y - drop_size, oval_x - drop_size, oval_y + drop_size, oval_x + drop_size)

    canvas.after(500, lambda: draw_drops(canvas, rain_drops))


if __name__ == '__main__':
    main_window = tkinter.Tk()
    main_window.geometry("1000x1000")
    main_window.title("Rain drops simulation")

    canvas = tkinter.Canvas(main_window)
    canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    rain_drops = [[0 for j in range(0, WINDOW_SIZE)] for i in range(0, WINDOW_SIZE)]
    draw_drops(canvas, rain_drops)
    main_window.mainloop()
