from config import *
from Utils import *


def putBlockOnBlock():
    down_motor.run_time(400, 300*1.5, then=Stop.HOLD, wait=True)
    down_motor.run(600)
    up_motor.run_angle(speed=300, rotation_angle=60, then=Stop.HOLD, wait=True)
    base.syncAcc(50, 600)
    up_motor.run_time(-250, 300)
    down_motor.stop()
    down_motor.run_angle(speed=-1000, rotation_angle=150,
                         then=Stop.HOLD, wait=True)


def see_yellow_big():
    ref1 = left_sensor.reflection()
    ref2 = right_sensor.reflection()
    return ref1+ref2 > 130


def see_white():
    ref1 = left_sensor.reflection()
    ref2 = right_sensor.reflection()
    return ref1+ref2 > 130


def see_yellow_small():
    h, s, v = left_sensor.hsv()
    return v > 20


def take8Blocks():
    left_motor.run_angle(speed=-700, rotation_angle=230)
    wait(100)
    right_motor.run_angle(speed=-700, rotation_angle=260)
    wait(100)
    resetDetectedColor()
    wait(100)
    moveUntilBlock(500)
    take4block()
    base.syncAcc(-300)
    base.move_until_method(see_white, -250)
    wait(100)
    base.syncAcc(60, 250)
    base.turn(-110)
    base.move_mm(170, -1000)
    down_motor.run_time(speed=10000, time=400, wait=False)
    up_motor.run_time(speed=1000, time=800, wait=False)
    wait(500)  # do not change to be fast
    base.syncAcc(600, 500)
    upMotorResetWithTrueOrFalse(speed=-1000, bool=True)
    base.move_until_method(see_black, speed=1000)
    upMotorResetWithTrueOrFalse(speed=1000, bool=False)
    downMotorResetTrueOrFalse(1000, False)
    base.syncAcc(100)
    upMotorResetWithTrueOrFalse(speed=1000, bool=False)
    base.stop()
    move_steering(380, 35)
    wait(400)
    resetDetectedColor(angle=145)
    base.syncAcc(-30)
    downClaw()
    base.stop()
    right_motor.run_angle(speed=-1000, rotation_angle=200)
    wait(200)
    left_motor.run_angle(speed=-1000, rotation_angle=180)
    wait(200)
    base.move_until_method(see_yellow_small, speed=300)
    wait(100)
    take4block()


def goToFirstSafahAfterHotam():
    base.syncAcc(-400)
    base.stop()
    down_motor.run_time(speed=1000, time=700, wait=False)
    right_motor.run_time(speed=-300, time=400)
    base.syncAcc(-400)


def goToLineAfterSafah():
    downClaw()
    # base.move_until_method(see_yellow_small,speed=-300)
    base.syncAcc(140)
    base.turn(70)
    base.move_mm(20, 300)
    down_motor.run_time(speed=-400, time=300)
    base.turn_until_method(lambda: front_sensor.reflection() < 15, speed=100)
    line.correct(duration=0.35)
    line.until_method(see_yellow_big, speed=50)


def take4block():
    base.move_mm(130, 400)
    putBlockOnBlockWithGood()
    down_motor.run_time(1000, 220*1.5, then=Stop.HOLD, wait=True)
    up_motor.run_angle(speed=1000, rotation_angle=90, wait=False)
    wait(135)
    base.syncAcc(100)
    downClaw()
    base.move_mm(65, 400)
    putBlockOnBlockWithGood(False)
    wait(130)


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


def resetStart():
    down_motor.run_time(speed=1000, time=600, wait=False)
    up_motor.run_time(speed=-1000, time=600, wait=False)


def move_from_blocks_to_line():
    wait(100)
    base.stop()
    base.settings(turn_acceleration=600, turn_rate=10000)
    base.turn(-90)
    up_motor.run_time(speed=-300, time=700, wait=False)
    down_motor.run_time(speed=1000, time=600, wait=False)
    base.syncAcc(100, acc=1000)
    base.move_until_method(see_black, speed=350)
    base.move_mm(distance_in_mm=100, speed=500)
    base.turn(65)
    base.turn_until_method(lambda: right_sensor.reflection() < 15, speed=140)
    line.correct()
    line.follow_cm(12)
    line.until_method(see_white)
    base.syncAcc(225)
    down_motor.run_angle(speed=-1000, rotation_angle=160, wait=False)
    wait(100)
    base.turn(90)
    up_motor.run_time(speed=1000, time=500, wait=False)
    wait(200)
    base.syncAcc(275)
    down_motor.run_time(speed=1000, time=400, wait=False)
    up_motor.run_time(speed=-1000, time=700, wait=True)
    base.stop()
    left_motor.run_time(speed=400, time=200)
    base.move_until_method(see_black, 350)
    base.syncAcc(100)
    wait(100)
    base.turn(70)
    wait(100)
    base.turn_until_method(lambda: left_sensor.reflection() > 80, speed=120)
    base.turn_until_method(lambda: left_sensor.reflection() < 30, speed=120)
    line.correct()
    down_motor.run_time(speed=-1000, time=400, wait=False)
    line.follow_cm(32)


def putBlockOnBlockWithGood(lastWait=True):
    putBlockOnBlock()
    up_motor.run_time(speed=-400, time=600, wait=False)
    wait(100)
    make2BlocksGood(lastWait)


def resetDetectedColor(angle=191):
    down_motor.run_angle(speed=-10000, rotation_angle=angle,
                         then=Stop.HOLD, wait=False)


def make2BlocksGood(lastWait):
    down_motor.run_time(1000, 300*1.5, wait=False)
    base.syncAcc(-35)
    down_motor.run_time(-1000, 220*3, wait=lastWait)


def akbs():
    down_motor.run_angle(400, 150)
    base.syncAcc(-40)
    upClaw()
    reset()
    up_motor.run_time(speed=-1000, time=640, wait=False)
    down_motor.run_time(speed=-1000, time=640)
    reset()


def downClaw(duty=70):
    up_motor.run_until_stalled(-6000, then=Stop.HOLD, duty_limit=duty)


def upClaw():
    up_motor.run_until_stalled(1000, then=Stop.HOLD, duty_limit=110)


def moveUntilBlock(speed):
    base.move_until_method(lambda: front_sensor.rgb()[0] > 4, speed)


def reset():
    up_motor.run(1000)
    down_motor.run(1000)
    up_motor.run_until_stalled(6000, then=Stop.HOLD, duty_limit=75)
    wait(200)
    down_motor.hold()
    up_motor.hold()


def upMotorResetWithTrueOrFalse(speed=1000, bool=True):
    up_motor.run_time(speed=speed, time=700, wait=bool)


def downMotorResetTrueOrFalse(speed=1000, bool=True):
    down_motor.run_time(speed=speed, time=700, wait=bool)


def see_black():
    fir = left_sensor.reflection()
    sec = right_sensor.reflection()
    return fir+sec < 35


def make2buildRedAndYellow(mode):
    base.move_until_method(see_yellow_small, -400)
    wait(200)
    base.syncAcc(220 if mode == 1 else 15)
    base.turn(70)
    base.move_mm(20, 300)
    base.turn_until_method(lambda: front_sensor.reflection() < 15, speed=100)
    line.correct(duration=0.35)
    line.until_method(see_yellow_big, speed=100)
    base.move_mm(140, 300)
    wait(200)
    base.turn(100 * (-1 if mode == 1 else 1))
    base.move_mm(10, 400)
    leaveblocks()


def leaveblocks():
    base.stop()
    down_motor.run_time(speed=1000, time=440, wait=True)
    down_motor.run_angle(speed=-1000, rotation_angle=40, wait=True)
    base.syncAcc(-130)
    base.syncAcc(15)
    upClaw()
    base.syncAcc(-190)
    downClaw()
    down_motor.run_time(speed=1000, time=450)
    base.syncAcc(-45)
    up_motor.run_angle(speed=300, rotation_angle=90)
    base.syncAcc(360, 190)
    base.stop()
    # uninstall
    up_motor.run_time(speed=-300, time=260)
    down_motor.run_angle(speed=-1000, rotation_angle=90)
    upClaw()
    base.syncAcc(-80)
    down_motor.run_angle(speed=600, rotation_angle=8)
    up_motor.stop()
    up_motor.run_time(speed=-400, time=800)
    base.syncAcc(-90)
    upClaw()
    base.syncAcc(-110)
    wait(200)
    # # yellow build
    down_motor.run_angle(speed=-1000, rotation_angle=20, wait=False)
    downClaw()
    down_motor.run_time(speed=1000, time=450)
    base.syncAcc(-50)
    up_motor.run_angle(speed=300, rotation_angle=120)
    base.syncAcc(115)
    up_motor.run_time(-250, 400)
    down_motor.run_angle(speed=-1000, rotation_angle=100)
    base.syncAcc(-200)
