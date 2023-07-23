import turtle

drawing_board = turtle.Screen()

drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()

sekil = input("Enter the shape you want drawn: ")
arkaplan = input("Enter the background color you want: ")

#square
def square():
    for i in range(4):
        turtle_instance.forward(100)
        turtle_instance.left(90)
#star
def star():
    for i in range(5):
        turtle.forward(210)
        turtle.left(216)

def triangle():
    for i in range(3):
        turtle.forward(150)
        turtle.left(120)

if sekil == "square":
    drawing_board.bgcolor(arkaplan)
    square()
    turtle.done()
elif sekil == "star":
    drawing_board.bgcolor(arkaplan)
    star()
    turtle.done()
elif sekil == "triangle":
    drawing_board.bgcolor(arkaplan)
    triangle()
    turtle.done()

else:
    print("There is no such shape.")
    turtle.done()



