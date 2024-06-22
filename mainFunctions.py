from config import *
from Utils import *


def putBlockOnBlock():
    down_motor.run_time(400, 300*1.5, then=Stop.HOLD, wait=True)
    down_motor.run(600)
    up_motor.run_angle(speed=300, rotation_angle=60, then=Stop.HOLD, wait=True)
    base.syncMoveMm(57, 70)
    up_motor.run_time(-250, 300)
    down_motor.stop()
    down_motor.run_angle(speed=-1000, rotation_angle=150,
                         then=Stop.HOLD, wait=True)


def take8Blocks():
    downClaw()
    # base.syncAcc(-400, 700)
    # base.straight(-300)
    left_motor.run_angle(speed=-300, rotation_angle=240)
    right_motor.run_angle(speed=-300, rotation_angle=270)
    # base.stop()
    left_motor.run_time(90, 700)
    take4block(500, 1)
    down_motor.run_time(440, 220*3, then=Stop.HOLD, wait=True)
    # base.syncAcc(-470, 200)
    base.straight(-330)
    base.straight(100)
    base.turn(-110)
    base.move_mm(200, -200)
    base.stop_and_hold()
    down_motor.run_time(-400, 220*1.5, then=Stop.HOLD, wait=True)
    upClaw()
    reset()
    base.move_mm(200, 100)
    downClaw()
    base.turn(-185)
    base.straight(-900)
    base.turn(-120)
    base.stop()
    left_motor.run_time(-350, 800, then=Stop.HOLD, wait=True)
    downClaw()
    down_motor.stop()
    down_motor.run_time(1000, 400, then=Stop.HOLD, wait=True)
    take4block(500)


def take4block(speed, num=0):
    resetDetectedColor()
    moveUntilBlock(speed)
    base.move_mm(150, 150)
    putBlockOnBlock()
    base.straight(-20)
    downClaw()
    make2BlocksGood()
    down_motor.run_time(1000, 220*1.5, then=Stop.HOLD, wait=True)
    upClaw()
    base.straight(100)
    downClaw()
    base.move_mm(85, 150)
    putBlockOnBlock()
    base.straight(-20)
    downClaw()
    make2BlocksGood()


def resetDetectedColor(angle=200):
    down_motor.run_angle(speed=-10000, rotation_angle=angle,
                         then=Stop.HOLD, wait=True)


def make2BlocksGood():
    down_motor.run_time(1000, 300*1.5)
    base.straight(-25)
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
    base.start_tank(speed, speed)
    while (True):
        r, g, b = front_sensor.rgb()
        if (r > 4):
            break
    base.stop_and_hold()


def reset():
    print("reset: ")
    up_motor.run(1000)
    down_motor.run(1000)
    up_motor.run_until_stalled(6000, then=Stop.HOLD, duty_limit=75)
    wait(200)
    down_motor.hold()
    up_motor.hold()
    print("reseted")
    ev3.speaker.beep()


def make2buildRedAndYellow(mode=2):
    line.stop_at_white(50)
    base.straight(-130 if mode == 1 else -320)
    base.turn(130)
    base.move_mm(300, -1000)
    base.stop_and_hold()
    downClaw(100)
    down_motor.run_time(-1000, 200, then=Stop.HOLD, wait=True)
    line.stop_at_joint(70)
    line.correct()
    line.stop_at_white(70)
    base.move_mm(100, 400)
    base.turn(-90 if mode == 1 else 90)
    base.move_mm(10, 400)
    leaveblocks()


def leaveblocks():
    base.stop()
    down_motor.run_angle(speed=1000, rotation_angle=140, wait=True)
    base.syncAcc(-130)
    upClaw()
    base.syncAcc(-175)
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
    base.syncAcc(-59)
    down_motor.run_angle(speed=600, rotation_angle=8)
    up_motor.stop()
    up_motor.run_angle(speed=-300, rotation_angle=95)
    base.syncAcc(-120)
    upClaw()
    base.syncAcc(-130)
    wait(1000)
    # # yellow build
    downClaw()
    down_motor.run_time(speed=1000, time=420)
    base.syncAcc(-50)
    up_motor.run_angle(speed=300, rotation_angle=120)
    base.syncAcc(120)
    base.stop()
    # left_motor.run_angle(speed=300, rotation_angle=10)
    up_motor.run_time(-250, 400)
    # down_motor.run_time(speed=-1000, time=400)
    down_motor.run_angle(speed=-1000, rotation_angle=100)
    base.syncAcc(-200)
