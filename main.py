import turtle
import math

file = open('pi.txt', 'r')
pi = file.read()
pi = [int(d) for d in pi]
file.close()

windo = turtle.Screen()
windo.bgcolor("light green")
windo.title("Turtle")
turtie = turtle.Turtle()

for digit in pi:
    turtie.forward(50)
    turtie.right(digit*180/math.pi)


turtle.done()