import turtle
from scipy.constants import golden as phi

"""
The aloe polyphylla plant grows in a pattern with five golden spirals
eminating from the same center. Make a function that draws a single golden
spiral, and use that to draw a shape like the aloe polyphylla.

You may find these functions useful:

turtle.up()

turtle.down()

turtle.setposition(x, y)

turtle.setheading(degrees)

The turtle starts at position(0, 0) with heading 0 degrees.
"""

### YOUR CODE STARTS HERE
turtle.speed(20)
IAL = 5
R = 10
for h in range(13):
    turtle.up()
    turtle.goto(0,0)
    turtle.right(360/5)
    turtle.down()
    for i in range(48):
        DTSF = R*i
        AL = IAL * (phi**(DTSF / 90)) 
        turtle.forward(AL)
        turtle.right(R)

### YOUR CODE ENDS HERE

turtle.exitonclick()