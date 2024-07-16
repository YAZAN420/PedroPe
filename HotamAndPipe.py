from config import *
from Utils import *
from resetsAndMotors import *
from seeWithSensors import *
from HotamAndPipe import *

def openpipfun():
    downMotorUntilStalled(speed=-1000, duty=25)
    upMotorRunAngle(speed=1000, angle=200, wait=False)
    base.stop()
    leftMotorRunAngle(speed=1000, angle=40, wait=True)


def open_pipe1():
    base.sync_acc(100)
    wait(100)
    base.turn(9)
    downMotorRunAngle(speed=-1000, angle=200, wait=False)
    base.sync_acc(420)
    downMotorRunTime(speed=1000, time=1000, wait=False)
    wait(200)
    base.sync_acc(80)
    openpipfun()

def open_pipe2():
    base.sync_acc(440)
    openpipfun()
    upMotorRunTime(speed=-500, time=1200, wait=True)

def takeFirstSmallDebris():
    base.sync_acc(-30)
    upMotorRunTime(speed=-500, time=1000, wait=False)
    wait(470)
    downMotorResetTrueOrFalse(1000)
    base.sync_acc(-200)
    downMotorRunAngle(speed=1000, angle=-220, wait=False)
    base.sync_acc(30)
    downMotorResetTrueOrFalse(1000, False)
    base.sync_acc(-240)
    upMotorRunAngle(speed=1000, angle=60, wait=True)
    base.turn(80)
    downMotorRunAngle(speed=-1000, angle=120, wait=True)
    base.sync_acc(250)
    upMotorResetWithTrueOrFalse(-1000, False)
    wait(100)

def takeSecondSmallDebris():
    base.move_mm(200, -1000)
    downMotorRunTime(speed=-400, time=300, wait=True)
    downMotorRunTime(speed=-1000, time=300, wait=True)
    base.sync_acc(200)
    upMotorResetWithTrueOrFalse(-1000)
    base.sync_acc(300)
    base.move_until_method(see_white, 300)

def close_pipe2():
    reset()
    downMotorRunAngle(speed=-1000, angle=250, wait=True)
    downClaw()
    base.move_until_method(see_white_front, speed=400)
    base.move_mm(30, 400)
    upMotorRunTime(speed=1000, time=100, wait=True)
    downMotorRunAngle(speed=1000, angle=100, wait=True)
    upMotorRunTime(speed=1000, time=800, wait=True)


def close_pipe1():
    reset()
    downClaw()
    downMotorRunAngle(speed=-1000, angle=120, wait=True)
    base.sync_acc(40)
    upMotorRunTime(speed=1000, time=800, wait=True)
    downMotorRunTime(speed=-1000, time=600, wait=True)
    base.move_mm(40, 330)
    reset()
    base.move_mm(40, 330)
