from config import *
from Utils import *
from seeWithSensors import *
from mainFunctions import *
from resetAndMotor import *


def openpipfun():
    down_motor.run_until_stalled(speed=-1000, duty_limit=21)
    up_motor.run_angle(speed=1000, rotation_angle=200, wait=False)
    base.stop()
    left_motor.run_angle(rotation_angle=40, speed=1000)


def open_pipe():
    line.until_method(see_white, speed=40)
    wait(100)
    base.turn(8)
    down_motor.run_angle(speed=-1000, rotation_angle=200, wait=False)
    base.sync_acc(520)
    down_motor.run_time(speed=1000, time=1000, wait=False)
    wait(200)
    base.sync_acc(77)
    openpipfun()


def open_pipe_second():
    base.sync_acc(415)
    openpipfun()
    downMotorResetTrueOrFalse(1000)
    # down_motor.run_angle(speed=-1000, rotation_angle=170, wait=True)
    # base.sync_acc(-25)
    up_motor.run_time(speed=-500, time=2000, wait=False)
    wait(1000)
    # base.sync_acc(-20)
    # base.sync_acc(30)
    downClaw()

    # second
    # up_motor.run_time(speed=-500, time=1000, wait=True)
    # base.sync_acc(40)
    # downClaw()
    # base.sync_acc(-20)
    # downClaw()


def close_pipe2():
    reset()
    down_motor.run_angle(speed=-1000, rotation_angle=250, wait=True)
    downClaw()
    base.move_until_method(see_white_front, speed=400)
    base.move_mm(30, 400)
    up_motor.run_time(speed=1000, time=100, wait=True)
    down_motor.run_angle(speed=1000, rotation_angle=100, wait=True)
    up_motor.run_time(speed=1000, time=800, wait=True)


def close_pipe1():
    reset()
    downClaw()
    down_motor.run_angle(speed=-1000, rotation_angle=120, wait=True)
    base.sync_acc(40)
    up_motor.run_time(speed=1000, time=800, wait=True)
    down_motor.run_time(speed=-1000, time=600, wait=True)
    base.move_mm(40, 330)
    reset()
    base.move_mm(40, 330)


def takeFirstSmallDebris():
    base.sync_acc(-30)
    up_motor.run_time(speed=-500, time=1000, wait=False)
    wait(560)
    downMotorResetTrueOrFalse(1000, False)
    wait(500)
    base.sync_acc(-390)
    up_motor.run_angle(rotation_angle=60, speed=1000, wait=False)
    base.turn(75)
    down_motor.run_angle(rotation_angle=120, speed=-1000, wait=False)
    base.move_mm(280, 500)
    upMotorResetWithTrueOrFalse(-1000, False)
    wait(100)


def takeSecondSmallDebris():
    down_motor.run_time(speed=-400, time=600, wait=False)
    wait(150)
    base.sync_acc(200)
    upMotorResetWithTrueOrFalse(-1000, False)
    base.sync_acc(300)
    base.move_until_method(see_white, 300)
