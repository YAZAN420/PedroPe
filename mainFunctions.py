from config import *
from Utils import *
from seeWithSensors import *
from HotamAndPipe import *
from resetAndMotor import *


def putBlockOnBlock():
    down_motor.run_time(400, 300*1.5, then=Stop.HOLD, wait=True)
    down_motor.run(600)
    up_motor.run_angle(speed=300, rotation_angle=60,
                       then=Stop.HOLD, wait=False)
    wait(110)
    base.sync_acc(50, 600)
    up_motor.run_time(-250, 300, wait=False)
    wait(150)
    down_motor.stop()
    down_motor.run_angle(speed=-1000, rotation_angle=150,
                         then=Stop.HOLD, wait=False)
    wait(200)


def make2BlocksGood(lastWait):
    down_motor.run_time(1000, 300*1.5, wait=False)
    wait(80)
    base.sync_acc(-35, 1000)
    down_motor.run_time(-1000, 220*3, wait=lastWait)


def putBlockOnBlockWithGood(lastWait=True):
    putBlockOnBlock()
    up_motor.run_time(speed=-1000, time=600, wait=False)
    wait(110)
    make2BlocksGood(lastWait)


def take_8_blocks():
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
    down_motor.run_time(speed=10000, time=400, wait=False)
    up_motor.run_time(speed=1000, time=500, wait=False)
    wait(400)  # do not change to be fast
    base.sync_acc(900, 450)
    base.move_mm(70, 200)
    wait(200)
    downMotorResetTrueOrFalse(1000, False)
    base.turn(78, 300)
    wait(200)
    resetDetectedColor(angle=180)
    base.stop()
    # right_motor.run_angle(speed=700, rotation_angle=70)
    # wait(50)
    # left_motor.run_angle(speed=700, rotation_angle=70)
    # wait(50)
    # base.move_mm(30, -400)
    downClaw()
    take4block(90)


def take4block(dis=130):
    base.move_mm(dis, 400)
    putBlockOnBlockWithGood()
    down_motor.run_time(1000, 220*1.5, then=Stop.HOLD, wait=True)
    up_motor.run_angle(speed=1000, rotation_angle=90, wait=False)
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
    # base.turn(95 * (-1 if mode == 1 else 1))
    base.turn(40 * (-1 if mode == 1 else 1))
    base.turn_until_method(see_black_front, 250*(-1 if mode == 1 else 1))
    base.turn_until_method(see_red, 250*(-1 if mode == 1 else 1))
    base.turn(10 * (-1 if mode == 1 else 1))
    base.move_mm(10, 400)
    leaveblocks()


def leaveblocks():
    base.stop()
    down_motor.run_time(speed=1000, time=440, wait=True)
    down_motor.run_angle(speed=-1000, rotation_angle=40, wait=True)
    base.sync_acc(-130)
    base.sync_acc(15)
    # upClaw()
    up_motor.run_angle(speed=300, rotation_angle=90, wait=False)
    wait(150)
    base.sync_acc(-190)
    # downClaw()
    upMotorResetWithTrueOrFalse(-1000, False)
    wait(250)
    down_motor.run_time(speed=1000, time=450, wait=False)
    wait(100)
    base.sync_acc(-45)
    up_motor.run_angle(speed=300, rotation_angle=85)
    base.sync_acc(360, 190)
    base.stop()
    # uninstall
    up_motor.run_time(speed=-300, time=250)
    down_motor.run_angle(speed=-1000, rotation_angle=90)
    upClaw()
    base.sync_acc(-80)
    down_motor.run_angle(speed=600, rotation_angle=8)
    up_motor.stop()
    up_motor.run_time(speed=-400, time=800)
    base.sync_acc(-75)
    upClaw()
    base.sync_acc(-110)
    wait(200)
    # # yellow build
    down_motor.run_angle(speed=-1000, rotation_angle=20, wait=False)
    downClaw()
    down_motor.run_time(speed=1000, time=450)
    base.sync_acc(-50)
    up_motor.run_angle(speed=300, rotation_angle=90)
    base.sync_acc(115)
    up_motor.run_time(-250, 340)
    down_motor.run_angle(speed=-1000, rotation_angle=105)
    base.sync_acc(-150)


def goToLineAfterMake2Build():
    downMotorResetTrueOrFalse(1000)
    downClaw()
    base.turn(50)
    base.move_mm(30, 600)
    base.move_until_method(see_black, 600)
    base.move_mm(40, 600)
    base.turn(100, 900)
    base.turn_until_method(lambda: right_sensor.reflection() < 7, 200)
    wait(100)


def removeBlocksFromTheFaceOfRobot(mode):
    if (mode == 1):
        base.turn(-100, 700)
        up_motor.run_angle(rotation_angle=50, speed=550)
        base.turn(105, 700)
        downClaw()
        base.sync_acc(310)
    else:
        base.sync_acc(310)


def from_blocks_to_hotam_four(mode):
    goToLineAfterMake2Build()
    open_pipe()
    takeFirstSmallDebris()
    base.move_mm(750, -1000)
    down_motor.run_angle(rotation_angle=-50, speed=550, wait=False)
    base.turn(150)
    base.move_mm(250, 600)
    base.move_until_method(see_blue_right, speed=500)
    wait(100)
    removeBlocksFromTheFaceOfRobot(mode)
    downMotorResetTrueOrFalse(1000)
    up_motor.run_angle(rotation_angle=75, speed=1000, wait=False)
    # base.move_mm(20, -1000)
    base.turn(-110)
    up_motor.stop()
    # up_motor.run_angle(rotation_angle=100, speed=-550, wait=False)
    base.move_mm(200, -1000)
    takeSecondSmallDebris()
    downMotorResetTrueOrFalse(1000, False)
    base.sync_acc(120)
    base.turn(90)
    open_pipe_second()
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
