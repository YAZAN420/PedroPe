from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor  # type: ignore
from pybricks.parameters import Port, Direction, Color, Stop  # type: ignore
from pybricks.tools import wait, StopWatch  # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
from base import Base
import time
import ColorSen
from constants import *


class LineController:
    """
    This class is responsible for any action that utilises the color sensors, such as line following and squaring.
    """

    def __init__(self, robotBase: Base,
                 left_sensor: ColorSen,
                 right_sensor: ColorSen,
                 ):
        self.robotBase = robotBase
        self.left_sensor = left_sensor
        self.right_sensor = right_sensor

    def black_state(self):
        """
        Gets the current state of the sensors: 0 for none black, 1 for right sensor black,
        2 for left sensor black, 3 for both black
        :return: 0, 1, 2, 3
        """
        s1 = (int(self.left_sensor.reflection() < 10) * 2)
        s2 = (int(self.right_sensor.reflection() < 10) * 1)
        return s1 + s2

    def white_state(self):
        """
        Gets the current state of the sensors: 0 for none white, 1 for right sensor white,
        2 for left sensor white, 3 for both white
        :return: 0, 1, 2, 3
        """
        s1 = (int(self.left_sensor.reflection() > 90) * 2)
        s2 = (int(self.right_sensor.reflection() > 90) * 1)
        return s1 + s2

    def stop_at_joint(self, speed: int):
        """
        Starts line following using a PID algorithm. The robot stops at the first intersection it senses.
        :param speed: The maximum speed of the robot -100% to 100%
        :return:(nothing)
        """
        speed = abs(speed)
        pd, last_error, error = 0, 0, 0
        captured_angles = self.robotBase.capture_motor_angles()
        while self.black_state() != 3:
            print(self.black_state())
            error = (self.right_sensor.reflection() -
                     self.left_sensor.reflection())
            pd = (KP * error) + (KD * (error - last_error))
            self.robotBase.start_tank_dc(int(speed - pd), int(speed + pd))
            last_error = error
            # wait(15)
        self.robotBase.stop_and_hold()
        return

    def move_until_black(self):
        self.robotBase.stop()
        while self.black_state() != 3:
            self.robotBase.drive(600, 0)
        self.robotBase.stop_and_hold()

    def stop_at_white(self, speed: float = 40):
        """
        Starts line following using a PID algorithm. The robot stops at the first intersection it senses.
        :param speed: The maximum speed of the robot -100% to 100%
        :return:(nothing)
        """
        self.until_method(lambda: self.white_state() != 3)

    def until_method(self, method, speed: float = 40):
        kp = 0.13
        kd = 0.3
        speed = abs(speed)
        pd, last_error, error = 0, 0, 0
        captured_angles = self.robotBase.capture_motor_angles()
        while not method():
            error = (self.right_sensor.reflection() -
                     self.left_sensor.reflection())
            pd = (kp * error) + (kd * (error - last_error))
            self.robotBase.start_tank_dc(int(speed - pd), int(speed + pd))
            last_error = error
        self.robotBase.stop_and_hold()

    def correct(self, duration=0.75, speed=50):
        kp = 0.12
        kd = 1
        pd, last_error, error = 0, 0, 0
        captured_angles = self.robotBase.capture_motor_angles()
        start_time = time.time()
        while (time.time() - start_time) < duration:
            error = (self.right_sensor.reflection() -
                     self.left_sensor.reflection())
            pd = (kp * error) + (kd * (error - last_error))
            self.robotBase.start_tank_dc(int(speed - pd), int(speed + pd))
            last_error = error
        self.robotBase.stop_and_hold()
        return

    def followUntilSensorright(self, speed: int):
        print(self.black_state())
        speed = abs(speed)
        pd, last_error, error = 0, 0, 0
        captured_angles = self.robotBase.capture_motor_angles()
        while self.black_state() != 1:
            print(self.black_state())
            error = (self.right_sensor.reflection() -
                     self.left_sensor.reflection())
            pd = (KP * error) + (KD * (error - last_error))
            self.robotBase.start_tank_dc(int(speed - pd), int(speed + pd))
            last_error = error
            # wait(15)
        self.robotBase.stop_and_hold()
        return

    def followUntilSensorleft(self, speed: int):
        print(self.black_state())
        speed = abs(speed)
        pd, last_error, error = 0, 0, 0
        captured_angles = self.robotBase.capture_motor_angles()
        while self.black_state() != 2:
            print(self.black_state())
            error = (self.right_sensor.reflection() -
                     self.left_sensor.reflection())
            pd = (KP * error) + (KD * (error - last_error))
            self.robotBase.start_tank_dc(int(speed - pd), int(speed + pd))
            last_error = error
            # wait(15)
        self.robotBase.stop_and_hold()
        return

    def follow_cm(self, distance_cm: float, speed: int = -85):
        """
        Starts line following using a PID algorithm. The robot stops when it has travelled a specific distance.
        :param speed: The maximum speed of the robot -100% to 100%
        :param distance_cm:
        :return:(nothing)
        """
        distance_cm = abs(distance_cm)
        speed = abs(speed)
        pd, last_error, error = 0, 0, 0
        captured_angles = self.robotBase.capture_motor_angles()
        distance_degrees = (
            distance_cm / self.robotBase.wheel_circumference) * 360
        while self.robotBase.get_avg_motor_deg(captured_angles) < distance_degrees:
            error = (self.right_sensor.reflection() -
                     self.left_sensor.reflection())
            pd = (KP * error) + (KD * (error - last_error))
            self.robotBase.start_tank_dc(int(speed - pd), int(speed + pd))
            last_error = error
            # wait(15)
        self.robotBase.stop_and_hold()
        return

    def turn_to_line(self, direction: str, speed: int, mode: int):
        """
        Starts turning until a line is detected. Could be used before PID line following.
        :param direction: "left" or "right"
        :param speed:  Maximum speed of the wheel motors
        :param mode: 1 for pivoting around the center, 0 for pivoting around a wheel
        :return:
        """
        if (mode not in [0, 1]) or (direction not in ["left", 'right']):
            return
        speed = abs(speed)
        if direction == "left":
            self.robotBase.start_tank(-1 * mode * speed, speed)
            while self.white_state() != 1:
                print(self.white_state())
                pass
            while self.white_state() not in [3, 2]:
                print(self.white_state())
                pass

        elif direction == "right":
            self.robotBase.start_tank(speed, -1 * mode * speed)
            while self.white_state() != 2:
                pass
            while self.white_state() not in [3, 1]:
                pass

        while self.white_state() != 3:
            pass
        self.robotBase.stop_and_hold()
        return
