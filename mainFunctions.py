from garbage import run
from config import *
from Utils import *
from garbage import *


def see_black():
    fir = left_sensor.reflection()
    sec = right_sensor.reflection()
    return fir+sec < 30


def see_blue_right():
    h, s, v = right_sensor.hsv()
    return h > 170


def see_black_front():
    sec = front_sensor.reflection()
    return sec < 20


def see_red():
    ref2 = front_sensor.color()
    return ref2 == Color.RED


def see_white():
    ref1 = left_sensor.reflection()
    ref2 = right_sensor.reflection()
    return ref1+ref2 > 170


def see_white_front():
    ref1 = front_sensor.reflection()
    return ref1 > 80


def see_yellow_big():
    ref1 = left_sensor.reflection()
    ref2 = right_sensor.reflection()
    return ref1+ref2 > 170


def see_yellow_small():
    h, s, v = left_sensor.hsv()
    return v > 20


def see_yellow_small2():
    h, s, v = right_sensor.hsv()
    return v > 20


def open_pipe1():
    line.until_method(see_white, speed=40)
    wait(200)
    base.sync_acc(100)
    wait(100)
    base.turn(9)
    # up_motor.run_angle(speed=8000, rotation_angle=80, wait=False)
    down_motor.run_angle(speed=-1000, rotation_angle=200, wait=False)
    # base.sync_acc(505)
    base.sync_acc(420)
    down_motor.run_time(speed=1000, time=1000, wait=False)
    wait(200)
    base.sync_acc(80)
    openpipfun()
    # base.move_mm(50, -400)
    # up_motor.stop()


def putBlockOnBlock():
    down_motor.run_time(400, 300*1.5, then=Stop.HOLD, wait=True)
    down_motor.run(600)
    up_motor.run_angle(speed=300, rotation_angle=60,
                       then=Stop.HOLD, wait=False)
    wait(110)
    base.sync_acc(50, 600)
    up_motor.run_time(-250, 300, wait=False)
    wait(110)
    down_motor.stop()
    down_motor.run_angle(speed=-1000, rotation_angle=150,
                         then=Stop.HOLD, wait=True)


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
    down_motor.run_time(speed=10000, time=400, wait=False)
    up_motor.run_time(speed=1000, time=800, wait=False)
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
    down_motor.run_time(1000, 220*1.5, then=Stop.HOLD, wait=True)
    up_motor.run_angle(speed=1000, rotation_angle=90, wait=False)
    wait(135)
    base.sync_acc(100)
    downClaw()
    base.move_mm(65, 400)
    putBlockOnBlockWithGood(False)
    wait(210)


def make2buildRedAndYellow(mode):
    base.move_until_method(see_yellow_small, -400)
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
    base.turn(30 * (-1 if mode == 1 else 1))
    base.turn_until_method(see_black_front, 250*(-1 if mode == 1 else 1))
    base.turn_until_method(see_red, 250*(-1 if mode == 1 else 1))
    base.turn(7 * (-1 if mode == 1 else 1))
    base.move_mm(10, 400)
    leaveblocks()


def leaveblocks():
    base.stop()
    down_motor.run_time(speed=1000, time=440, wait=True)
    down_motor.run_angle(speed=-1000, rotation_angle=40, wait=True)
    base.sync_acc(-130)
    base.sync_acc(15)
    upClaw()
    base.sync_acc(-190)
    downClaw()
    down_motor.run_time(speed=1000, time=450)
    base.sync_acc(-45)
    up_motor.run_angle(speed=300, rotation_angle=90)
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
    down_motor.run_angle(speed=-1000, rotation_angle=100)
    base.sync_acc(-150)


def from_blocks_to_hotam_four(mode):
    downClaw()
    base.turn(50)
    base.move_mm(30, 600)
    base.move_until_method(see_black, 600)
    base.move_mm(30, 600)
    base.turn(100, 900)
    base.turn_until_method(lambda: right_sensor.reflection() < 7, 200)
    wait(100)
    open_pipe1()
    base.sync_acc(-30)
    up_motor.run_time(speed=-500, time=1000, wait=False)
    wait(470)
    downMotorResetTrueOrFalse(1000)
    base.sync_acc(-200)
    down_motor.run_angle(rotation_angle=-220, speed=1000, wait=False)
    base.sync_acc(30)
    downMotorResetTrueOrFalse(1000, False)
    base.sync_acc(-240)
    up_motor.run_angle(rotation_angle=60, speed=1000)
    base.turn(80)
    down_motor.run_angle(rotation_angle=120, speed=-1000)
    base.sync_acc(250)
    upMotorResetWithTrueOrFalse(-1000, False)
    wait(100)
    base.move_mm(600, -600)
    down_motor.run_angle(rotation_angle=-50, speed=550, wait=False)
    base.turn(150)
    base.move_until_method(see_blue_right, speed=400)
    if (mode == 1):
        base.turn(-100, 700)
        up_motor.run_angle(rotation_angle=50, speed=550)
        base.turn(105, 700)
        downClaw()
        base.sync_acc(360)
    else:
        base.sync_acc(360)
    downMotorResetTrueOrFalse(1000)
    up_motor.run_angle(rotation_angle=75, speed=1000, wait=False)
    base.sync_acc(-5)
    base.turn(-85)
    up_motor.stop()
    # up_motor.run_angle(rotation_angle=100, speed=-550, wait=False)
    base.move_mm(200, -1000)
    down_motor.run_time(speed=-400, time=300, wait=True)
    down_motor.run_time(speed=-1000, time=300)
    base.sync_acc(200)
    upMotorResetWithTrueOrFalse(-1000)
    base.sync_acc(300)
    base.move_until_method(see_white, 300)
    downMotorResetTrueOrFalse(1000, False)
    base.sync_acc(120)
    base.turn(90)
    base.sync_acc(440)
    openpipfun()
    up_motor.run_time(speed=-500, time=1200)
    base.turn(-90)
    upClaw()
    base.sync_acc(150)


def openpipfun():
    # down_motor.run_time(speed=-500, time=450, wait=True)
    down_motor.run_until_stalled(-1000, duty_limit=25)
    up_motor.run_angle(speed=1000, rotation_angle=200, wait=False)
    base.stop()
    left_motor.run_angle(rotation_angle=40, speed=1000)
    # base.move_mm(20, 400)


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


def moveUntilBlock(speed):
    base.move_until_method(lambda: front_sensor.rgb()[0] > 4, speed)


def resetDetectedColor(angle=191):
    down_motor.run_angle(speed=-10000, rotation_angle=angle,
                         then=Stop.HOLD, wait=False)


def resetStart():
    down_motor.run_time(speed=1000, time=600, wait=False)
    up_motor.run_time(speed=-1000, time=600, wait=False)


def downClaw(duty=70):
    up_motor.run_until_stalled(-6000, then=Stop.HOLD, duty_limit=duty)


def upClaw():
    up_motor.run_until_stalled(1000, then=Stop.HOLD, duty_limit=110)


def upMotorResetWithTrueOrFalse(speed=1000, bool=True):
    up_motor.run_time(speed=speed, time=700, wait=bool)


def downMotorResetTrueOrFalse(speed=1000, bool=True):
    down_motor.run_time(speed=speed, time=700, wait=bool)


def reset():
    up_motor.run(1000)
    down_motor.run(1000)
    up_motor.run_until_stalled(6000, then=Stop.HOLD, duty_limit=75)
    wait(200)
    down_motor.hold()
    up_motor.hold()


def close_pipe2():
    reset()
    down_motor.run_angle(speed=-1000, rotation_angle=250, wait=True)
    downClaw()
    base.move_until_method(see_white_front, speed=400)
    base.move_mm(30, 400)
    up_motor.run_time(speed=1000, time=100, wait=True)
    down_motor.run_angle(speed=1000, rotation_angle=100, wait=True)
    up_motor.run_time(speed=1000, time=800, wait=True)


def close_pipe1():
    reset()
    downClaw()
    down_motor.run_angle(speed=-1000, rotation_angle=120, wait=True)
    base.sync_acc(40)
    up_motor.run_time(speed=1000, time=800, wait=True)
    down_motor.run_time(speed=-1000, time=600, wait=True)
    base.move_mm(40, 330)
    reset()
    base.move_mm(40, 330)


def move_from_blocks_to_line():
    wait(100)
    base.stop()
    base.settings(turn_acceleration=600, turn_rate=10000)
    base.turn(-90)
    up_motor.run_time(speed=-300, time=700, wait=False)
    down_motor.run_time(speed=1000, time=600, wait=False)
    base.sync_acc(100, acc=1000)
    base.move_until_method(see_black, speed=350)
    base.move_mm(distance_in_mm=100, speed=500)
    base.turn(65)
    base.turn_until_method(lambda: right_sensor.reflection() < 15, speed=140)
    line.correct()
    line.follow_cm(12)
    line.until_method(see_white)
    base.sync_acc(225)
    down_motor.run_angle(speed=-1000, rotation_angle=160, wait=False)
    wait(100)
    base.turn(90)
    up_motor.run_time(speed=1000, time=500, wait=False)
    wait(200)
    base.sync_acc(275)
    down_motor.run_time(speed=1000, time=400, wait=False)
    up_motor.run_time(speed=-1000, time=700, wait=True)
    base.stop()
    left_motor.run_time(speed=400, time=200)
    base.move_until_method(see_black, 350)
    base.sync_acc(100)
    wait(100)
    base.turn(70)
    wait(100)
    base.turn_until_method(lambda: left_sensor.reflection() > 80, speed=120)
    base.turn_until_method(lambda: left_sensor.reflection() < 30, speed=120)
    line.correct()
    down_motor.run_time(speed=-1000, time=400, wait=False)
    line.follow_cm(32)
