
import turtle

screen=turtle.Screen()
screen.title("Clock Turtle")
screen.bgcolor("lightgreen")

turtle1= turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("blue")

def drawClock():
    turtle1.stamp()
    turtle1.penup()
    turtle1.forward(150)
    for i in range(12):
        turtle1.pendown()
        turtle1.stamp()
        turtle1.penup()
        turtle1.backward(150)
        turtle1.right(30)
        turtle1.forward(150)

def specialSquare():
    for i in range(1000):
        turtle1.forward((2+i)*2)
        turtle1.left(90)

def swirlySquare():
    screen.bgcolor("maroon")
    turtle1.color("darkorange")
    turtle1.pensize(3)
    turtle1.speed(1000)
    for i in range(300):
         turtle1.forward((0+i))
         turtle1.left(67)
swirlySquare()



  

    


screen.listen()
screen.mainloop()
