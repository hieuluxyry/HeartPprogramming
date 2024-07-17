import turtle
screen = turtle.Screen()
screen.bgcolor("pink")
screen.title("Heart Code")
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(100)

def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

def write_message():
    pen.up()
    pen.setpos(0, -20)
    pen.down()
    pen.color("pink")
    pen.write("Hà Thư , I love you!!!!", align="center", font=("Times New Roman", 15, "bold"))
    pen.penup()

pen.goto(0, -100)
pen.pendown()
draw_heart()
write_message()
pen.hideturtle()
turtle.done()
