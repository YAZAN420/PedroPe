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
    base.syncAcc(-400, 700)
    base.stop()
    left_motor.run_time(90, 900)
    take4block(600, 1)
    base.syncAcc(-470, 200)
    base.turn(-80)
    base.move_mm(250, -200)
    base.stop_and_hold()
    down_motor.run_time(400, 220*1.5, then=Stop.HOLD, wait=True)
    upClaw()
    reset()
    base.syncAcc(200, 60)
    downClaw()
    base.turn(-180)
    up_motor.stop()
    down_motor.stop()
    base.syncAcc(-900, 450)
    base.turn(-120)
    base.stop()
    left_motor.run_time(-350, 800, then=Stop.HOLD, wait=True)
    downClaw()
    down_motor.stop()
    down_motor.run_time(1000, 400, then=Stop.HOLD, wait=True)
    take4block(300)


def take4block(speed, num=0):
    resetDetectedColor()
    moveUntilBlock(speed)
    base.syncMoveMm(160, 150)
    putBlockOnBlock()
    base.straight(-20)
    downClaw()
    make2BlocksGood()
    down_motor.run_time(1000, 220*1.5, then=Stop.HOLD, wait=True)
    upClaw()
    # if (num == 1):
    #     base.move_mm(45, 200)
    #     downClaw(duty=50)
    #     upClaw()
    #     base.straight(70)
    # else:
    base.straight(100)
    downClaw()
    base.move_mm(80, 150)
    putBlockOnBlock()
    base.straight(-20)
    downClaw()
    make2BlocksGood()


def resetDetectedColor(angle=200):
    down_motor.run_angle(speed=-10000, rotation_angle=angle,
                         then=Stop.HOLD, wait=True)


def make2BlocksGood():
    down_motor.run_time(1000, 300*1.5, then=Stop.HOLD, wait=True)
    base.straight(-25)
    down_motor.run_time(-1000, 220*3, then=Stop.HOLD, wait=True)


def downClaw(duty=40):
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
