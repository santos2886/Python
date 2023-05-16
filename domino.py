import turtle

pen=turtle.Turtle()
pen.speed(5)
pen.up()
pen.goto(-100,0)
pen.down()
for i in range(4):
    pen.forward(200)
    pen.right(90)
pen.left(90)
for i in range(3):
    pen.forward(200)
    pen.right(90)


#1 circulo
pen.up()
pen.goto(0,130)
pen.down()

pen.begin_fill()
pen.circle(30)
pen.end_fill()

#2 circulo
pen.up()
pen.goto(-50,-20)
pen.down()
pen.begin_fill()
pen.circle(30)
pen.end_fill()
#3 circulo
pen.up()
pen.goto(50,-120)
pen.down()
pen.begin_fill()
pen.circle(30)
pen.end_fill()
turtle.mainloop()