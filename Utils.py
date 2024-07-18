from pybricks.tools import wait, StopWatch  # type: ignore
from config import *
from pybricks.tools import wait, StopWatch  # type: ignore


def preflight_checks():
    if (DEBUG):
        stopwatch.reset()
    voltage = ev3.battery.voltage()
    print("The voltage is :", voltage)
    if voltage < 8000:
        if (DEBUG):
            ev3.speaker.beep(frequency=200, duration=1000)
        if (DEBUG):
            print("Low battery.")
        from sys import exit
        exit()
    ev3.speaker.beep(frequency=600, duration=300)


def wait_for_button_press():
    print("Waiting for the button:")
    while not ev3.buttons.pressed():
        wait(10)

    while ev3.buttons.pressed():
        wait(10)
    wait(500)


def printCalibrateColor():
    print("Black:")
    wait_for_button_press()
    black = (left_sensor.rawRef() + right_sensor.rawRef())/2
    print(black)
    print("White:")
    wait_for_button_press()
    white = (left_sensor.rawRef() + right_sensor.rawRef())/2
    print(white)
    print("Finished calibrate")


def finish(infint: bool = False):
    if (DEBUG):
        print(stopwatch.time()//1000)
    if (DEBUG):
        print("finished!")
    ev3.screen.draw_text(10, 10, stopwatch.time()//1000,
                         text_color=Color.BLACK, background_color=None)
    wait(6000 if not infint else 999999999)
