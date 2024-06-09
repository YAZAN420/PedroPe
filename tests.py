from config import *
from pybricks.tools import wait,StopWatch # type: ignore
from Utils import *
from mainFunctions import *
def testUpMotor():
    while True:
        up_motor.run(-800)
        ev3.speaker.beep()
        wait(3000)
        up_motor.run(800)
        ev3.speaker.beep()
        wait(3000)
        
def grap():
    up_motor.run_until_stalled(-1000,then=Stop.HOLD)
    down_motor.run_until_stalled(-1000,then=Stop.HOLD)
    down_motor.run_until_stalled(1000,then=Stop.HOLD)
    

    
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
    up_motor.run_until_stalled(500,then=Stop.HOLD,duty_limit=85)
    wait(5000)
    up_motor.run_until_stalled(-6000,then=Stop.HOLD,duty_limit=75)
    
    
def lineAndTurn():
    up_motor.run_until_stalled(-80, then=Stop.HOLD)
    waitForButtonPress()
    line.correct()    
    line.followUntilSensor(-70,"right")
    line.follow_cm(-70,7.5)
   
    line.correct()  
    line.stop_at_joint(-70)

def testClaws():
    up_motor.run_until_stalled(1000,then=Stop.HOLD)
    down_motor.run_until_stalled(1000,then=Stop.HOLD)
    down_motor.run(-500)
    wait(500)
    up_motor.run_until_stalled(-1000,then=Stop.HOLD)

def correctTest():
    while True:
        waitForButtonPress()
        line.correct()

def lineTest():
    while True:
        waitForButtonPress()
        line.correct()
        line.follow_cm(40)
        
def testU():
    waitForButtonPress()
    line.correct()    
    line.followUntilSensorright(-70)
    base.move_cm(10,250)
    base.turn(90)
    base.stop_and_hold()
    line.correct()
    line.stop_at_joint(-70)
    base.move_cm(10,250)
    base.turn(-90)
    line.correct()
    line.stop_at_joint(-70)
    base.turn(180)
    line.correct()
    line.followUntilSensorright(-70)
    base.move_cm(10,450)
    base.turn(90)
    line.correct()
    line.stop_at_joint(-70)
    base.move_cm(10,250)
    base.turn(-90)
    line.correct()
    line.stop_at_joint(-85)
    base.turn(180)
    line.correct()
    down_motor.run(500)

def printValues():
    while True:
        wait(200)
        h,s,v=front_sensor.hsv()
        wait(200)
        # ref = front_sensor.reflection()
        # wait(200)
        # amp = front_sensor.ambient()
        # print(r)
        # print(g)
        # print(b)
        # print(h)
        # print(s)
        print(v)
        # print(ref)
        # print(amp)\
def testBlocks():
    down_motor.run_time(400,300*1.5,then=Stop.HOLD, wait=True)
    down_motor.run(600)
    print("1")
    up_motor.run_angle(speed=300,rotation_angle=60,then=Stop.HOLD, wait=True)
    print("2")
    base.move_cm(5.5,70)    
    print("3")
    up_motor.run_time(-300,400)
    print("4")
    down_motor.stop()
    down_motor.run_angle(speed=-1000,rotation_angle=150,then=Stop.HOLD,wait=True)
def tmpTest():
    while True:
        waitForButtonPress()
        reset()
        wait(2000)
        up_motor.stop()
        down_motor.stop()