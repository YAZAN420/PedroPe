from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import Motor, GyroSensor  # type: ignore
from pybricks.parameters import Port, Direction, Color, Stop  # type: ignore
from pybricks.tools import wait, StopWatch  # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
from gyroClass import GyroController
from base import Base
from ColorSen import ColorSen
from lineFollowClass import LineController


ev3 = EV3Brick()
left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
up_motor = Motor(Port.D, Direction.CLOCKWISE)
down_motor = Motor(Port.B, Direction.CLOCKWISE)
left_sensor = ColorSen(Port.S2)
right_sensor = ColorSen(Port.S3)
front_sensor = ColorSen(Port.S1)
base = Base(left_motor=left_motor, right_motor=right_motor,
            wheel_diameter=81.6, axle_track=160)
base.settings(turn_rate=225, straight_speed=10000, straight_acceleration=700,turn_acceleration=200)
line = LineController(base, left_sensor=left_sensor, right_sensor=right_sensor)
