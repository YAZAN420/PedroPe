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
waitForButtonPress()
preflightChecks()
resetStart()
# take8Blocks()
# make2buildRedAndYellow(1)
# move_from_blocks_to_line()

# goToFirstSafahAfterHotam()

base.move_mm(30,300)
downClaw()
base.turn(50)
base.move_until_method(see_black,700)
base.move_mm(50,800)
base.turn(70)
base.turn_until_method(lambda: right_sensor.reflection() < 7,100)
wait(200)
garbage.run()
# base.syncAcc(-600,1000)
base.turn(140)
base.move_until_method(see_yellow_small2,100)

finish()
