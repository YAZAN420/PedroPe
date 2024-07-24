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
    base.sync_acc(80)
    openpipfun()


def open_pipe_second():

    # upClaw()
    # base.sync_acc(445)
    # downClaw()
    # downMotorResetTrueOrFalse(1000, True)
    # upClaw()
    # base.turn(-90)
    # base.move_mm(200, 1000)
    # base.turn(110)
    # base.move_mm(300, -1000)
    # downClaw()
    # base.turn(220)
    downMotorResetTrueOrFalse(1000)
    base.sync_acc(430)
    down_motor.run_until_stalled(speed=-1000, duty_limit=40)
    base.turn(-20)
    base.turn(20)
    # up_motor.run_angle(speed=1000, rotation_angle=200, wait=False)
    upMotorResetWithTrueOrFalse(1000, False)
    base.stop()
    left_motor.run_angle(rotation_angle=40, speed=1000)
    base.turn(-40)
    downMotorResetTrueOrFalse(1000)
    resetDetectedColor()
    base.sync_acc(40)
    up_motor.stop()
    downClaw()
    downClaw()
    downMotorResetTrueOrFalse(1000)
    upClaw()
    base.turn(-60)
    base.move_mm(200, 1000)
    base.turn(110)
    base.move_mm(300, -1000)
    downClaw()
    base.turn(220)


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
    wait(500)
    base.sync_acc(-390)
    up_motor.run_angle(rotation_angle=60, speed=1000, wait=False)
    base.turn(72)
    down_motor.run_angle(rotation_angle=120, speed=-1000, wait=False)
    base.move_mm(280, 500)
    upMotorResetWithTrueOrFalse(-1000, False)
    wait(100)


def supriseRoleDeletHotam():
    base.sync_acc(-30)
    up_motor.run_time(speed=-500, time=1000, wait=False)
    wait(470)
    downMotorResetTrueOrFalse(1000, False)
    wait(500)
    base.sync_acc(-390)
    # up_motor.run_angle(rotation_angle=60, speed=1000, wait=False)
    base.turn(72)


def takeSecondSmallDebris():
    down_motor.run_time(speed=-400, time=600, wait=False)
    wait(150)
    base.sync_acc(500)

    # base.sync_acc(300)
    upMotorResetWithTrueOrFalse(-1000, False)
    wait(300)
    base.move_until_method(see_white, 300)
