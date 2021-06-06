from turtle import Screen, Turtle
import pandas as pd
import openpyxl

screen = Screen()
turtle = Turtle()


screen.setup(width=750, height=1000)
screen.title("Philippine Provinces Game")

image = "Philippines_administrative_map_blank1.gif"
screen.addshape(image)

turtle.shape(image)

x_click = 0
y_click = 0


def get_coor():
    screen.onscreenclick(modify_variable)


def modify_variable(raw_x, raw_y):
    global x_click
    global y_click

    x_click = int(raw_x // 1)
    y_click = int(raw_y // 1)

    file = pd.DataFrame([x_click, y_click], index=["x", "y"])

    # print(x_click)
    # print(y_click)
    print(file)


get_coor()
screen.mainloop()
