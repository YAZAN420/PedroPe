from config import *
from pybricks.tools import wait, StopWatch  # type: ignore
from Utils import *
from mainFunctions import *
from AccTwoEnc import *
from syncCtrl import *


def testUpMotor():
    while True:
        up_motor.run(-800)
        ev3.speaker.beep()
        wait(3000)
        up_motor.run(800)
        ev3.speaker.beep()
        wait(3000)


def testForTurn1Motor():
    down_motor.run_time(speed=-1000, time=1000)

    def see_yellow():
        ref1 = left_sensor.reflection()
        ref2 = right_sensor.reflection()
        return ref1+ref2 > 150
    line.until_method(see_yellow, speed=50)


def grap():
    up_motor.run_until_stalled(-1000, then=Stop.HOLD)
    down_motor.run_until_stalled(-1000, then=Stop.HOLD)
    down_motor.run_until_stalled(1000, then=Stop.HOLD)


def testClaws():
    reset()
    grap()
    up_motor.run(-600)
    ev3.speaker.beep()
    wait(3000)
    up_motor.run(600)
    ev3.speaker.beep()
    wait(3000)


def put2BlockOn2Block():
    up_motor.run_until_stalled(-80, then=Stop.HOLD)
    down_motor.run(-600)
    wait(2000)
    down_motor.run(600)
    wait(2000)
    up_motor.run_until_stalled(500, then=Stop.HOLD, duty_limit=85)
    wait(5000)
    up_motor.run_until_stalled(-6000, then=Stop.HOLD, duty_limit=75)


def lineAndTurn():
    up_motor.run_until_stalled(-80, then=Stop.HOLD)
    wait_for_button_press()
    line.correct()
    line.followUntilSensor(-70, "right")
    line.follow_cm(-70, 7.5)

    line.correct()
    line.stop_at_joint(-70)


def testClaws2():
    up_motor.run_until_stalled(1000, then=Stop.HOLD)
    down_motor.run_until_stalled(1000, then=Stop.HOLD)
    down_motor.run(-500)
    wait(500)
    up_motor.run_until_stalled(-1000, then=Stop.HOLD)


def correctTest():
    while True:
        wait_for_button_press()
        line.correct()


def test_for_steering():
    while True:
        wait_for_button_press()
        downClaw()
        base.move_until_method(see_black, 1000)
        base.sync_acc(100)
        upClaw()
        base.stop()
        move_steering(380, 40)
        wait(2000)
        resetDetectedColor(angle=170)
        wait(5000)
        downClaw()
        wait(5000)
        wait(200)
        base.move_until_method(see_yellow_small, speed=300)
        take4block()


def testleaveblocksagain():
    downClaw()
    wait(2000)
    down_motor.run_time(speed=-1000, time=3500, wait=True)
    leaveblocks()
    wait(2000)
    down_motor.stop()
    up_motor.stop()
    wait(10000)


def lineTest():
    while True:
        wait_for_button_press()
        line.correct()
        line.follow_cm(40)


def testU():
    wait_for_button_press()
    line.correct()
    line.followUntilSensorright(-70)
    base.move_mm(100, 250)
    base.turn(90)
    base.stop_and_hold()
    line.correct()
    line.stop_at_joint(-70)
    base.move_mm(100, 250)
    base.turn(-90)
    line.correct()
    line.stop_at_joint(-70)
    base.turn(180)
    line.correct()
    line.followUntilSensorright(-70)
    base.move_mm(100, 450)
    base.turn(90)
    line.correct()
    line.stop_at_joint(-70)
    base.move_mm(100, 250)
    base.turn(-90)
    line.correct()
    line.stop_at_joint(-85)
    base.turn(180)
    line.correct()
    down_motor.run(500)


def printValues(sensor):
    while True:
        wait(200)
        r, g, b = sensor.rgb()
        h, s, v = sensor.hsv()
        wait(200)
        ref = sensor.reflection()
        wait(200)
        # amp = sensor.ambient()
        print(r)
        print(g)
        print(b)
        print(h)
        print(s)
        print(v)
        print(ref)
        # print(amp)
        print("______________________________")


def testBlocks():
    down_motor.run_time(400, 300*1.5, then=Stop.HOLD, wait=True)
    down_motor.run(600)
    print("1")
    up_motor.run_angle(speed=300, rotation_angle=60, then=Stop.HOLD, wait=True)
    print("2")
    base.move_mm(55, 70)
    print("3")
    up_motor.run_time(-300, 400)
    print("4")
    down_motor.stop()
    down_motor.run_angle(speed=-1000, rotation_angle=150,
                         then=Stop.HOLD, wait=True)


def tmpTest():
    while True:
        wait_for_button_press()
        reset()
        wait(2000)
        up_motor.stop()
        down_motor.stop()


def syncAccTest():
    AccTwoEnc.config(200, 1000, 250, 250, 1200)
    SyncCtrl.config(0.012, 0, 400, 400)
    done = False
    s = 0
    sABS = 0
    cnt = 0
    while not done:
        el = left_motor.angle()
        er = right_motor.angle()
        s += el - er
        sABS += abs(el-er)
        cnt += 1
        power, done = AccTwoEnc.calculate(el, er)
        powerB, powerC = SyncCtrl.calculateWithSpeed(el, er, power, power)
        left_motor.run(powerB)
        right_motor.run(powerC)
    base.stop_and_hold()
    print(s/cnt)
    print(sABS/cnt)


def syncAccTest2():
    while True:
        base.sync_acc(500)
        base.sync_acc(-500)


def syncAccTest3():
    base.settings(straight_speed=10000, straight_acceleration=700)
    while True:
        base.straight(200)
        wait(400)
        base.straight(-200)
        wait(400)


def syncTest():
    SyncCtrl.config(0.012, 0, 400, 400)
    done = False
    s = 0
    sABS = 0
    cnt = 0
    while not done:
        el = left_motor.angle()
        er = right_motor.angle()
        s += el - er
        sABS += abs(el-er)
        cnt += 1
        power = 500
        powerB, powerC = SyncCtrl.calculateWithSpeed(el, er, power, power)
        left_motor.run(powerB)
        right_motor.run(powerC)
    base.stop_and_hold()
    print(s/cnt)
    print(sABS/cnt)


def testDedected():
    downClaw()
    resetDetectedColor()
    printValues()


def littleDown():
    up_motor.run_angle(-600, 25)


def littleUp():
    base.stop_and_hold()
    wait(100)
    base.move_mm(4, 100)
    wait(100)
    up_motor.run_angle(600, 25)
    base.drive(-100, 0)


def testforputblockonblock():
    while (True):
        downClaw()
        wait(4000)
        putBlockOnBlock()


def leaveTest():
    upClaw()
    up_motor.run_angle(-300, 65)
    wait(2000)
    base.drive(-100, 0)
    wait(620)
    littleDown()
    wait(1000)
    littleUp()
    wait(260)
    littleDown()
    wait(1000)
    littleUp()
    wait(1000)
    base.stop_and_hold()


def testgar():
    def little1Down():
        up_motor.run_until_stalled(-1000, duty_limit=100, then=Stop.HOLD)

    def little1Up():
        up_motor.run_angle(600, 90)
    upClaw()
    up_motor.run_angle(-300, 60)
    wait(2000)
    base.drive(-100, 0)
    wait(500)
    base.stop_and_hold()
    littleDown()
    littleUp()
    base.drive(-100, 0)
    wait(530)
    base.stop_and_hold()
    littleDown()

    base.drive(-100, 0)
    wait(900)
    littleUp()
    base.drive(-100, 0)
    wait(480)
    base.stop_and_hold()
    littleDown()
    base.stop_and_hold()
    base.drive(-100, 0)
    wait(900)
    base.stop_and_hold()
    littleUp()


def follow_test():
    downClaw()
    while True:
        wait_for_button_press()
        line.follow_cm(30)


def test_pipe():
    while True:
        reset()
        wait(2000)
        downClaw()
        wait(2000)
        up_motor.run_angle(speed=80000, rotation_angle=30, wait=False)
        down_motor.run_angle(speed=-1000, rotation_angle=260, wait=False)
        wait(6000)


def testleftandrirght():
    while True:
        wait(2000)
        left_motor.reset_angle(0)
        right_motor.reset_angle(0)
        wait(500)
        left_motor.run_angle(speed=4000, rotation_angle=719, wait=False)
        right_motor.run_angle(speed=4000, rotation_angle=719, wait=True)
        left_motor.hold()
        right_motor.hold()
        print(left_motor.angle())
        print(right_motor.angle())
        wait(2000)
        left_motor.reset_angle(0)
        right_motor.reset_angle(0)
        wait(500)
        left_motor.run_angle(speed=-4000, rotation_angle=719, wait=False)
        right_motor.run_angle(speed=-4000, rotation_angle=719, wait=True)
        left_motor.hold()
        right_motor.hold()
        print(left_motor.angle())
        print(right_motor.angle())


def testForSortingRYYR():
    downClaw()
    wait(4000)
    down_motor.run_time(1000, 300*1.5)
    down_motor.run_time(speed=-1000, time=3500, wait=True)
    down_motor.run_angle(speed=1000, rotation_angle=140, wait=True)
    # base.move_mm(150,-100)
    upClaw()
    base.sync_acc(-200, 100)
    downClaw()
    down_motor.run_time(1000, 300*1.5)
    base.sync_acc(-60, 100)
    upClaw()
    base.sync_acc(300, 100)
    wait(4000)
    print("1")
    up_motor.run_angle(speed=-1000, rotation_angle=80, wait=True)
    print("2")
    down_motor.run_angle(speed=-1000, rotation_angle=100)
    print("3")
    base.sync_acc(-15, 100)
    print("4")
    up_motor.run_angle(speed=-1000, rotation_angle=25, wait=True)
    print("5")
    base.sync_acc(-120, 100)
    print("6")
    upClaw()
    print("7")
    base.sync_acc(-180, 100)
    print("8")
    downClaw()
    print("9")
    down_motor.run_time(speed=1000, time=3500, wait=True)
    print("10")


def testagainforput4():
    downClaw()
    down_motor.run_time(1000, 300*1.5)
    down_motor.run_time(speed=-1000, time=3500, wait=True)
    down_motor.run_angle(speed=1000, rotation_angle=140, wait=True)
    # upClaw()
    up_motor.run_until_stalled(400, then=Stop.HOLD, duty_limit=70)
    base.sync_acc(-210, 100)
    downClaw()
    down_motor.run_time(1000, 300*1.5)
    base.sync_acc(-50, 100)
    upClaw()
    base.sync_acc(270, 100)
    # base.move_mm(270,100)
    up_motor.run_angle(speed=-1000, rotation_angle=90, wait=True)
    # base.turn(5)
    print("2")
    down_motor.run_angle(speed=-1000, rotation_angle=100)
