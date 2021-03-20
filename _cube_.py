from tkinter import *
import random


# defining movements
def La():
    global cube, cm1
    cm1 = [[[cube[3][0][0], cube[0][0][1], cube[0][0][2]], [cube[3][1][0], cube[0][1][1], cube[0][1][2]],
            [cube[3][2][0], cube[0][2][1], cube[0][2][2]]],
           [[cube[5][2][2], cube[1][0][1], cube[1][0][2]], [cube[5][1][2], cube[1][1][1], cube[1][1][2]],
            [cube[5][0][2], cube[1][2][1], cube[1][2][2]]],
           [[cube[2][0][2], cube[2][1][2], cube[2][2][2]], [cube[2][0][1], cube[2][1][1], cube[2][2][1]],
            [cube[2][0][0], cube[2][1][0], cube[2][2][0]]],
           [[cube[1][0][0], cube[3][0][1], cube[3][0][2]], [cube[1][1][0], cube[3][1][1], cube[3][1][2]],
            [cube[1][2][0], cube[3][2][1], cube[3][2][2]]],
           [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
            [cube[4][2][0], cube[4][2][1], cube[4][2][2]]],
           [[cube[5][0][0], cube[5][0][1], cube[0][2][0]], [cube[5][1][0], cube[5][1][1], cube[0][1][0]],
            [cube[5][2][0], cube[5][2][1], cube[0][0][0]]]]

    cube = cm1
    drawCube()


def Lc():
    global cube, cm2

    cm2 = [[[cube[5][2][2], cube[0][0][1], cube[0][0][2]], [cube[5][1][2], cube[0][1][1], cube[0][1][2]],
            [cube[5][0][2], cube[0][2][1], cube[0][2][2]]],
           [[cube[3][0][0], cube[1][0][1], cube[1][0][2]], [cube[3][1][0], cube[1][1][1], cube[1][1][2]],
            [cube[3][2][0], cube[1][2][1], cube[1][2][2]]],
           [[cube[2][2][0], cube[2][1][0], cube[2][0][0]], [cube[2][2][1], cube[2][1][1], cube[2][0][1]],
            [cube[2][2][2], cube[2][1][2], cube[2][0][2]]],
           [[cube[0][0][0], cube[3][0][1], cube[3][0][2]], [cube[0][1][0], cube[3][1][1], cube[3][1][2]],
            [cube[0][2][0], cube[3][2][1], cube[3][2][2]]],
           [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
            [cube[4][2][0], cube[4][2][1], cube[4][2][2]]],
           [[cube[5][0][0], cube[5][0][1], cube[1][2][0]], [cube[5][1][0], cube[5][1][1], cube[1][1][0]],
            [cube[5][2][0], cube[5][2][1], cube[1][0][0]]]]
    cube = cm2
    drawCube()


def MYu():
    global cube, cm3
    cm3 = [[[cube[0][0][0], cube[3][0][1], cube[0][0][2]], [cube[0][1][0], cube[3][1][1], cube[0][1][2]],
            [cube[0][2][0], cube[3][2][1], cube[0][2][2]]],
           [[cube[1][0][0], cube[5][2][1], cube[1][0][2]], [cube[1][1][0], cube[5][1][1], cube[1][1][2]],
            [cube[1][2][0], cube[5][0][1], cube[1][2][2]]],
           [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
            [cube[2][2][0], cube[2][2][1], cube[2][2][2]]],
           [[cube[3][0][0], cube[1][0][1], cube[3][0][2]], [cube[3][1][0], cube[1][1][1], cube[3][1][2]],
            [cube[3][2][0], cube[1][2][1], cube[3][2][2]]],
           [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
            [cube[4][2][0], cube[4][2][1], cube[4][2][2]]],
           [[cube[5][0][0], cube[0][2][1], cube[5][0][2]], [cube[5][1][0], cube[0][1][1], cube[5][1][2]],
            [cube[5][2][0], cube[0][0][1], cube[5][2][2]]]]
    cube = cm3
    drawCube()


def MYd():
    global cube, cm4

    cm4 = [[[cube[0][0][0], cube[5][2][1], cube[0][0][2]], [cube[0][1][0], cube[5][1][1], cube[0][1][2]],
            [cube[0][2][0], cube[5][0][1], cube[0][2][2]]],
           [[cube[1][0][0], cube[3][0][1], cube[1][0][2]], [cube[1][1][0], cube[3][1][1], cube[1][1][2]],
            [cube[1][2][0], cube[3][2][1], cube[1][2][2]]],
           [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
            [cube[2][2][0], cube[2][2][1], cube[2][2][2]]],
           [[cube[3][0][0], cube[0][0][1], cube[3][0][2]], [cube[3][1][0], cube[0][1][1], cube[3][1][2]],
            [cube[3][2][0], cube[0][2][1], cube[3][2][2]]],
           [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
            [cube[4][2][0], cube[4][2][1], cube[4][2][2]]],
           [[cube[5][0][0], cube[1][2][1], cube[5][0][2]], [cube[5][1][0], cube[1][1][1], cube[5][1][2]],
            [cube[5][2][0], cube[1][0][1], cube[5][2][2]]]]
    cube = cm4
    drawCube()


def Rc():
    global cube, cm5
    cm5 = [[[cube[0][0][0], cube[0][0][1], cube[3][0][2]], [cube[0][1][0], cube[0][1][1], cube[3][1][2]],
            [cube[0][2][0], cube[0][2][1], cube[3][2][2]]],
           [[cube[1][0][0], cube[1][0][1], cube[5][2][0]], [cube[1][1][0], cube[1][1][1], cube[5][1][0]],
            [cube[1][2][0], cube[1][2][1], cube[5][0][0]]],
           [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
            [cube[2][2][0], cube[2][2][1], cube[2][2][2]]],
           [[cube[3][0][0], cube[3][0][1], cube[1][0][2]], [cube[3][1][0], cube[3][1][1], cube[1][1][2]],
            [cube[3][2][0], cube[3][2][1], cube[1][2][2]]],
           [[cube[4][2][0], cube[4][1][0], cube[4][0][0]], [cube[4][2][1], cube[4][1][1], cube[4][0][1]],
            [cube[4][2][2], cube[4][1][2], cube[4][0][2]]],
           [[cube[0][2][2], cube[5][0][1], cube[5][0][2]], [cube[0][1][2], cube[5][1][1], cube[5][1][2]],
            [cube[0][0][2], cube[5][2][1], cube[5][2][2]]]]
    cube = cm5
    drawCube()


def Ra():
    global cube, cm6
    cm6 = [[[cube[0][0][0], cube[0][0][1], cube[5][2][0]], [cube[0][1][0], cube[0][1][1], cube[5][1][0]],
            [cube[0][2][0], cube[0][2][1], cube[5][0][0]]],
           [[cube[1][0][0], cube[1][0][1], cube[3][0][2]], [cube[1][1][0], cube[1][1][1], cube[3][1][2]],
            [cube[1][2][0], cube[1][2][1], cube[3][2][2]]],
           [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
            [cube[2][2][0], cube[2][2][1], cube[2][2][2]]],
           [[cube[3][0][0], cube[3][0][1], cube[0][0][2]], [cube[3][1][0], cube[3][1][1], cube[0][1][2]],
            [cube[3][2][0], cube[3][2][1], cube[0][2][2]]],
           [[cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[4][0][1], cube[4][1][1], cube[4][2][1]],
            [cube[4][0][0], cube[4][1][0], cube[4][2][0]]],
           [[cube[1][2][2], cube[5][0][1], cube[5][0][2]], [cube[1][1][2], cube[5][1][1], cube[5][1][2]],
            [cube[1][0][2], cube[5][2][1], cube[5][2][2]]]]
    cube = cm6
    drawCube()


def Uc():
    global cube, cm7
    cm7 = [[[cube[0][2][0], cube[0][1][0], cube[0][0][0]], [cube[0][2][1], cube[0][1][1], cube[0][0][1]],
            [cube[0][2][2], cube[0][1][2], cube[0][0][2]]],
           [[cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[1][1][0], cube[1][1][1], cube[1][1][2]],
            [cube[1][2][0], cube[1][2][1], cube[1][2][2]]],
           [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
            [cube[2][2][0], cube[2][2][1], cube[2][2][2]]],
           [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
            [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
           [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
            [cube[4][2][0], cube[4][2][1], cube[4][2][2]]],
           [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
            [cube[5][2][0], cube[5][2][1], cube[5][2][2]]]]
    cube = cm7
    drawCube()


def Ua():
    global cube, cm8
    cm8 = [[[cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[0][0][1], cube[0][1][1], cube[0][2][1]],
            [cube[0][0][0], cube[0][1][0], cube[0][2][0]]],
           [[cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[1][1][0], cube[1][1][1], cube[1][1][2]],
            [cube[1][2][0], cube[1][2][1], cube[1][2][2]]],
           [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
            [cube[2][2][0], cube[2][2][1], cube[2][2][2]]],
           [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
            [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
           [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
            [cube[4][2][0], cube[4][2][1], cube[4][2][2]]],
           [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
            [cube[5][2][0], cube[5][2][1], cube[5][2][2]]]]
    cube = cm8
    drawCube()


def MXl():
    global cube, cm9
    cm9 = [[[cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[0][1][0], cube[0][1][1], cube[0][1][2]],
            [cube[0][2][0], cube[0][2][1], cube[0][2][2]]],
           [[cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[1][1][0], cube[1][1][1], cube[1][1][2]],
            [cube[1][2][0], cube[1][2][1], cube[1][2][2]]],
           [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
            [cube[2][2][0], cube[2][2][1], cube[2][2][2]]],
           [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
            [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
           [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
            [cube[4][2][0], cube[4][2][1], cube[4][2][2]]],
           [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
            [cube[5][2][0], cube[5][2][1], cube[5][2][2]]]]
    cube = cm9
    drawCube()


def MXr():
    global cube, cm10
    cm10 = [[[cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[0][1][0], cube[0][1][1], cube[0][1][2]],
             [cube[0][2][0], cube[0][2][1], cube[0][2][2]]],
            [[cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[1][1][0], cube[1][1][1], cube[1][1][2]],
             [cube[1][2][0], cube[1][2][1], cube[1][2][2]]],
            [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
             [cube[2][2][0], cube[2][2][1], cube[2][2][2]]],
            [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
             [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
            [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
             [cube[4][2][0], cube[4][2][1], cube[4][2][2]]],
            [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
             [cube[5][2][0], cube[5][2][1], cube[5][2][2]]]]
    cube = cm10
    drawCube()


def Da():
    global cube, cm11
    cm11 = [[[cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[0][1][0], cube[0][1][1], cube[0][1][2]],
             [cube[0][2][0], cube[0][2][1], cube[0][2][2]]],
            [[cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[1][0][1], cube[1][1][1], cube[1][2][1]],
             [cube[1][0][0], cube[1][1][0], cube[1][2][0]]],
            [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
             [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
            [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
             [cube[4][2][0], cube[4][2][1], cube[4][2][2]]],
            [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
             [cube[5][2][0], cube[5][2][1], cube[5][2][2]]],
            [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
             [cube[2][2][0], cube[2][2][1], cube[2][2][2]]]]
    cube = cm11
    drawCube()


def Dc():
    global cube, cm12
    cm12 = [[[cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[0][1][0], cube[0][1][1], cube[0][1][2]],
             [cube[0][2][0], cube[0][2][1], cube[0][2][2]]],
            [[cube[1][2][0], cube[1][1][0], cube[1][0][0]], [cube[1][2][1], cube[1][1][1], cube[1][0][1]],
             [cube[1][2][2], cube[1][1][2], cube[1][0][2]]],
            [[cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[2][1][0], cube[2][1][1], cube[2][1][2]],
             [cube[5][2][0], cube[5][2][1], cube[5][2][2]]],
            [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
             [cube[2][2][0], cube[2][2][1], cube[2][2][2]]],
            [[cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[4][1][0], cube[4][1][1], cube[4][1][2]],
             [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
            [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
             [cube[4][2][0], cube[4][2][1], cube[4][2][2]]]]
    cube = cm12
    drawCube()


def Bc():
    global cube, cm13
    cm13 = [[[cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[0][1][0], cube[0][1][1], cube[0][1][2]],
             [cube[0][2][0], cube[0][2][1], cube[0][2][2]]],
            [[cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[1][1][0], cube[1][1][1], cube[1][1][2]],
             [cube[2][0][0], cube[2][1][0], cube[2][2][0]]],
            [[cube[0][0][2], cube[2][0][1], cube[2][0][2]], [cube[0][0][1], cube[2][1][1], cube[2][1][2]],
             [cube[0][0][0], cube[2][2][1], cube[2][2][2]]],
            [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
             [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
            [[cube[4][0][0], cube[4][0][1], cube[1][2][2]], [cube[4][1][0], cube[4][1][1], cube[1][2][1]],
             [cube[4][2][0], cube[4][2][1], cube[1][2][0]]],
            [[cube[5][2][0], cube[5][1][0], cube[5][0][0]], [cube[5][2][1], cube[5][1][1], cube[5][0][1]],
             [cube[5][2][2], cube[5][1][2], cube[5][0][2]]]]
    cube = cm13
    drawCube()


def Ba():
    global cube, cm14
    cm14 = [[[cube[2][2][0], cube[2][1][0], cube[2][0][0]], [cube[0][1][0], cube[0][1][1], cube[0][1][2]],
             [cube[0][2][0], cube[0][2][1], cube[0][2][2]]],
            [[cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[1][1][0], cube[1][1][1], cube[1][1][2]],
             [cube[4][2][2], cube[4][1][2], cube[4][0][2]]],
            [[cube[1][2][0], cube[2][0][1], cube[2][0][2]], [cube[1][2][1], cube[2][1][1], cube[2][1][2]],
             [cube[1][2][2], cube[2][2][1], cube[2][2][2]]],
            [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
             [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
            [[cube[4][0][0], cube[4][0][1], cube[0][0][0]], [cube[4][1][0], cube[4][1][1], cube[0][0][1]],
             [cube[4][2][0], cube[4][2][1], cube[0][0][2]]],
            [[cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[5][0][1], cube[5][1][1], cube[5][2][1]],
             [cube[5][0][0], cube[5][1][0], cube[5][2][0]]]]
    cube = cm14
    drawCube()


def MZl():
    global cube, cm15
    cm15 = [[[cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[4][0][1], cube[4][1][1], cube[4][2][1]],
             [cube[0][2][0], cube[0][2][1], cube[0][2][2]]],
            [[cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[2][0][1], cube[2][1][1], cube[2][2][1]],
             [cube[1][2][0], cube[1][2][1], cube[1][2][2]]],
            [[cube[2][0][0], cube[0][1][2], cube[2][0][2]], [cube[2][1][0], cube[0][1][1], cube[2][1][2]],
             [cube[2][2][0], cube[0][1][0], cube[2][2][2]]],
            [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
             [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
            [[cube[4][0][0], cube[1][1][2], cube[4][0][2]], [cube[4][1][0], cube[1][1][1], cube[4][1][2]],
             [cube[4][2][0], cube[1][1][0], cube[4][2][2]]],
            [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
             [cube[5][2][0], cube[5][2][1], cube[5][2][2]]]]
    cube = cm15
    drawCube()


def MZr():
    global cube, cm16
    cm16 = [[[cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[2][2][1], cube[2][1][1], cube[2][0][1]],
             [cube[0][2][0], cube[0][2][1], cube[0][2][2]]],
            [[cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[4][2][1], cube[4][1][1], cube[4][0][1]],
             [cube[1][2][0], cube[1][2][1], cube[1][2][2]]],
            [[cube[2][0][0], cube[1][1][0], cube[2][0][2]], [cube[2][1][0], cube[1][1][1], cube[2][1][2]],
             [cube[2][2][0], cube[1][1][2], cube[2][2][2]]],
            [[cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[3][1][0], cube[3][1][1], cube[3][1][2]],
             [cube[3][2][0], cube[3][2][1], cube[3][2][2]]],
            [[cube[4][0][0], cube[0][1][0], cube[4][0][2]], [cube[4][1][0], cube[0][1][1], cube[4][1][2]],
             [cube[4][2][0], cube[0][1][2], cube[4][2][2]]],
            [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
             [cube[5][2][0], cube[5][2][1], cube[5][2][2]]]]
    cube = cm16
    drawCube()


def Fa():
    global cube, cm17
    cm17 = [[[cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[0][1][0], cube[0][1][1], cube[0][1][2]],
             [cube[4][0][0], cube[4][1][0], cube[4][2][0]]],
            [[cube[2][0][2], cube[2][1][2], cube[2][2][2]], [cube[1][1][0], cube[1][1][1], cube[1][1][2]],
             [cube[1][2][0], cube[1][2][1], cube[1][2][2]]],
            [[cube[2][0][0], cube[2][0][1], cube[0][2][2]], [cube[2][1][0], cube[2][1][1], cube[0][2][1]],
             [cube[2][2][0], cube[2][2][1], cube[0][2][0]]],
            [[cube[3][0][2], cube[3][1][2], cube[3][2][2]], [cube[3][0][1], cube[3][1][1], cube[3][2][1]],
             [cube[3][0][0], cube[3][1][0], cube[3][2][0]]],
            [[cube[1][0][2], cube[4][0][1], cube[4][0][2]], [cube[1][0][1], cube[4][1][1], cube[4][1][2]],
             [cube[1][0][0], cube[4][2][1], cube[4][2][2]]],
            [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
             [cube[5][2][0], cube[5][2][1], cube[5][2][2]]]]
    cube = cm17
    drawCube()


def Fc():
    global cube, cm18
    cm18 = [[[cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[0][1][0], cube[0][1][1], cube[0][1][2]],
             [cube[2][2][2], cube[2][1][2], cube[2][0][2]]],
            [[cube[4][2][0], cube[4][1][0], cube[4][0][0]], [cube[1][1][0], cube[1][1][1], cube[1][1][2]],
             [cube[1][2][0], cube[1][2][1], cube[1][2][2]]],
            [[cube[2][0][0], cube[2][0][1], cube[1][0][0]], [cube[2][1][0], cube[2][1][1], cube[1][0][1]],
             [cube[2][2][0], cube[2][2][1], cube[1][0][2]]],
            [[cube[3][2][0], cube[3][1][0], cube[3][0][0]], [cube[3][2][1], cube[3][1][1], cube[3][0][1]],
             [cube[3][2][2], cube[3][1][2], cube[3][0][2]]],
            [[cube[0][2][0], cube[4][0][1], cube[4][0][2]], [cube[0][2][1], cube[4][1][1], cube[4][1][2]],
             [cube[0][2][2], cube[4][2][1], cube[4][2][2]]],
            [[cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[5][1][0], cube[5][1][1], cube[5][1][2]],
             [cube[5][2][0], cube[5][2][1], cube[5][2][2]]]]
    cube = cm18
    drawCube()


# defining cube movements
def cubeRotate_X_left():
    Ua()
    Dc()
    MXr()


def cubeRotate_X_right():
    Uc()
    Da()
    MXl()


def cubeRotate_Y_up():
    Lc()
    Ra()
    MYd()


def cubeRotate_Y_down():
    La()
    Rc()
    MYu()


def cubeRotate_Z_right():
    Fa()
    MZl()
    Bc()


def cubeRotate_Z_left():
    Fc()
    MZr()
    Ba()


def Scramble():
    Cube()
    clear = Label(root, text=" " * 240, fg="sky blue", bg="sky blue", font="Helvetica 12 bold")
    clear.place(x=10, y=550)
    moves = ['Fa', 'Fc', 'Ra', 'Rc', 'Ua', 'Uc', 'MXl', 'MXr', 'La', 'Lc', 'Da', 'Dc', 'Ba', 'Bc', 'MYu', 'MYd', 'MZl',
             'MZr']
    string = ""
    times = random.randint(15, 30)
    for i in range(times):
        rotation = random.randint(0, 17)
        if rotation == 0:
            Fa()
            string += "F' "
        elif rotation == 1:
            Fc()
            string += "F "
        elif rotation == 2:
            Ra()
            string += "R' "
        elif rotation == 3:
            Rc()
            string += "R "
        elif rotation == 4:
            Ua()
            string += "U' "
        elif rotation == 5:
            Uc()
            string += "U "
        elif rotation == 6:
            MXl()
            string += "MXl "
        elif rotation == 7:
            MXr()
            string += "MXr "
        elif rotation == 8:
            La()
            string += "L' "
        elif rotation == 9:
            Lc()
            string += "L "
        elif rotation == 10:
            Da()
            string += "D' "
        elif rotation == 11:
            Dc()
            string += "D "
        elif rotation == 12:
            Ba()
            string += "B' "
        elif rotation == 13:
            Bc()
            string += "B "
        elif rotation == 14:
            MYu()
            string += "MYu "
        elif rotation == 15:
            MYd()
            string += "MYd "
        elif rotation == 16:
            MZl()
            string += "MZl "
        elif rotation == 17:
            MZr()
            string += "MZr "

    scramble_text = Label(root, text="Scramble : ", fg="Red", bg="skyblue", font="Helvetica 12 bold")
    scramble_text.place(x=10, y=550)
    scramble_steps = Label(root, text=string, fg='black', bg='#E4E4E4', font="Helvetica 12 bold")
    scramble_steps.place(x=100, y=550)


def drawCube():
    global a, b, x, y

    # Creation face 1 :

    F1C1 = canvas.create_rectangle(4 * i, 1 * j, 5 * i, 2 * j, outline='black', fill=cube[0][0][0])
    F1C2 = canvas.create_rectangle(4 * i, 2 * j, 5 * i, 3 * j, outline='black', fill=cube[0][1][0])
    F1C3 = canvas.create_rectangle(4 * i, 3 * j, 5 * i, 4 * j, outline='black', fill=cube[0][2][0])
    F1C4 = canvas.create_rectangle(5 * i, 1 * j, 6 * i, 2 * j, outline='black', fill=cube[0][0][1])
    F1C5 = canvas.create_rectangle(5 * i, 2 * j, 6 * i, 3 * j, outline='black', fill=cube[0][1][1])
    F1C6 = canvas.create_rectangle(5 * i, 3 * j, 6 * i, 4 * j, outline='black', fill=cube[0][2][1])
    F1C7 = canvas.create_rectangle(6 * i, 1 * j, 7 * i, 2 * j, outline='black', fill=cube[0][0][2])
    F1C8 = canvas.create_rectangle(6 * i, 2 * j, 7 * i, 3 * j, outline='black', fill=cube[0][1][2])
    F1C9 = canvas.create_rectangle(6 * i, 3 * j, 7 * i, 4 * j, outline='black', fill=cube[0][2][2])

    # Creation face 2 :

    F2C1 = canvas.create_rectangle(4 * i, 7 * j, 5 * i, 8 * j, outline='black', fill=cube[1][0][0])
    F2C2 = canvas.create_rectangle(4 * i, 8 * j, 5 * i, 9 * j, outline='black', fill=cube[1][1][0])
    F2C3 = canvas.create_rectangle(4 * i, 9 * j, 5 * i, 10 * j, outline='black', fill=cube[1][2][0])
    F2C4 = canvas.create_rectangle(5 * i, 7 * j, 6 * i, 8 * j, outline='black', fill=cube[1][0][1])
    F2C5 = canvas.create_rectangle(5 * i, 8 * j, 6 * i, 9 * j, outline='black', fill=cube[1][1][1])
    F2C6 = canvas.create_rectangle(5 * i, 9 * j, 6 * i, 10 * j, outline='black', fill=cube[1][2][1])
    F2C7 = canvas.create_rectangle(6 * i, 7 * j, 7 * i, 8 * j, outline='black', fill=cube[1][0][2])
    F2C8 = canvas.create_rectangle(6 * i, 8 * j, 7 * i, 9 * j, outline='black', fill=cube[1][1][2])
    F2C9 = canvas.create_rectangle(6 * i, 9 * j, 7 * i, 10 * j, outline='black', fill=cube[1][2][2])

    # Creation face 3 :

    F3C1 = canvas.create_rectangle(1 * i, 4 * j, 2 * i, 5 * j, outline='black', fill=cube[2][0][0])
    F3C2 = canvas.create_rectangle(1 * i, 5 * j, 2 * i, 6 * j, outline='black', fill=cube[2][1][0])
    F3C3 = canvas.create_rectangle(1 * i, 6 * j, 2 * i, 7 * j, outline='black', fill=cube[2][2][0])
    F3C4 = canvas.create_rectangle(2 * i, 4 * j, 3 * i, 5 * j, outline='black', fill=cube[2][0][1])
    F3C5 = canvas.create_rectangle(2 * i, 5 * j, 3 * i, 6 * j, outline='black', fill=cube[2][1][1])
    F3C6 = canvas.create_rectangle(2 * i, 6 * j, 3 * i, 7 * j, outline='black', fill=cube[2][2][1])
    F3C7 = canvas.create_rectangle(3 * i, 4 * j, 4 * i, 5 * j, outline='black', fill=cube[2][0][2])
    F3C8 = canvas.create_rectangle(3 * i, 5 * j, 4 * i, 6 * j, outline='black', fill=cube[2][1][2])
    F3C9 = canvas.create_rectangle(3 * i, 6 * j, 4 * i, 7 * j, outline='black', fill=cube[2][2][2])

    # Creation face 4 :

    F4C1 = canvas.create_rectangle(4 * i, 4 * j, 5 * i, 5 * j, outline='black', fill=cube[3][0][0])
    F4C2 = canvas.create_rectangle(4 * i, 5 * j, 5 * i, 6 * j, outline='black', fill=cube[3][1][0])
    F4C3 = canvas.create_rectangle(4 * i, 6 * j, 5 * i, 7 * j, outline='black', fill=cube[3][2][0])
    F4C4 = canvas.create_rectangle(5 * i, 4 * j, 6 * i, 5 * j, outline='black', fill=cube[3][0][1])
    F4C5 = canvas.create_rectangle(5 * i, 5 * j, 6 * i, 6 * j, outline='black', fill=cube[3][1][1])
    F4C6 = canvas.create_rectangle(5 * i, 6 * j, 6 * i, 7 * j, outline='black', fill=cube[3][2][1])
    F4C7 = canvas.create_rectangle(6 * i, 4 * j, 7 * i, 5 * j, outline='black', fill=cube[3][0][2])
    F4C8 = canvas.create_rectangle(6 * i, 5 * j, 7 * i, 6 * j, outline='black', fill=cube[3][1][2])
    F4C9 = canvas.create_rectangle(6 * i, 6 * j, 7 * i, 7 * j, outline='black', fill=cube[3][2][2])

    # Creation face 5 :

    F5C1 = canvas.create_rectangle(7 * i, 4 * j, 8 * i, 5 * j, outline='black', fill=cube[4][0][0])
    F5C2 = canvas.create_rectangle(7 * i, 5 * j, 8 * i, 6 * j, outline='black', fill=cube[4][1][0])
    F5C3 = canvas.create_rectangle(7 * i, 6 * j, 8 * i, 7 * j, outline='black', fill=cube[4][2][0])
    F5C4 = canvas.create_rectangle(8 * i, 4 * j, 9 * i, 5 * j, outline='black', fill=cube[4][0][1])
    F5C5 = canvas.create_rectangle(8 * i, 5 * j, 9 * i, 6 * j, outline='black', fill=cube[4][1][1])
    F5C6 = canvas.create_rectangle(8 * i, 6 * j, 9 * i, 7 * j, outline='black', fill=cube[4][2][1])
    F5C7 = canvas.create_rectangle(9 * i, 4 * j, 10 * i, 5 * j, outline='black', fill=cube[4][0][2])
    F5C8 = canvas.create_rectangle(9 * i, 5 * j, 10 * i, 6 * j, outline='black', fill=cube[4][1][2])
    F5C9 = canvas.create_rectangle(9 * i, 6 * j, 10 * i, 7 * j, outline='black', fill=cube[4][2][2])

    # Creation face 6 :

    F6C1 = canvas.create_rectangle(10 * i, 4 * j, 11 * i, 5 * j, outline='black', fill=cube[5][0][0])
    F6C2 = canvas.create_rectangle(10 * i, 5 * j, 11 * i, 6 * j, outline='black', fill=cube[5][1][0])
    F6C3 = canvas.create_rectangle(10 * i, 6 * j, 11 * i, 7 * j, outline='black', fill=cube[5][2][0])
    F6C4 = canvas.create_rectangle(11 * i, 4 * j, 12 * i, 5 * j, outline='black', fill=cube[5][0][1])
    F6C5 = canvas.create_rectangle(11 * i, 5 * j, 12 * i, 6 * j, outline='black', fill=cube[5][1][1])
    F6C6 = canvas.create_rectangle(11 * i, 6 * j, 12 * i, 7 * j, outline='black', fill=cube[5][2][1])
    F6C7 = canvas.create_rectangle(12 * i, 4 * j, 13 * i, 5 * j, outline='black', fill=cube[5][0][2])
    F6C8 = canvas.create_rectangle(12 * i, 5 * j, 13 * i, 6 * j, outline='black', fill=cube[5][1][2])
    F6C9 = canvas.create_rectangle(12 * i, 6 * j, 13 * i, 7 * j, outline='black', fill=cube[5][2][2])

    right_back = canvas.create_line(500, 200, 500, 350, width=3, fill="black")
    back_left = canvas.create_line(650, 200, 650, 350, width=3, fill="black")
    front_left = canvas.create_line(200, 200, 200, 350, width=3, fill="black")
    front_right = canvas.create_line(350, 200, 350, 350, width=3, fill="black")
    left_back = canvas.create_line(50, 200, 50, 350, width=3, fill="black")
    top_line = canvas.create_line(50, 200, 650, 200, width=3, fill="black")
    bottom_line = canvas.create_line(50, 350, 650, 350, width=3, fill="black")
    top_left = canvas.create_line(200, 200, 200, 50, width=3, fill="black")
    top_right = canvas.create_line(350, 200, 350, 50, width=3, fill="black")
    bottom_left = canvas.create_line(200, 350, 200, 500, width=3, fill="black")
    bottom_right = canvas.create_line(350, 350, 350, 500, width=3, fill="black")
    top_back = canvas.create_line(200, 50, 350, 50, width=3, fill="black")
    bottom_back = canvas.create_line(200, 500, 350, 500, width=3, fill="black")
    drawLogo()


def drawLogo():
    logo = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\PycharmProjects\\Rubics Cube\\Images\\GAN.png')
    small_logo = logo.subsample(5, 5)
    small_canvas = Button(root, image=small_logo, bg=cube[3][1][1], activebackground=cube[3][1][1], bd=0, relief='flat')
    small_canvas.image = small_logo
    small_canvas.place(x=253, y=253)


def Cube():
    global cr, red, orange, white, green, yellow, blue, cube
    cr = [[[yellow, yellow, yellow], [yellow, yellow, yellow], [yellow, yellow, yellow]],
          [[white, white, white], [white, white, white], [white, white, white]],
          [[orange, orange, orange], [orange, orange, orange], [orange, orange, orange]],
          [[green, green, green], [green, green, green], [green, green, green]],
          [[red, red, red], [red, red, red], [red, red, red]],
          [[blue, blue, blue], [blue, blue, blue], [blue, blue, blue]]]
    cube = cr


def Buttons():
    RightClockwise = Button(root, text="Right", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Rc)
    RightClockwise.place(x=720, y=100)

    RightAnticlockwise = Button(root, text="Right'", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Ra)
    RightAnticlockwise.place(x=820, y=100)

    LeftClockwise = Button(root, text="Left", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Lc)
    LeftClockwise.place(x=720, y=145)

    LeftAnticlockwise = Button(root, text="Left'", width=9, height=1, bd=5, font="Helvetica 8 bold", command=La)
    LeftAnticlockwise.place(x=820, y=145)

    TopClockwise = Button(root, text="Top", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Uc)
    TopClockwise.place(x=720, y=190)

    TopAnticlockwise = Button(root, text="Top'", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Ua)
    TopAnticlockwise.place(x=820, y=190)

    DownClockwise = Button(root, text="Down", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Dc)
    DownClockwise.place(x=720, y=235)

    DownAnticlockwise = Button(root, text="Down'", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Da)
    DownAnticlockwise.place(x=820, y=235)

    FrontClockwise = Button(root, text="Front", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Fc)
    FrontClockwise.place(x=720, y=280)

    FrontAnticlockwise = Button(root, text="Front'", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Fa)
    FrontAnticlockwise.place(x=820, y=280)

    BackClockwise = Button(root, text="Back", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Bc)
    BackClockwise.place(x=720, y=325)

    BackAnticlockwise = Button(root, text="Back'", width=9, height=1, bd=5, font="Helvetica 8 bold", command=Ba)
    BackAnticlockwise.place(x=820, y=325)

    MiddleX_left = Button(root, text="Middle X ←", width=9, height=1, bd=5, font="Helvetica 8 bold", command=MXl)
    MiddleX_left.place(x=720, y=370)

    MiddleX_right = Button(root, text="Middle X →", width=9, height=1, bd=5, font="Helvetica 8 bold", command=MXr)
    MiddleX_right.place(x=820, y=370)

    MiddleY_left = Button(root, text="Middle Y ↑", width=9, height=1, bd=5, font="Helvetica 8 bold", command=MYu)
    MiddleY_left.place(x=720, y=415)

    MiddleY_right = Button(root, text="Middle Y ↓", width=9, height=1, bd=5, font="Helvetica 8 bold", command=MYd)
    MiddleY_right.place(x=820, y=415)

    MiddleZ_left = Button(root, text="Middle Z ←", width=9, height=1, bd=5, font="Helvetica 8 bold", command=MZl)
    MiddleZ_left.place(x=720, y=460)

    MiddleZ_right = Button(root, text="Middle Z →", width=9, height=1, bd=5, font="Helvetica 8 bold", command=MZr)
    MiddleZ_right.place(x=820, y=460)

    scramble = Button(root, text="Scramble", width=9, height=1, bd=5, activebackground="red", font="Helvetica 8 bold",
                      command=Scramble)
    scramble.place(x=770, y=505)


# cube orientation
def cube_orientation():
    canvas.create_line(465, 135, 535, 65, width=1.5, fill="yellow")
    canvas.create_line(500, 50, 500, 150, width=1.5, fill="blue")
    canvas.create_line(450, 100, 550, 100, width=1.5, fill="green")

    Image_up = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\PycharmProjects\\Rubics Cube\\Images\\arrow_up.png')
    small_Image_up = Image_up.subsample(21, 21)
    yUp_rotation = Button(root, image=small_Image_up, command=cubeRotate_Y_up)
    yUp_rotation.image = small_Image_up
    yUp_rotation.place(x=485, y=15)

    Image_down = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\PycharmProjects\\Rubics Cube\\Images\\arrow_down.png')
    small_Image_down = Image_down.subsample(21, 21)
    yDown_rotation = Button(root, image=small_Image_down, command=cubeRotate_Y_down)
    yDown_rotation.image = small_Image_down
    yDown_rotation.place(x=485, y=154)

    Image_left = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\PycharmProjects\\Rubics Cube\\Images\\arrow_left.png')
    small_Image_left = Image_left.subsample(21, 21)
    xLeft_rotation = Button(root, image=small_Image_left, command=cubeRotate_X_left)
    xLeft_rotation.image = small_Image_left
    xLeft_rotation.place(x=415, y=83)

    Image_right = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\PycharmProjects\\Rubics Cube\\Images\\arrow_right.png')
    small_Image_right = Image_right.subsample(21, 21)
    xRight_rotation = Button(root, image=small_Image_right, command=cubeRotate_X_right)
    xRight_rotation.image = small_Image_right
    xRight_rotation.place(x=555, y=83)

    Image_top_right = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\PycharmProjects\\Rubics Cube\\Images\\arrow_up-right.png')
    small_Image_top_right = Image_top_right.subsample(21, 21)
    zRight_rotation = Button(root, image=small_Image_top_right, command=cubeRotate_Z_left)
    zRight_rotation.image = small_Image_top_right
    zRight_rotation.place(x=537, y=36)

    Image_down_left = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\PycharmProjects\\Rubics Cube\\Images\\arrow_down-left.png')
    small_Image_down_left = Image_down_left.subsample(21, 21)
    zLeft_rotation = Button(root, image=small_Image_down_left, command=cubeRotate_Z_right)
    zLeft_rotation.image = small_Image_down_left
    zLeft_rotation.place(x=434, y=138)


# main
if __name__ == '__main__':
    a = 600
    b = 1000
    i = int(a / 12)
    j = int(a / 12)
    x = int(a / 22.5)
    y = int(b / 30)
    color = ['red', 'blue', 'yellow', 'white', 'orange', 'forest green']
    red = 'red'
    orange = 'orange'
    white = 'white'
    green = 'forest green'
    yellow = 'yellow'
    blue = 'blue'
    Cube()
    root = Tk()
    root.geometry(str(b) + "x" + str(a))
    root.title("Rubics Cube")
    icon = PhotoImage(file="C:\\Users\\Lenovo\\Desktop\\PycharmProjects\\Rubics Cube\\Images\\rubik.png")
    root.iconphoto(False, icon)
    root.resizable(False, False)
    canvas = Canvas(root, width=b, heigh=a, bg='sky blue')
    canvas.pack(side=LEFT)
    canvas.create_window(700, 500)
    drawCube()
    Buttons()
    cube_orientation()

    root.mainloop()
