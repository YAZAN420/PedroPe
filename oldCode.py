from config import *
from Utils import *
from resetsAndMotors import *
from seeWithSensors import *
from HotamAndPipe import *


def move_from_blocks_to_line():
    wait(100)
    base.stop()
    base.settings(turn_acceleration=600, turn_rate=10000)
    base.turn(-90)
    upMotorRunTime(speed=-300, time=700, wait=False)
    downMotorRunTime(speed=1000, time=600, wait=False)
    base.sync_acc(100, acc=1000)
    base.move_until_method(see_black, speed=350)
    base.move_mm(distance_in_mm=100, speed=500)
    base.turn(65)
    base.turn_until_method(lambda: right_sensor.reflection() < 15, speed=140)
    line.correct()
    line.follow_cm(12)
    line.until_method(see_white)
    base.sync_acc(225)
    downMotorRunAngle(speed=-1000, rotation_angle=160, wait=False)
    wait(100)
    base.turn(90)
    upMotorRunTime(speed=1000, time=500, wait=False)
    wait(200)
    base.sync_acc(275)
    downMotorRunTime(speed=1000, time=400, wait=False)
    upMotorRunTime(speed=-1000, time=700, wait=True)
    base.stop()
    leftMotorRunTime(speed=400, time=200, wait=True)
    base.move_until_method(see_black, 350)
    base.sync_acc(100)
    wait(100)
    base.turn(70)
    wait(100)
    base.turn_until_method(lambda: left_sensor.reflection() > 80, speed=120)
    base.turn_until_method(lambda: left_sensor.reflection() < 30, speed=120)
    line.correct()
    downMotorRunTime(speed=-1000, time=400, wait=False)
    line.follow_cm(32)
