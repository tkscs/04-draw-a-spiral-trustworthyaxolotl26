import turtle

"""
Make a rectangular spiral (see the README.md for an example)
"""

### YOUR CODE STARTS HERE

x = 20
HBS = 1.3

def regSprial():
    global x
    for i in range(20):
        turtle.forward(x)
        turtle.right(90) 
        x = x+10

def exponentialSpiral():
    for i in range(10):
        turtle.forward(x)
        turtle.right(90)
        x = x*HBS 

exponentialSpiral()

regSprial()

### YOUR CODE ENDS HERE

turtle.exitonclick()