from config import *
from mainFunctions import *
from tests import *


class garbage:

    @classmethod
    def move_until_white(cls, sensor=front_sensor):
        base.start_tank(70, 70)
        while (True):
            ref = sensor.reflection()
            if (ref > 70):
                break
        base.stop_and_hold()

    @classmethod
    def reset_to_down_sen(cls):
        downClaw()
        down_motor.run_angle(speed=-1000, rotation_angle=245)
        # printValues()

    @classmethod
    def open_pipe1(cls):
        downClaw()
        line.correct()
        line.stop_at_white()
        base.move_mm(120, 300)
        wait(200)
        left_motor.run_angle(speed=500, rotation_angle=47)
        wait(200)
        up_motor.run_angle(speed=8000, rotation_angle=60, wait=False)
        wait(200)
        down_motor.run_angle(speed=-1000, rotation_angle=260, wait=False)
        base.move_mm(430, 300)
        wait(200)
        up_motor.run_angle(speed=-1000, rotation_angle=40)
        wait(200)
        left_motor.run_angle(speed=500, rotation_angle=12)
        base.move_mm(23, 200)
        down_motor.run_time(speed=-1000, time=200, wait=False)
        upClaw()

    @classmethod
    def open_pipe2(cls):
        downClaw()
        line.correct()
        line.follow_cm(35)
        line.stop_at_white()
        up_motor.run_angle(speed=800, rotation_angle=20, wait=False)
        down_motor.run_angle(speed=-1000, rotation_angle=260, wait=False)
        wait(200)
        base.syncAcc(520, acc=900)
        wait(200)
        base.move_sideway(160, 30, 1)
        wait(200)
        base.syncAcc(60, acc=900)
        wait(2000)
        down_motor.run_time(speed=-1000, time=200, wait=False)
        upClaw()

    @classmethod
    def take_debris(cls):
        downClaw()
        base.syncAcc(-390, 500)
        base.turn(77)
        upClaw()
        down_motor.stop()
        base.syncMoveMm(90,1000)
        down_motor.run_time(speed=10000, time=700, wait=False)
        up_motor.run_time(speed=-400, time=700, wait=False)
        base.syncAcc(300, acc=880)
        downClaw()
        down_motor.hold()
        cls.move_until_white(left_sensor)

    @classmethod
    def run(cls):
        print("running garbage: ")
        # reset()
        # cls.open_pipe1()
        # cls.take_debris()
        # base.syncAcc(130)
        # base.turn(75)
        # base.turn_until_method(lambda: left_sensor.reflection() > 80)
        # base.turn_until_method(lambda: left_sensor.reflection() < 30)
        cls.open_pipe2()
        base.syncAcc(-100)
        base.turn(-45)
        base.syncAcc(250)
        reset()
        base.syncAcc(-500)
        base.turn(45)
        
