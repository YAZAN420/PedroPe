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
mode = 1
waitForButtonPress()
preflightChecks()
resetStart()
take8Blocks()
make2buildRedAndYellow(mode)
print(stopwatch.time()//1000)
downClaw()
base.turn(45)
base.move_mm(30, 500)
base.move_until_method(see_black, 400)
base.move_mm(50, 800)
base.turn(120)
base.turn_until_method(lambda: right_sensor.reflection() < 7, 100)
wait(200)
open_pipe1()
upClaw()
down_motor.run_time(speed=-500, time=150, wait=False)
base.turn(130)
downClaw()
base.move_mm(300, 500)
base.turn(95)
down_motor.run_time(1000, 220*1.5, then=Stop.HOLD, wait=True)
down_motor.run_time(-1000, 100, then=Stop.HOLD, wait=True)
upClaw()
base.move_mm(200,1000)
downClaw()
down_motor.run_time(-1000, 100, then=Stop.HOLD, wait=True)
base.move_mm(450,1000)
down_motor.run_angle(speed=-200,rotation_angle=70,wait=False)
right_motor.run_angle(speed=750, rotation_angle=200,wait=False)
left_motor.run_angle(speed=700, rotation_angle=200)

from_blocks_to_hotam_four(mode)
finish()
