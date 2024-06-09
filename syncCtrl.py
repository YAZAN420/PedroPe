class Sync:
    print("Sync")

    def __init__(self):
        print("__init__")

    def config(self, kp: float, kd: float, speedB: float, speedC: float):
        self.kp = kp
        self.kd = kd
        self.speedB = speedB
        self.speedC = speedC
        self.speedBsign = abs(speedB + 1) - abs(speedB)
        self.speedCsign = abs(speedC + 1) - abs(speedC)
        self.last_error = 0

    def calculate(self, encoderB, encoderC):
        error = ((self.speedC * encoderB) - (self.speedB * encoderC))
        U = (error - self.last_error) * self.kd + error * self.kp
        powerB = self.speedB - self.speedCsign * U
        powerC = self.speedC + self.speedBsign * U
        self.last_error = error
        return (powerB, powerC)

    def calculateWithSpeed(self, encoderB, encoderC, speedB, speedC):
        speedBsign = abs(speedB + 1) - abs(speedB)
        speedCsign = abs(speedC + 1) - abs(speedC)
        error = ((speedC * encoderB) - (speedB * encoderC))
        U = (error - self.last_error) * self.kd + error * self.kp
        powerB = speedB - speedCsign * U
        powerC = speedC + speedBsign * U
        self.last_error = error
        return (powerB, powerC)
