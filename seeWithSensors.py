from config import *
from Utils import *


def see_black():
    fir = left_sensor.reflection()
    sec = right_sensor.reflection()
    return fir+sec < 40


def see_blue_right():
    h, s, v = right_sensor.hsv()
    return h > 170


def see_black_front():
    sec = front_sensor.reflection()
    return sec < 20


def see_red():
    ref2 = front_sensor.color()
    return ref2 == Color.RED

def see_red_Right():
    ref2 = right_sensor.color()
    return ref2 == Color.RED



def see_white():
    ref1 = left_sensor.reflection()
    ref2 = right_sensor.reflection()
    return ref1+ref2 > 170


def see_white_front():
    ref1 = front_sensor.reflection()
    return ref1 > 80


def see_yellow_big():
    ref1 = left_sensor.reflection()
    ref2 = right_sensor.reflection()
    return ref1+ref2 > 170


def see_yellow_small_left():
    h, s, v = left_sensor.hsv()
    return v > 20


def see_yellow_small_right():
    h, s, v = right_sensor.hsv()
    return v > 20


def move_until_block(speed):
    base.move_until_method(lambda: front_sensor.rgb()[0] > 4, speed)
