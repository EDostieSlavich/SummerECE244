import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(random.randrange(0, 90, 15))
        tree(branchLen - 1, t)
        t.left(random.randrange(0, 90, 15))
        tree(branchLen - 15, t)
        t.right(random.randrange(0, 90, 1))
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()


main()
