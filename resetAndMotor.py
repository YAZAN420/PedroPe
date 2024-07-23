
from config import *
from Utils import *
from seeWithSensors import *
from HotamAndPipe import *


def resetDetectedColor(angle=191):
    down_motor.run_angle(speed=-10000, rotation_angle=angle,
                         then=Stop.HOLD, wait=False)


def reset_start():
    down_motor.run_time(speed=1000, time=600, wait=False)
    up_motor.run_time(speed=-1000, time=600, wait=False)


def downClaw(duty=130):
    up_motor.run_until_stalled(-6000, then=Stop.HOLD, duty_limit=duty)


def upClaw():
    up_motor.run_until_stalled(1000, then=Stop.HOLD, duty_limit=110)


def upMotorResetWithTrueOrFalse(speed=1000, bool=True):
    up_motor.run_time(speed=speed, time=900, wait=bool)


def downMotorResetTrueOrFalse(speed=1000, bool=True):
    down_motor.run_time(speed=speed, time=900, wait=bool)


def reset():
    up_motor.run(1000)
    down_motor.run(1000)
    up_motor.run_until_stalled(6000, then=Stop.HOLD, duty_limit=75)
    wait(200)
    down_motor.hold()
    up_motor.hold()
