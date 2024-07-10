from config import *
from mainFunctions import *
from tests import *
from mainFunctions import *

class garbage:

    @classmethod
    def reset_to_down_sen(cls):
        downClaw()
        down_motor.run_angle(speed=-1000, rotation_angle=245)


    @classmethod
    def open_pipe1(cls):
        
        line.until_method(see_white)
        print("done")
        base.move_mm(100, 400)
        wait(200)
        left_motor.run_angle(speed=500, rotation_angle=30)
        up_motor.run_angle(speed=8000, rotation_angle=80, wait=False)
        down_motor.run_angle(speed=1000, rotation_angle=260, wait=False)
        wait(2000)
        base.move_mm(440, 400)
        # wait(2000)
        downClaw()
        wait(2000)
        # print ("5 down")
        # wait(200)
        # base.move_mm(50, 400)
        # wait(2000)
        down_motor.stop()
        down_motor.run_time(speed=-500, time=400, wait=True)
       
      
        wait(2000)
        print("close")
        # up_motor.stop()
        # wait(2000)
        # print ("up")
        up_motor.run_angle(speed=200, rotation_angle=30, wait=True)
        base.move_mm(10, 400)
        up_motor.run_angle(speed=1000, rotation_angle=200, wait=False)
        base.move_mm(20, 400)
        # left_motor.run_angle(speed=400, rotation_angle=10,wait=True)
        # up_motor.run_angle(speed=1000, rotation_angle=100, wait=False)
        # wait(2000) 
        # downClaw()..
        base.move_mm(50, -400)
        up_motor.stop()
        downClaw()
        # # base.move_mm(50, 400)
      
    

    @classmethod
    def open_pipe2(cls):
        line.correct()
        line.follow_cm(37)
        line.until_method(see_white,speed=40)
        up_motor.run_angle(speed=800, rotation_angle=20, wait=False)
        down_motor.run_angle(speed=-1000, rotation_angle=260, wait=False)
        wait(100)
        base.turn(-14)
        up_motor.run_time(speed=800, time=500, wait=False)
        base.syncAcc(650, acc=900)


    @classmethod
    def take_debris(cls):
        # down_motor.stop()
        # downClaw()
        base.syncAcc(-350, 500)
        base.turn(70) 
        upClaw()
        base.syncMoveMm(200, 1000)
        down_motor.stop()

        down_motor.run_time(speed=10000, time=700, wait=False)
        up_motor.run_time(speed=-400, time=700, wait=False)
        # base.syncAcc(270, acc=1000)
        downClaw()
        down_motor.hold()
        # base.move_until_method(lambda: left_sensor.reflection() > 70, 200)

    @classmethod
    def run(cls):
        cls.open_pipe1()
        cls.take_debris()
        base.syncAcc(-700,1000)
        # base.syncAcc(130, 800)
        # base.turn(75)
        # base.turn_until_method(lambda: left_sensor.reflection() > 80,speed=100)
        # base.turn_until_method(lambda: left_sensor.reflection() < 30,speed=100)
        # cls.open_pipe2()
        