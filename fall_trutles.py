
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

def drawClock(t):
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
    screen.bgcolor("darkorange")
    turtle1.color("maroon")
    turtle1.pensize(10)
    turtle1.speed(1000)
    for i in range(750):
         turtle1.forward((0+i)*2)
         turtle1.left(91)

def multiColorSquare(t, sz, c):
    t.pensize(3)
    for i in c:
        t.color(i)
        t.forward(sz)
        t.left(90)
def getThickness():
    thickness=int(input("Enter the thickness of the turtles"))
    return thickness 
def test():
    test_turtle=turtle.Turtle()
    test_turtle.color("pink")
    color1=["red", "purple","hotpink","blue"]
    color2=["black", "orange", "green", "yellow"]
    color3=["purple", "red", "grey", "brown"]
    for i in range(200):
        multiColorSquare(test_turtle, i*10, c)
    

def drawSquare(t, side):
    for i in range(4):
        t.forward(side)
        t.right(90)



def testSpace():
   testy_turtle=turtle.Turtle
   for i in range(5):
       drawSquare(testy_turtle, 20)
       testy_turtle.penup()
       testy_turtle.forward(10)
       testy_turtle.pendown()

testSpace()




  
screen.listen()
screen.mainloop()
    


