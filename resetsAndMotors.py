from config import *
from Utils import *


def upMotorRunAngle(speed, angle, wait=True):
    up_motor.run_angle(speed=speed, rotation_angle=angle, wait=wait)


def downMotorRunAngle(speed, angle, wait=True):
    down_motor.run_angle(speed=speed, rotation_angle=angle, wait=wait)


def upMotorRunTime(speed, time, wait=True):
    up_motor.run_time(speed=speed, time=time, wait=wait)


def downMotorRunTime(speed, time, wait=True):
    down_motor.run_time(speed=speed, time=time, wait=wait)


def leftMotorRunAngle(speed, angle, wait=True):
    left_motor.run_angle(speed=speed, rotation_angle=angle, wait=wait)


def rightMotorRunAngle(speed, angle, wait=True):
    right_motor.run_angle(speed=speed, rotation_angle=angle, wait=wait)


def leftMotorRunTime(speed, time, wait=True):
    left_motor.run_time(speed=speed, time=time, wait=wait)


def rightMotorRunTime(speed, time, wait=True):
    right_motor.run_time(speed=speed, time=time, wait=wait)


def resetDetectedColor(angle=191):
    down_motor.run_angle(speed=-10000, rotation_angle=angle,
                         then=Stop.HOLD, wait=False)


def downMotorUntilStalled(speed, duty=25):
    down_motor.run_until_stalled(speed=speed, duty_limit=duty)


def resetStart():
    down_motor.run_time(speed=1000, time=600, wait=False)
    up_motor.run_time(speed=-1000, time=600, wait=False)


def downClaw(duty=70):
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
