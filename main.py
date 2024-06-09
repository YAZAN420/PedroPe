#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick # type: ignore
from pybricks.ev3devices import Motor,ColorSensor,GyroSensor # type: ignore
from pybricks.parameters import Port,Direction,Color,Stop # type: ignore
from pybricks.tools import wait,StopWatch # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
from Utils import *
from config import *
from tests import *
from mainFunctions import *
preflightChecks()
reset()
downClaw(70)
take8Blocks()

# tmpTest()
base.stop_and_hold()
finish()
    


