from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor  # type: ignore
from pybricks.parameters import Port, Direction, Color, Stop  # type: ignore
from pybricks.tools import wait, StopWatch  # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
import math
from syncCtrl import *
from AccTwoEnc import *
from AccOneEnc import *


class Base(DriveBase):
    """
    This is the class responsible for movement. To use this class, you need to specify the left and right motors,
    the wheel circumference in cm.
    """

    def __init__(self, left_motor: Motor,
                 right_motor: Motor,
                 wheel_diameter: float,
                 axle_track: float,
                 ):
        self.wheel_circumference = math.pi * wheel_diameter * 0.1
        self.left_motor = left_motor
        self.right_motor = right_motor
        super().__init__(left_motor, right_motor, wheel_diameter, axle_track)

    def start_tank(self, leftSpeed: int, rightSpeed: int):
        """
        This method gives you control of the speed of each motor separately. The base will start moving and will not
        stop automatically.

        :param leftSpeed: -100 to 100, negative for reverse
        :param rightSpeed: -100 to 100, negative for reverse
        """
        super().stop()
        self.left_motor.run(leftSpeed)
        self.right_motor.run(rightSpeed)
        return

    def start_tank_dc(self, leftSpeed: int, rightSpeed: int):
        """
        This method gives you control of voltage of each motor separately. The base will start moving and will not stop
        automatically.
        :param leftSpeed: -100 to 100, negative for reverse
        :param rightSpeed: -100 to 100, negative for reverse
        """
        super().stop()
        self.left_motor.dc(leftSpeed)
        self.right_motor.dc(rightSpeed)
        return

    def stop_and_hold(self):
        """
        Instantly stops the robot and holds the motors at current position.
        """
        super().stop()
        self.left_motor.hold()
        self.right_motor.hold()
        return

    def reset_angles(self):
        """
        Resets the angles of the motors
        :return: nothing
        """
        self.stop()
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        return

    def get_avg_motor_deg(self, captured_motor_angles):
        """
        Returns the average number of the wheel motors degrees based on the initial angles' parameter.
        :return: int
        """
        return int((abs(int(self.right_motor.angle()) - captured_motor_angles[1]) +
                    abs(int(self.left_motor.angle()) - captured_motor_angles[0])) / 2)

    def capture_motor_angles(self):
        """
        Capture the left and right motor angles as a list of 2 items.
        :returns a list containing the left motor angle and the right motor angle [int, int]
        """
        return [int(self.left_motor.angle()), int(self.right_motor.angle())]

    def move_mm(self, distance_in_mm: float, speed: int):
        """
        Starts moving at the specified speed and stops when the distance specified is reached.
        :param distance_in_cm: Positive Integer
        :param speed: -100 to 100
        """
        self.start_tank(speed, speed)
        captured_angles = self.capture_motor_angles()
        distance_in_degrees = abs(
            (distance_in_mm / self.wheel_circumference) * 36)
        while self.get_avg_motor_deg(captured_angles) < distance_in_degrees:
            pass
        self.stop_and_hold()
        return

    def syncMoveMm(self, distance_in_Mm: float, speed: int):
        self.reset_angles()
        SyncCtrl.config(0.012, 0, speed, speed)
        distance_in_degrees = abs(
            int((distance_in_Mm / self.wheel_circumference) * 36))
        done = False
        while not done:
            el = self.left_motor.angle()
            er = self.right_motor.angle()
            powerB, powerC = SyncCtrl.calculate(el, er)
            self.left_motor.run(powerB)
            self.right_motor.run(powerC)
            done = (abs(el)+abs(er))/2 >= distance_in_degrees
        self.left_motor.hold()
        self.right_motor.hold()
   

    def turn(self, angle, acc=600):
        self.stop()
        self.settings(turn_acceleration=acc)
        super().turn(angle)

    def sync_acc(self, distance_in_mm: float, acc=500, speedMin=150, speedMax=1000):
        self.stop()
        self.settings(straight_acceleration=acc)
        self.straight(distance_in_mm)
    
    def acc_one_motor(self, motor, degrees, speed=100):
        self.stop()
        motor.reset_angle(0)
        sign = abs(speed + 1) - abs(speed)
        speed = abs(speed)
        speed /= 100
        done = False
        AccOneEnc.config(
            200, 800*speed, degrees/2, degrees/2, degrees)
        while not done:
            encoder = abs(motor.angle())
            power, done = AccOneEnc.calculate(encoder)
            power *= sign
            motor.run(power)
        motor.hold()

    def move_sideway(self, degrees, speed, right):
        if (right):
            self.acc_one_motor(self.left_motor, degrees, speed)
            wait(200)
            self.acc_one_motor(self.right_motor, degrees, speed)
        else:
            self.acc_one_motor(self.right_motor, degrees, speed)
            wait(200)
            self.acc_one_motor(self.left_motor, degrees, speed)

    def turn_without_sync(self,angle,speed=1000):
        angle *= 4
        self.left_motor.run_angle(speed=speed,rotation_angle=angle,wait=False)
        self.right_motor.run_angle(speed=speed,rotation_angle=-angle,wait=True)
    


    def turn_until_method(self, function, speed=60):
        self.start_tank(speed, -speed)
        while (not function()):
            pass
        self.stop_and_hold()

    def move_until_method(self, function, speed=60):
        self.start_tank(speed, speed)
        while (not function()):
            pass
        self.stop_and_hold()

    def start_moving(self, speed: int):
        """
        Starts moving at the specified speed.
        :param speed: -100 to 100
        """
        self.start_tank(speed, speed)
        return
