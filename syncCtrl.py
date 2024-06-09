class SyncCtrl:
    print("Sync")

    @classmethod
    def config(cls, kp: float, kd: float, speedB: float, speedC: float):
        cls.kp = kp
        cls.kd = kd
        cls.speedB = speedB
        cls.speedC = speedC
        cls.speedBsign = abs(speedB + 1) - abs(speedB)
        cls.speedCsign = abs(speedC + 1) - abs(speedC)
        cls.last_error = 0

    @classmethod
    def calculate(cls, encoderB, encoderC):
        error = ((cls.speedC * encoderB) - (cls.speedB * encoderC))
        U = (error - cls.last_error) * cls.kd + error * cls.kp
        powerB = cls.speedB - cls.speedCsign * U
        powerC = cls.speedC + cls.speedBsign * U
        cls.last_error = error
        return (powerB, powerC)

    @classmethod
    def calculateWithSpeed(cls, encoderB, encoderC, speedB, speedC):
        speedBsign = abs(speedB + 1) - abs(speedB)
        speedCsign = abs(speedC + 1) - abs(speedC)
        error = ((speedC * encoderB) - (speedB * encoderC))
        U = (error - cls.last_error) * cls.kd + error * cls.kp
        powerB = speedB - speedCsign * U
        powerC = speedC + speedBsign * U
        cls.last_error = error
        return (powerB, powerC)
