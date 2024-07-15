from config import *
from mainFunctions import *
from tests import *
from mainFunctions import *


def downClaw(duty=70):
    up_motor.run_until_stalled(-6000, then=Stop.HOLD, duty_limit=duty)


def see_white():
    ref1 = left_sensor.reflection()
    ref2 = right_sensor.reflection()
    return ref1+ref2 > 170


def see_black():
    fir = left_sensor.reflection()
    sec = right_sensor.reflection()
    return fir+sec < 45


def upClaw():
    up_motor.run_until_stalled(1000, then=Stop.HOLD, duty_limit=110)


def reset_to_down_sen():
    downClaw()
    down_motor.run_angle(speed=-1000, rotation_angle=245)


def openpipfun():
    down_motor.run_time(speed=-500, time=450, wait=True)
    up_motor.run_angle(speed=1000, rotation_angle=200, wait=False)
    base.stop()
    left_motor.run_angle(rotation_angle=40, speed=1000)
    base.move_mm(20, 400)


def open_pipe1():
    line.until_method(see_white, speed=40)
    base.sync_acc(100)
    wait(200)
    base.turn(9.5)
    up_motor.run_angle(speed=8000, rotation_angle=80, wait=False)
    down_motor.run_angle(speed=1000, rotation_angle=260, wait=False)
    base.sync_acc(505)
    downClaw()
    down_motor.stop()
    openpipfun()
    base.move_mm(50, -400)
    up_motor.stop()



def open_pipe2():
    line.correct()
    line.follow_cm(37)
    line.until_method(see_white, speed=40)
    up_motor.run_angle(speed=800, rotation_angle=20, wait=False)
    down_motor.run_angle(speed=-1000, rotation_angle=260, wait=False)
    wait(100)
    base.turn(-20)
    up_motor.run_time(speed=800, time=500, wait=False)
    base.sync_acc(650, acc=900)


def take_debris():
    base.turn(15)
    base.sync_acc(-370, 500)
    base.turn(63)
    up_motor.run_angle(rotation_angle=60, speed=550, wait=True)
    base.syncMoveMm(280, 1000)
    down_motor.stop()
    down_motor.run_time(speed=10000, time=700, wait=False)
    up_motor.run_time(speed=-400, time=700, wait=False)
    downClaw()
    down_motor.hold()


def run():
    open_pipe1()
    take_debris()
    base.sync_acc(-680, 700)
