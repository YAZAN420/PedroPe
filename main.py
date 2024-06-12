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
preflightChecks()
reset()
# base.turn(93)
# garbage.run()


base.acc_one_motor(left_motor, 200, -60)
wait(300)
base.acc_one_motor(right_motor, 200, -60)


# take8Blocks()
# base.stop_and_hold()
# base.syncAcc(-100)
# base.turn(-90)
# base.move_mm(70, -600)
# line.move_until_black()
# line.correct()
finish()
