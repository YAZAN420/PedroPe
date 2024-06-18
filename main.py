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
base.straight(65)
base.turn(130)
base.move_mm(300, -1000)
base.stop_and_hold()
downClaw(100)
down_motor.run_time(-1000, 200, then=Stop.HOLD, wait=True)
line.stop_at_joint(70)
print("black finsshed")
wait(1000)
line.correct()
line.stop_at_white(70)
print("white finsshed")
wait(1000)
base.move_mm(100, 400)
base.turn(-95)
base.move_mm(10, 400)
base.stop()
down_motor.run_time(1000, 400, then=Stop.HOLD, wait=True)
base.move_mm(130, -300)
upClaw()
base.move_mm(230, -300)
downClaw()
down_motor.run_time(1000, 400, then=Stop.HOLD, wait=True)
upClaw()
base.move_mm(310, 300)
finish()
