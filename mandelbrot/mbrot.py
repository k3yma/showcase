import numpy as np
import cmath
import tkinter
from tkinter import ttk, messagebox, PhotoImage, filedialog

resolution = 800
minx = miny = -2.0
maxx = maxy = 2.0
iterations = 100


def get_colour(col_val):
    cols = [
        "#421e0f",
        "#250726",
        "#19071a",
        "#09012f",
        "#040449",
        "#000764",
        "#0c2c8a",
        "#1855b1",
        "#397dd1",
        "#86b5e5",
        "#d3ecf8",
        "#f1e9bf",
        "#f8c95f",
        "#ffaa00",
        "#cc8000",
        "#995700",
        "#6a3403",
    ]
    q = col_val % len(cols)

    if col_val == iterations:
        return "#000000"
    else:
        return cols[q]


def calc_value(c):
    n = z = 0

    while abs(z) <= 2 and (n := n + 1) < iterations:
        z = z**2 + c
    return get_colour(n)


def get_array():
    return np.array(
        [
            [
                calc_value(
                    complex(
                        minx + (x * (maxx - minx) / resolution),
                        miny + (y * (maxy - miny) / resolution),
                    )
                )
                for x in range(resolution)
            ]
            for y in range(resolution)
        ]
    )


def draw_mbrot():
    img.put(get_array().tolist())


def reset():
    global minx, miny, maxx, maxy
    minx = miny = -2.0
    maxx = maxy = 2.0
    draw_mbrot()


def button_pressed(event):
    global rect_draw_x, rect_draw_y, rect

    rect_draw_x = event.x
    rect_draw_y = event.y

    rect = c.create_rectangle(
        rect_draw_x, rect_draw_y, rect_draw_x, rect_draw_y, outline="red"
    )


def button_move(event):
    global rect_draw_x1
    global rect_draw_y1
    rect_draw_x1 = event.x
    rect_draw_y1 = rect_draw_y + (rect_draw_x1 - rect_draw_x)  # Force a square
    c.coords(rect, rect_draw_x, rect_draw_y, rect_draw_x1, rect_draw_y1)


def redefine_scale(min_x, max_x, min_y, max_y):
    global minx, miny, maxx, maxy

    x_min_old = minx
    x_max_old = maxx
    y_min_old = miny
    y_max_old = maxy

    minx = x_min_old + (min_x * ((x_max_old - x_min_old) / resolution))
    maxx = x_min_old + (max_x * ((x_max_old - x_min_old) / resolution))
    miny = y_min_old + (min_y * ((y_max_old - y_min_old) / resolution))
    maxy = y_min_old + (max_y * ((y_max_old - y_min_old) / resolution))


def button_released(event):
    c.delete(rect)
    redefine_scale(
        min(rect_draw_x1, rect_draw_x),
        max(rect_draw_x1, rect_draw_x),
        min(rect_draw_y1, rect_draw_y),
        max(rect_draw_y1, rect_draw_y),
    )
    draw_mbrot()


def save():
    img.write("output.png", format="png")
    print("Saved to output.png")


if __name__ == "__main__":
    rect_draw_x = None
    rect_draw_y = None
    rect_draw_x1 = None
    rect_draw_y1 = None
    rect = None

    # Set up the browser GUI
    top = tkinter.Tk()
    top.title("Mandelbrot")
    top.geometry(f"{resolution}x{resolution}")
    menubar = tkinter.Menu(top)
    menubar.add_command(label="Save", command=save)
    menubar.add_command(label="Reset", command=reset)
    menubar.add_command(label="Quit", command=exit)
    top.config(menu=menubar)
    c = tkinter.Canvas(top, width=resolution, height=resolution, cursor="cross")
    c.pack()
    img = PhotoImage(width=resolution, height=resolution)
    c.create_image((resolution // 2, resolution // 2), image=img, state="normal")

    # Mouse bindings
    c.bind("<ButtonPress-1>", button_pressed)
    c.bind("<B1-Motion>", button_move)
    c.bind("<ButtonRelease-1>", button_released)
    draw_mbrot()
    top.mainloop()
