#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor  # type: ignore
from pybricks.parameters import Port, Direction, Color, Stop  # type: ignore
from pybricks.tools import wait, StopWatch  # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
from Utils import *
from config import *
from tests import *
from mainFunctions import *
from garbage import *
from AccOneEnc import *
import time
# waitForButtonPress()
preflightChecks()
# resetStart()
# take8Blocks()
# make2buildRedAndYellow(1)
move_from_blocks_to_line()

line.correct()
down_motor.run_time(speed=1000, time=800, wait=False)


def see_white():
    ref1 = left_sensor.reflection()
    ref2 = right_sensor.reflection()
    return ref1+ref2 > 180


line.until_method(see_white)
base.syncAcc(220)
down_motor.run_angle(speed=-1000, rotation_angle=160, wait=False)
base.turn(107)
wait(100)
base.syncAcc(290)
wait(100)
base.move_until_method(see_black)
base.syncAcc(100)
wait(100)
base.turn(80)
wait(100)
base.turn_until_method(lambda: left_sensor.reflection() > 80, speed=100)
base.turn_until_method(lambda: left_sensor.reflection() < 30, speed=100)
line.correct()
line.follow_cm(30)
garbage.run()
finish()
