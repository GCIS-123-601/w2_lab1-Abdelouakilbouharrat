import turtle
def turtle_code():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50,40)
    turtle.down()
    turtle.home()
    turtle.circle(25)
def turtle_state():
    penstate=turtle.isdown()
    facing=turtle.heading()
    xcoor=turtle.xcor()
    ycoor=turtle.ycor()
    print("Is the pen down?",penstate)
    print("Turtle is facing",facing)
    print("X coordinate",xcoor, "Y coordinate",ycoor)

def main():
    turtle_state()
    turtle_code()
    turtle_state()
    input("press key to continue")
main()    