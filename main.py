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
from AccOneEnc import *
import time
mode = 2
upClaw()
wait_for_button_press()
# preflight_checks()
reset_start()
take_8_blocks()
make2buildRedAndYellow(mode)
print(stopwatch.time()//1000)
from_blocks_to_hotam_four(mode)
finish()
