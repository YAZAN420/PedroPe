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
downClaw()
take8Blocks()
base.syncAcc(140, 100)
base.turn(100)
base.move_mm(200, -1000)
base.stop_and_hold()
line.stop_at_joint(200)
finish()
