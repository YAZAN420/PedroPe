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
upClaw()
waitForButtonPress()
# preflightChecks()
resetStart()
right_motor.run_time(time=150, speed=400)
upClaw()
base.syncAcc(500)
downClaw()
base.move_until_method(see_black, speed=300)
upClaw()
base.move_mm(270, 300)
reset()
base.turn(90)
resetDetectedColor()
downClaw()
base.move_mm(70, -200)
wait(200)
base.move_sideway(180, -50, 0)
moveUntilBlock(400)
take4block()
base.syncAcc(890)
# base.move_until_method(lambda: front_sensor.reflection() > 75, speed=-100)
down_motor.run_time(speed=300, time=450)
upClaw()
base.syncAcc(-450)
base.turn(90)
base.move_mm(170, -300)
move_from_blocks_to_line()
garbage.run()
upClaw()
base.syncAcc(-250)
downClaw()
base.syncAcc(250)
        
finish(True)
