from config import *
from mainFunctions import *
from tests import *


class garbage:

    @classmethod
    def move_until_white(cls, sensor=front_sensor):
        base.start_tank(60, 60)
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
        left_motor.run_angle(speed=500, rotation_angle=44)
        up_motor.run_angle(speed=800, rotation_angle=60, wait=False)
        down_motor.run_angle(speed=-1000, rotation_angle=260, wait=False)
        base.move_mm(440, 300)
        wait(200)
        up_motor.run_angle(speed=-1000, rotation_angle=32)
        wait(200)
        left_motor.run_angle(speed=500, rotation_angle=14)
        base.move_mm(15, 200)
        upClaw()

    @classmethod
    def open_pipe2(cls):
        downClaw()
        line.correct()
        line.stop_at_white()
        up_motor.run_angle(speed=800, rotation_angle=60, wait=False)
        down_motor.run_angle(speed=-1000, rotation_angle=260, wait=False)
        base.syncAcc(640,acc=900)
        

    @classmethod
    def take_debris(cls):
        downClaw()
        base.syncAcc(-410, 500)
        base.turn(82)
        upClaw()
        base.syncMoveMm(90, 1000)
        up_motor.run_time(speed=-400, time=600, wait=False)
        base.syncAcc(300, acc=900)
        cls.move_until_white(left_sensor)
        up_motor.stop()
        up_motor.hold()

    @classmethod
    def run(cls):
        print("running garbage: ")
        reset()
        cls.open_pipe1()
        cls.take_debris()
        wait(100)
        base.syncAcc(70)
        wait(100)
        base.turn(90)
        wait(2000)
        reset()
        cls.open_pipe2()   
