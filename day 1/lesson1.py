from turtle import *


#We want to paint a house

#Atep 1: draw a square
speed(5)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("Purple")
left(30)
forward(10)
left(90)

color("brown")
begin_fill()
forward(60)
right(90)

forward(60)
right(90)

forward(60)
right(90)

forward(60)
end_fill()

penup()
goto(200, 190)
left(90)

color("brown")
begin_fill()
forward(60)
left(90)

forward(60)
left(90)

forward(60)
left(90)

forward(60)
left(90)
end_fill()



exitonclick()