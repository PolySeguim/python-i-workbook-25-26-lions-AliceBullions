#All import statements need to be on top of your program
import turtle

# Create a screen and a turtle object
# creating a variable that will store the screen object
# turtle.Screen you are instantiating a Screen Object


# data types that are objects normally have a behavior attached to it.
# behaviors are functions or methods
#screen is a complex data type 

screen = turtle.Screen()
screen.title("Turtle Example in Python")

# Create a turtle instance - you are instantiating a Turtle object
#turtle is a complex data type 
my_turtle = turtle.Turtle() #this is the instatiation call for the object turtle 
my_turtle_2 =turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.pensize("9")
my_turtle.pencolor("green")
my_turtle_2.shape("turtle")

#non fruitful, does not return a value 

"""
def foward100():
    my_turtle.forward(100)
def foward100W():
    my_turtle_2.forward(100)
    
def right90():
    my_turtle.right(90)
def right90D():
    my_turtle_2.right(90)
    
def backward100():
    my_turtle.backward(100)
def backward100S():
    my_turtle_2.backward(100)

def left90():
    my_turtle.left(90)
def left90A():
    my_turtle_2.left(90)

def circle():
    my_turtle.circle(50)

# Draw a square
#  The for loop will loop through the same code 4 times.
# the i represents the loop variable.


for i in range(4):
    #print(i)
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees



screen.onkey(foward100, "Up",)
screen.onkey(backward100, "Down")
screen.onkey(right90, "Right")
screen.onkey(left90, "Left")
screen.onkey(circle, "space")
screen.onkey(foward100W, "w",)
screen.onkey(backward100S, "s")
screen.onkey(right90D, "d")
screen.onkey(left90A, "a")


# Keep the window open until clicked
#closeWindow = input("Press any key to close window. ")

screen.listen()
screen.mainloop()

# Keep the window open until clicked
turtle.done()
"""
#subjects is a list which is a complext data type 
#subject contains a length of 5 
#for loop is for finitee loops 
#ITERATIONS
def rainbow():
    colors = ["red", "orange","yellow", "green", "blue", "indigo", "purple"]
    for color in colors:
        print(color)
        my_turtle.color(color)
        my_turtle.pensize(3)
        my_turtle.circle(20)
        my_turtle.forward(10)


def funActivityWithTurtles ():
    size=20 
    for i in range (30):
        my_turtle_2.penup()
        my_turtle_2.stamp()
        size= size+3 
        my_turtle_2.forward(size)
        my_turtle_2.right(24)
        my_turtle_2.pendown()

def turtle1000():
    size=5
    for i in range (1000):
        colors = ["red", "orange","yellow", "green", "blue", "indigo", "purple"]
        for color in colors:
            print(color)
            my_turtle_2.color(color)
            my_turtle_2.penup()
            my_turtle_2.write("You're amazing")
            size= size+1 
            my_turtle_2.forward(size)
            my_turtle_2.right(50)

def turtlefunsies():
    size=5
    for i in range (1000):
        colors = ["red", "orange","yellow", "green", "blue", "indigo", "purple"]
        for color in colors:
            print(color)
            my_turtle_2.penup()
            my_turtle_2.write("i miss you")
            my_turtle_2.color(color)
            size= size+1 
            my_turtle_2.forward(size)
            my_turtle_2.right(50)
        colors=["purple", "indigo", "blue", "green", "yellow", "orange", "red"]
        for color in colors:
            my_turtle.penup()
            my_turtle.write("i miss you")  
            my_turtle.color(color)
            my_turtle.forward(size)
            my_turtle.left(24)
                             
turtlefunsies()

        



"""
subjects= ["English", "Math", "Science", "Health", "Economics"]
for subject in subjects:
    print("My favorite subject is", subject)
counter=0
while(counter <= subjects.length):
    print("counter:", counter)
    counter= counter+1 
"""

screen.listen()
screen.mainloop()

