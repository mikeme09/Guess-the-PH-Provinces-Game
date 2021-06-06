from turtle import Screen, Turtle
import pandas as pd

turtle = Turtle()
screen = Screen()

screen.setup(width=750, height=1000)
screen.title("Philippine Provinces Game")

image = "Philippines_administrative_map_blank1.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("provinces_ph.csv")
all_province = data["provinces"].to_list()  # converting all the provinces to a List type
guessed_province = []


while len(guessed_province) < len(all_province):

    answer_prov = screen.textinput(title=f"{len(guessed_province)}/{len(all_province)}", prompt="What is the Province Name?").title()

    if answer_prov == "Exit":
        break

    elif answer_prov in all_province:
        guessed_province.append(answer_prov)
        t = Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.provinces == answer_prov]  # getting the x and y coordinate of the selected province.
        t.goto(int(province_data.x), int(province_data.y))  # (_tkinter.TclError: bad screen distance) error if you don't convert it to int() the default is string.
        t.write(province_data.provinces.item())  # answer_prov

        print(f"{province_data.x} \n {province_data.y}\n")