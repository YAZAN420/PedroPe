from config import *
from Utils import *


def putBlockOnBlock():
    down_motor.run_time(400, 300*1.5, then=Stop.HOLD, wait=True)
    down_motor.run(600)
    up_motor.run_angle(speed=300, rotation_angle=60, then=Stop.HOLD, wait=True)
    base.syncAcc(51, 600)
    up_motor.run_time(-250, 300)
    down_motor.stop()
    down_motor.run_angle(speed=-1000, rotation_angle=150,
                         then=Stop.HOLD, wait=True)


def see_white():
    ref1 = left_sensor.reflection()
    ref2 = right_sensor.reflection()
    return ref1+ref2 > 170


def take8Blocks():
    downClaw()
    left_motor.run_angle(speed=-700, rotation_angle=240)
    right_motor.run_angle(speed=-700, rotation_angle=240)
    # left_motor.run_time(speed=300, time=400)
    resetDetectedColor()
    wait(300)
    moveUntilBlock(500)
    take4block()
    # down_motor.run_time(440, 220*3, then=Stop.HOLD, wait=True)
    base.move_until_method(see_white, -400)
    #
    wait(100)
    base.syncAcc(90, 200)
    base.turn(-110)
    # wait(6000)
    base.move_mm(170, -300)
    down_motor.run_time(speed=10000, time=250)
    print("done")
    up_motor.run_time(speed=1000, time=800, wait=False)
    wait(500)
    base.syncAcc(920, 250)
    upClaw()
    base.move_mm(40, 120)
    # base.move_mm(20, -90)
    reset()
    base.turn(90)
    resetDetectedColor()
    downClaw()
    base.move_mm(20, -200)
    wait(200)
    base.move_sideway(170, -50, 0)
    moveUntilBlock(300)
    take4block()


def take4block():
    base.move_mm(150, 200)
    putBlockOnBlockWithGood()
    down_motor.run_time(1000, 220*1.5, then=Stop.HOLD, wait=True)
    upClaw()
    base.syncAcc(100)
    downClaw()
    base.move_mm(85, 200)
    putBlockOnBlockWithGood()


def resetStart():
    down_motor.run_time(speed=1000, time=600, wait=False)
    up_motor.run_time(speed=-1000, time=600, wait=False)


def move_from_blocks_to_line():
    wait(100)
    base.stop()
    base.settings(turn_acceleration=600, turn_rate=10000)
    base.turn(-90)
    up_motor.run_time(speed=-300, time=700, wait=False)
    base.syncAcc(100, acc=1000)
    base.move_until_method(see_black, speed=300)
    base.move_mm(distance_in_mm=100, speed=400)
    base.turn(75)
    base.turn_until_method(lambda: right_sensor.reflection() < 15, speed=120)
    line.correct()
    down_motor.run_time(speed=1000, time=800, wait=False)
    line.follow_cm(10)
    line.until_method(see_white)
    base.syncAcc(215)
    down_motor.run_angle(speed=-1000, rotation_angle=160, wait=False)
    wait(100)
    base.turn(98)
    wait(100)
    base.syncAcc(295)
    wait(100)
    down_motor.run_time(speed=1000, time=400, wait=False)
    base.move_until_method(see_black,200)
    base.syncAcc(100)
    wait(100)
    base.turn(80)
    wait(100)
    base.turn_until_method(lambda: left_sensor.reflection() > 80, speed=100)
    base.turn_until_method(lambda: left_sensor.reflection() < 30, speed=100)
    line.correct()
    down_motor.run_time(speed=-1000, time=400, wait=False)
    line.follow_cm(30)


def putBlockOnBlockWithGood():
    putBlockOnBlock()
    up_motor.run_time(speed=-400, time=600, wait=False)
    wait(200)
    make2BlocksGood()


def resetDetectedColor(angle=191):
    down_motor.run_angle(speed=-10000, rotation_angle=angle,
                         then=Stop.HOLD, wait=False)


def make2BlocksGood():
    down_motor.run_time(1000, 300*1.5)
    base.syncAcc(-35)
    down_motor.run_time(-1000, 220*3)


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


def see_black():
    fir = left_sensor.reflection()
    sec = right_sensor.reflection()
    return fir+sec < 35


def make2buildRedAndYellow(mode):
    def see_yellow_one():
        h, s, v = left_sensor.hsv()
        return v > 20
    base.move_until_method(see_yellow_one, -400)
    wait(200)
    base.syncAcc(205 if mode == 1 else 10)
    base.turn(110)
    base.move_mm(170, -300)
    base.stop_and_hold()
    wait(4000)
    downClaw()
    down_motor.run_time(speed=-1000, time=200, wait=False)
    base.move_until_method(see_black, speed=250)
    # wait(1000)
    # line.correct(duration=0.35)

    def see_yellow():
        ref1 = left_sensor.reflection()
        ref2 = right_sensor.reflection()
        return ref1+ref2 > 150
    line.until_method(see_yellow, speed=50)
    base.move_mm(140, 300)
    wait(200)
    base.turn(98 * (-1 if mode == 1 else 1))
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
    down_motor.run_time(speed=1000, time=420)
    base.syncAcc(-45)
    up_motor.run_angle(speed=300, rotation_angle=90)
    base.syncAcc(365, 200)
    base.stop()
    # uninstall
    up_motor.run_time(speed=-300, time=300)
    down_motor.run_angle(speed=-1000, rotation_angle=90)
    upClaw()
    base.syncAcc(-75)
    down_motor.run_angle(speed=600, rotation_angle=8)
    up_motor.stop()
    up_motor.run_time(speed=-400, time=800)
    base.syncAcc(-90)
    upClaw()
    base.syncAcc(-110)
    # base.syncAcc(30)
    wait(200)
    # # yellow build
    down_motor.run_angle(speed=-1000, rotation_angle=20, wait=False)
    downClaw()
    down_motor.run_time(speed=1000, time=420)
    base.syncAcc(-50)
    up_motor.run_angle(speed=300, rotation_angle=120)
    base.syncAcc(115)
    # left_motor.run_angle(speed=300, rotation_angle=10)
    up_motor.run_time(-250, 400)
    # down_motor.run_time(speed=-1000, time=400)
    down_motor.run_angle(speed=-1000, rotation_angle=100)
    base.syncAcc(-200)
