from config import *
from Utils import *

def putBlockOnBlock():
    down_motor.run_time(400,300*1.5,then=Stop.HOLD, wait=True)
    down_motor.run(600)
    up_motor.run_angle(speed=300,rotation_angle=60,then=Stop.HOLD, wait=True)
    base.move_cm(5.7,70)    
    up_motor.run_time(-300,400)
    down_motor.stop()
    down_motor.run_angle(speed=-1000,rotation_angle=150,then=Stop.HOLD,wait=True)
    
def make2BlocksGood():
    down_motor.run_time(1000,300*1.5,then=Stop.HOLD, wait=True)
    down_motor.run_time(-1000,220*3,then=Stop.HOLD, wait=True)
    down_motor.run_time(1000,220*1.5,then=Stop.HOLD, wait=True)
    
def take4block(angle):
    resetDetectedColor(angle)
    moveUntilBlock()
    base.move_cm(14,150)
    putBlockOnBlock()
    base.straight(-20)
    downClaw()
    make2BlocksGood()
    upClaw()
    base.straight(100)
    base.stop_and_hold()
    downClaw()
    #
    base.move_cm(7,150)
    putBlockOnBlock()
    base.straight(-20)
    downClaw()
    down_motor.run_time(1000,300*1.5,then=Stop.HOLD, wait=True)
    down_motor.run_time(-1000,220*3,then=Stop.HOLD, wait=True)
    

def take8Blocks():
    downClaw(70)
    base.straight(-200)
    base.stop()
    left_motor.run_time(90,900)
    left_motor.hold()
    
    base.move_cm(16,350)
    take4block(195)
    
    base.straight(-150)
    base.turn(-80)
    base.stop_and_hold()
    base.stop()
    down_motor.run_time(1000,220*1.5,then=Stop.HOLD, wait=True)
    upClaw()
    reset()
    base.straight(200)
    downClaw()
    base.turn(-180)
    base.straight(-1000)
    base.turn(75)
    base.stop()
    downClaw()
    down_motor.run_time(1000,250,then=Stop.HOLD, wait=True)
    
    take4block(195)
    down_motor.run_time(1000,220*1.5,then=Stop.HOLD, wait=True)
    down_motor.run_time(1000,300*1.5,then=Stop.HOLD, wait=True)
    
def resetDetectedColor(angle):
    down_motor.run_angle(speed=-10000, rotation_angle=angle,then=Stop.HOLD,wait=True)
    
def downClaw(duty=60):
    up_motor.run_until_stalled(-6000,then=Stop.HOLD,duty_limit=duty)
    
def upClaw():
    up_motor.run_until_stalled(1000,then=Stop.HOLD,duty_limit=110)
    
    
def moveUntilBlock():
    base.start_tank(350,350)
    while(True):
        h,s,v=front_sensor.hsv()
        if(v >= 2): break
    base.stop_and_hold()
    
    
def reset():
    up_motor.run(1000)
    down_motor.run(1000)
    up_motor.run_until_stalled(6000,then=Stop.HOLD,duty_limit=75)
    wait(200)
    down_motor.hold()
    print("reseted")
    ev3.speaker.beep()