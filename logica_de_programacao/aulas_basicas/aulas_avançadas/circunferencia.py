from turtle import *
clearscreen()
setup(600, 400)
bob = Turtle()
bob.speed(13)
bob.penup()
bob.sety(48)
bob.pendown()
for cont in range (360):
    bob.forward(1)
    bob.right(1)
    
exitonclick()