from config import *
from Utils import *
from seeWithSensors import *
from mainFunctions import *
from resetAndMotor import *


def openpipfun():
    down_motor.run_until_stalled(speed=-1000, duty_limit=25)
    up_motor.run_angle(speed=1000, rotation_angle=200, wait=False)
    base.stop()
    left_motor.run_angle(rotation_angle=40, speed=1000)


def open_pipe():
    line.until_method(see_white, speed=40)
    wait(100)
    base.turn(9)
    down_motor.run_angle(speed=-1000, rotation_angle=200, wait=False)
    base.sync_acc(520)
    down_motor.run_time(speed=1000, time=1000, wait=False)
    wait(200)
    base.sync_acc(80)
    openpipfun()


def open_pipe_second():
    base.sync_acc(420)
    openpipfun()
    up_motor.run_time(speed=-500, time=1200)


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
    wait(470)
    downMotorResetTrueOrFalse(1000, False)
    wait(400)
    # base.sync_acc(-200)
    # down_motor.run_angle(rotation_angle=-220, speed=1000, wait=False)
    # base.sync_acc(30)
    # downMotorResetTrueOrFalse(1000, False)
    base.sync_acc(-390)
    up_motor.run_angle(rotation_angle=60, speed=1000, wait=False)
    base.turn(72)
    down_motor.run_angle(rotation_angle=120, speed=-1000, wait=False)
    # base.sync_acc(260)
    base.move_mm(280, 1000)
    upMotorResetWithTrueOrFalse(-1000, False)
    wait(100)


def takeSecondSmallDebris():
    down_motor.run_time(speed=-400, time=600, wait=False)
    # down_motor.run_time(speed=-1000, time=300)
    wait(150)
    base.sync_acc(200)
    upMotorResetWithTrueOrFalse(-1000, False)
    base.sync_acc(300)
    base.move_until_method(see_white, 300)
