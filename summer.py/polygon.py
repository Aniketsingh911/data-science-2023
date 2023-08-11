from turtle import *

def triangle():
    for i in range(3):
        fd(100)
        lt(360/3)


def square():
    for i in range(4):
        fd(100)
        lt(360/4)


def hexagon():
    for i in range(6):
        fd(100)
        lt(360/6)


def pentagon():
    for i in range(5):
        fd(100)
        lt(360/5)


def hectagon():
    for i in range(8):
        fd(100)
        lt(360/8)


def spentagon():
    for i in range(7):
        fd(100)
        lt(360/7)


def decagon():
    for i in range(10):
        fd(100)
        lt(360/10)

print(__name__)
if __name__ == "__main__":
    print('This is running as current file')
    