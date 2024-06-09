from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import Motor,ColorSensor,GyroSensor # type: ignore
from pybricks.parameters import Port,Direction,Color,Stop # type: ignore
from pybricks.tools import wait,StopWatch # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
from base import Base

class GyroController:
    """
    This class is responsible for any action that utilises the gyro sensor, such as turning accurately and moving
    straight accurately.
    """

    def __init__(self, robotBase: Base,
                 gyroS: GyroSensor):
        self.robotBase = robotBase
        self.sensor = gyroS

    def turn(self, endAngle: int, speed: int, mode=1):
        """
        This method turns the robot to a specific angle using the gyro sensor. If the robot doesn't turn accurately
        try reconnecting the gyro sensor or restarting the program while the robot is perfectly still. :param
        endAngle: The angle to turn to :param speed: Maximum speed of the wheel motors :param mode: 1 for
        pivoting around the center, 0 for pivoting around a wheel :return: nothing
        """
        if mode not in [0, 1]:
            return       
        for i in range(2):
            start_angle = self.sensor.angle()
            
            if endAngle > start_angle:
                while endAngle > self.sensor.angle():                
                    if abs(start_angle - self.sensor.angle()) > 15:
                        self.robotBase.start_tank(speed, -speed * mode)
                    else:
                        self.robotBase.start_tank(90, -90 * mode)

            elif endAngle < start_angle:
                while endAngle < self.sensor.angle():
                    if abs(start_angle - self.sensor.angle()) > 15:
                        self.robotBase.start_tank(-speed * mode, speed)
                    else:
                        self.robotBase.start_tank(-90 * mode, 90)

            self.robotBase.stop_and_hold()
            # EV3Brick().screen.draw_text(70, 70, str(gyro.sensor.angle())) # type: ignore
        return

    def straight_pid(self, distance_cm, speed, targetAngle):
        """
        The robot moves perfectly straight using the gyro sensor and a PID algorithm for a specific distance
        :param distance_cm: Distance to move in cm before stopping
        :param speed: Maximum speed of the wheel motors
        :param targetAngle: Angle to maintain while moving, works best if you turn to that angle first
        """
        pid, integral, d, error, last_error = 0, 0, 0, 0, 0
        kp, ki, kd = 100, 0, 0
        speed = abs(speed)
        captured_angles = self.robotBase.capture_motor_angles()
        distance_degrees = (abs(distance_cm) / self.robotBase.wheel_circumference) * 360
        while self.robotBase.get_avg_motor_deg(captured_angles) < distance_degrees:
            error = self.sensor.angle() - targetAngle
            integral += error
            d = error - last_error
            pid = (kp * error) + (ki * integral) + (kd * d)
            self.robotBase.start_tank_dc(speed - pid, speed + pid)
            last_error = error
            EV3Brick().screen.draw_text(70, 70, str(self.sensor.angle()))
            print(str(self.sensor.angle()))
            wait(10)
            
        self.robotBase.stop_and_hold()