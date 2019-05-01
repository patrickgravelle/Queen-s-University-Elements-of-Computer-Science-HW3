# Patrick Gravelle 10141195
# This program uses the turtle to draw a standard dart board with
# the usual colour pattern that a dartboard contains.  The code is
# comprised of several functions which all serve a different aspect
# in creating the dartboard.  The board starts from nothing, and is
# then constructed from the biggest components to the smallest.
from turtle import *

# The board function assembles the base of the board with the
# simple 20 slices in alternating colour fashion using a while
# loop and counter.
def board():
    count = 0
    while (count < 20) :
        if (count % 2 == 0):
            fillcolor("light yellow")
        else :
            fillcolor("black")
        begin_fill()
        circle(100, 36)
        left(90)
        forward(100)
        left(162)
        forward(100)
        left(90)
        end_fill()
        count = count + 1
# The multiples function assembles the sections of the board in
# which players receive "double" or "triple" points for hitting
# these spots. This was done similarly to the board assembly.
def multiples(radius, width, negradius):
    num = 0
    while (num < 20) :
        if (num % 2 == 0):
            fillcolor("green")
        else :
            fillcolor("red")
        begin_fill()
        circle(radius, 36)
        left(90)
        forward(width)
        left(90)
        circle(negradius, 18)
        left(90)
        forward(width)
        left(90)
        end_fill()
        num = num + 1
# The bullseye function along with its parameters allows for
# the construction of any size and colour bullseye.  The length
# parameter determines how far inward toward the centre the
# turtle must go to begin the next bullseye.
def bullseyes(size, colour, length):
    left(90)
    penup()
    forward(length)
    pendown()
    right(90)
    fillcolor(colour)
    begin_fill()
    circle(size)
    end_fill()
# Here in main we call the function with the correct parameters
# to complete the dartboard.
def main():
    shape("turtle")
    speed(100)
    board()
    multiples(100, 10, -90)
    left(90)
    forward(40)
    right(90)
    multiples(60, 7, -53)
    bullseyes(10, "green", 50)
    bullseyes(5, "red", 5)
    penup()
    right(90)
    forward(110)
main()
