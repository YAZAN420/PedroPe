from config import *
from Utils import *
from resetsAndMotors import *
from seeWithSensors import *
from HotamAndPipe import *


def putBlockOnBlock():
    downMotorRunTime(speed=400, time=300*1.5, wait=False)
    down_motor.run(600)
    upMotorRunAngle(speed=300, angle=60, wait=False)
    wait(110)
    base.sync_acc(50, 600)
    upMotorRunTime(speed=-250, time=300, wait=False)
    wait(110)
    downMotorRunAngle(speed=-1000, angle=150, wait=True)


def make2BlocksGood(lastWait):
    downMotorRunTime(speed=1000, time=300*1.5, wait=False)
    wait(80)
    base.sync_acc(-35, 1000)
    downMotorRunTime(speed=-1000, time=220*3, wait=lastWait)


def putBlockOnBlockWithGood(lastWait=True):
    putBlockOnBlock()
    upMotorRunTime(speed=-1000, time=600, wait=False)
    wait(110)
    make2BlocksGood(lastWait)


def take8Blocks():
    left_motor.run_angle(speed=-700, rotation_angle=230)
    wait(100)
    right_motor.run_angle(speed=-700, rotation_angle=260)
    wait(100)
    resetDetectedColor()
    wait(100)
    moveUntilBlock(500)
    take4block()
    base.move_mm(300, -400)
    base.move_until_method(see_white, -250)
    wait(100)
    base.sync_acc(90, 250)
    base.turn(-110)
    base.move_mm(170, -1000)
    downMotorRunTime(speed=10000, time=400, wait=False)
    upMotorRunTime(speed=1000, time=800, wait=False)
    wait(500)  # do not change to be fast
    base.sync_acc(900, 500)
    base.move_mm(70, 200)
    wait(200)
    downMotorResetTrueOrFalse(1000, False)
    base.turn(83, 300)
    wait(200)
    resetDetectedColor(angle=195)
    downClaw()
    take4block(90)


def take4block(dis=130):
    base.move_mm(dis, 400)
    putBlockOnBlockWithGood()
    downMotorRunTime(speed=1000, time=220*1.5, wait=True)
    upMotorRunAngle(speed=1000, angle=90, wait=False)
    wait(135)
    base.sync_acc(100)
    downClaw()
    base.move_mm(65, 400)
    putBlockOnBlockWithGood(False)
    wait(210)


def make2buildRedAndYellow(mode):
    base.move_until_method(see_yellow_small_left, -400)
    wait(200)
    base.sync_acc(190 if mode == 1 else 15)
    base.turn(70)
    base.move_mm(20, 300)
    base.turn_until_method(lambda: front_sensor.reflection() < 10, speed=100)
    line.correct(duration=0.35)
    line.until_method(see_yellow_big, speed=50)
    base.move_mm(150, 300)
    wait(200)
    base.turn(30 * (-1 if mode == 1 else 1))
    base.turn_until_method(see_black_front, 250*(-1 if mode == 1 else 1))
    base.turn_until_method(see_red, 250*(-1 if mode == 1 else 1))
    base.turn(7 * (-1 if mode == 1 else 1))
    base.move_mm(10, 400)
    leaveblocks()


def leaveblocks():
    base.stop()
    downMotorRunTime(speed=1000, time=440, wait=True)
    downMotorRunAngle(speed=-1000, angle=40, wait=True)
    base.sync_acc(-130)
    base.sync_acc(15)
    upClaw()
    base.sync_acc(-190)
    downClaw()
    downMotorRunTime(speed=1000, time=450, wait=True)
    base.sync_acc(-45)
    upMotorRunAngle(speed=300, rotation_angle=90, wait=True)
    base.sync_acc(360, 190)
    base.stop()
    # UnInstall
    upMotorRunTime(speed=-300, time=250, wait=True)
    downMotorRunAngle(speed=-1000, angle=90, wait=False)
    upClaw()
    base.sync_acc(-80)
    downMotorRunAngle(speed=600, angle=8, wait=True)
    up_motor.stop()
    upMotorRunTime(speed=-400, time=800)
    base.sync_acc(-75)
    upClaw()
    base.sync_acc(-110)
    wait(200)
    # YellowBuild
    downMotorRunAngle(speed=-1000, angle=20, wait=False)
    downClaw()
    downMotorRunTime(speed=1000, time=450, wait=True)
    base.sync_acc(-50)
    upMotorRunAngle(speed=300, angle=90, wait=True)
    base.sync_acc(115)
    upMotorRunTime(speed=-250, time=340, wait=True)
    downMotorRunAngle(speed=-1000, angle=100, wait=True)
    base.sync_acc(-150)


def goToLineAfterMake2Build():
    downClaw()
    base.turn(50)
    base.move_mm(30, 600)
    base.move_until_method(see_black, 600)
    base.move_mm(30, 600)
    base.turn(100, 900)
    base.turn_until_method(lambda: right_sensor.reflection() < 7, 200)
    wait(100)
    line.until_method(see_white, speed=40)
    wait(200)

def removeBlocksFromTheFaceOfRobot(mode):
    if (mode == 1):
        base.turn(-100, 700)
        upMotorRunAngle(speed=550, angle=50, wait=True)
        base.turn(105, 700)
        downClaw()
        base.sync_acc(360)
    else:
        base.sync_acc(360)

def from_blocks_to_hotam_four(mode):
    goToLineAfterMake2Build()
    open_pipe1()
    takeFirstSmallDebris()
    base.move_mm(600, -600)
    downMotorRunAngle(speed=550, angle=-50, wait=False)
    base.turn(150)
    base.move_until_method(see_blue_right, speed=400)
    removeBlocksFromTheFaceOfRobot(mode)
    downMotorResetTrueOrFalse(1000)
    upMotorRunAngle(speed=1000, angle=75, wait=False)
    base.sync_acc(-5)
    base.turn(-85)
    # up_motor.stop()
    takeSecondSmallDebris()
    downMotorResetTrueOrFalse(1000, False)
    base.sync_acc(120)
    base.turn(90)
    open_pipe2()
    base.turn(-90)
    upClaw()
    base.sync_acc(150)


def move_steering(angle, steering, speed=1000):
    motor1 = left_motor
    motor2 = right_motor
    if (steering < 0):
        motor1 = right_motor
        motor2 = left_motor
    k = 1-abs(steering)/50
    print(k)
    motor1.run_angle(speed, angle, wait=False)
    motor2.run_angle(speed*k, angle*abs(k), wait=True)


