from turtle import *

#We want to draw a GOA castle

#Step 1: Draw a rectangle - the center of the castle.

speed(1000)
width(25)
color("brown")
begin_fill()

forward(350)
right(90)

forward(270)
right(90)

forward(700)
right(90)

forward(270)
right(90)

forward(350)
end_fill()

penup()
goto(-350, 0)
pendown()

begin_fill()
left(90)
forward(200)

right(90)
forward(30)

right(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

right(90)
forward(30)

right(90)
forward(200)
end_fill()

penup()
goto(350, 0)
pendown()

begin_fill()
right(180)
forward(200)

left(90)
forward(30)

left(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

left(90)
forward(30)
left(90) 
forward(200)
end_fill()

penup()
goto(-150, 0)
penup()

begin_fill()

right(180)
forward(300)

right(90)
forward(60)

right(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)

right(90)
forward(60)

right(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)

right(90)
forward(60)

right(90)
forward(300)
end_fill()

penup()
goto(0, 300)
pendown()

color("black")
width(7)

right(180)
forward(90)

color("yellow")
begin_fill()
right(90)
forward(130)

right(90)
forward(70)

right(90)
forward(130)
end_fill()

penup()
goto(12, 330)
pendown()

color("green")
right(90)
width(23)
write("GOA")



penup()
goto(-90, -270)
pendown()

color("yellow")
begin_fill()
forward(250)

right(90)
forward(180)

right(90)
forward(250)

right(90)
forward(180)
end_fill()

penup()
goto(-320, 25)
pendown()

begin_fill()
right(90)
forward(125)

right(90)
forward(90)

right(90)
forward(125)

right(90)
forward(90)
end_fill()

penup()
goto(320, 25)
pendown()

begin_fill()
right(90)
forward(125)

left(90)
forward(90)

left(90)
forward(125)

left(90)
forward(90)
end_fill()






exitonclick()





