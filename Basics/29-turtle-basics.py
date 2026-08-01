from turtle import *

bgcolor('black')
#Traingle
color('white')
fillcolor('red')
begin_fill()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
end_fill()


#pos()
#clearscreen()

#spiral
#for steps in range(100):
 #   for c in('blue','red','green'):
 #       color(c)
  #      forward(steps)
   #     right(30)

#clearscreen()

#star
color('red')
fillcolor('yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
