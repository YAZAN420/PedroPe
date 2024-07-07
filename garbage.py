from config import *
from mainFunctions import *
from tests import *
from mainFunctions import *

class garbage:

    @classmethod
    def reset_to_down_sen(cls):
        downClaw()
        down_motor.run_angle(speed=-1000, rotation_angle=245)
        # printValues()

    @classmethod
    def open_pipe1(cls):
        
        line.until_method(see_white)
        print("done")
        base.move_mm(100, 400)
        wait(200)
        left_motor.run_angle(speed=500, rotation_angle=21)
        up_motor.run_angle(speed=8000, rotation_angle=80, wait=False)
        down_motor.run_angle(speed=-1000, rotation_angle=260, wait=False)
        base.move_mm(450, 400)
        downClaw()
        base.move_mm(50, -400)
        base.move_mm(50, 400)
        upClaw()
        downClaw()
        # wait(200)
        # up_motor.run_angle(speed=-1000, rotation_angle=55)
        # wait(200)
        # up_motor.run_angle(speed=1000, rotation_angle=30)
        # wait(200)
        # left_motor.run_angle(speed=500, rotation_angle=12)
        # base.move_mm(23, 200)
        # down_motor.run_time(speed=-1000, time=200, wait=False)
        # upClaw()

    @classmethod
    def open_pipe2(cls):
        downClaw()
        line.correct()
        line.follow_cm(37)
        line.until_method(see_white,speed=40)
        up_motor.run_angle(speed=800, rotation_angle=20, wait=False)
        down_motor.run_angle(speed=-1000, rotation_angle=260, wait=False)
        wait(100)
        base.turn(-14)
        up_motor.run_time(speed=800, time=500, wait=False)
        base.syncAcc(750, acc=900)
        # wait(200)
        # base.move_sideway(160, 30, 1)
        # wait(200)
        # base.syncAcc(60, acc=900)
        # wait(2000)
        # down_motor.run_time(speed=-1000, time=200, wait=False)
        # upClaw()

    @classmethod
    def take_debris(cls):
        downClaw()
        base.syncAcc(-390, 500)
        base.turn(77)
        upClaw()
        down_motor.stop()
        base.syncMoveMm(90, 1000)
        down_motor.run_time(speed=10000, time=700, wait=False)
        up_motor.run_time(speed=-400, time=700, wait=False)
        base.syncAcc(270, acc=1000)
        downClaw()
        down_motor.hold()
        base.move_until_method(lambda: left_sensor.reflection() > 70, 200)

    @classmethod
    def run(cls):
        cls.open_pipe1()
        cls.take_debris()
        base.syncAcc(130, 800)
        base.turn(75)
        base.turn_until_method(lambda: left_sensor.reflection() > 80,speed=100)
        base.turn_until_method(lambda: left_sensor.reflection() < 30,speed=100)
        cls.open_pipe2()
        
        # base.turn(-45)
        # base.syncAcc(250)
        # reset()
        # base.syncAcc(-500)
        # base.turn(45)
