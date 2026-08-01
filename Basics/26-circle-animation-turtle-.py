from turtle import *
bgcolor("black")
tracer(15)
for i in range(200):
    color("red")
    circle(i*0.6)
    color("blue")
    circle(i*0.4)
    right(4)
    forward(3)
done()