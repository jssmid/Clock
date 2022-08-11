import datetime
import turtle

#screen
x = turtle.Screen()
x.title("A NORMAL CLOCK AND THE DATE")
x.bgcolor("black")
x.setup(width=500, height=400)
x.tracer(0)

#Time
t = turtle.Turtle()
t.hideturtle()
t.color("white")
a = t.write("{}".format(datetime.datetime.now().time().replace(microsecond=0)), align="center", font=("Courier",50,"normal"))


#Date
d = turtle.Turtle()
d.hideturtle()
d.goto(-200,-100)
d.color("white")
b = d.write("{}".format(datetime.datetime.now().date()))

#FUNCTIONS

def time():
    if a != datetime.datetime.now().time().replace(microsecond=0):
        t.clear()
        return t.write("{}".format(datetime.datetime.now().time().replace(microsecond=0)), align="center", font=("Courier",50,"normal"))


def date():
    if b != datetime.datetime.now().date():
        d.clear()
        return d.write("{}".format(datetime.datetime.now().date()), align="left", font=("Courier",50,"normal"))


#MAINLOOP

while True:
    try:
        x.update()
        time()
        date()
    except:
        break