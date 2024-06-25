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

preflightChecks()
reset()
downClaw(100)


# down_motor.run_time(speed=-1000, time=1000)
# while True:

#     base.turn(100)
#     wait(5000)
take8Blocks()
make2buildRedAndYellow(1)
finish()
