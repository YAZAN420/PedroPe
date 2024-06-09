from pybricks.tools import wait,StopWatch # type: ignore
from config import *

def preflightChecks():
    print("The voltage is :" , ev3.battery.voltage())
    if ev3.battery.voltage() < 8000:
        ev3.speaker.beep(frequency=200, duration=1000)    
        print("Low battery.")
        from sys import exit               
        exit()
    ev3.speaker.beep(frequency=600, duration=300)
        
def waitForButtonPress():
    print("Waiting for the button:")
    while not ev3.buttons.pressed():
        wait(10)

    while ev3.buttons.pressed():
        wait(10) 
    wait(500)
    
def printCalibrateColor():
    print("Black:")
    waitForButtonPress()
    black = (left_sensor.rawRef() + right_sensor.rawRef())/2
    print(black)
    print("White:")
    waitForButtonPress()
    white = (left_sensor.rawRef() + right_sensor.rawRef())/2
    print(white)
    print("Finished calibrate")
    
    
def finish(infint : bool = False ):
    print("finished!")
    wait(6000 if not infint  else 999999999)
    


    