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
down_motor.run_time(speed=1000,time=600,wait=False)
up_motor.run_time(speed=-1000,time=600,wait=False)
take8Blocks()
make2buildRedAndYellow(1)
wait(3000)
base.turn(60)
downClaw()
base.move_until_method(see_black, speed=300)
base.move_mm(distance_in_mm=100, speed=300)
base.turn(70)
base.turn_until_method(lambda: right_sensor.reflection() < 15, speed=90)
garbage.run()
# testleaveblocksagain()
finish()
