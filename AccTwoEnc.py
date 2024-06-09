class AccTwoEnc:

    def __init__():
        print("__init__")

    def config(self, minPower, maxPower, accelDist, decelDist, totalDist):
        self.minPower = abs(minPower)
        self.maxPower = abs(maxPower)
        self.accelDist = accelDist
        self.decelDist = decelDist
        self.totalDist = totalDist
        self.isNeg = (minPower < 0)

    def calculate(self, encoder_b, encoder_c):
        current_encoder = (abs(encoder_b) + abs(encoder_c)) / 2

        if current_encoder >= self.total_distance:
            done = 1
            power_output = 0
        elif current_encoder > self.total_distance / 2:
            if self.decel_distance == 0:
                power = self.max_power
            else:
                power = ((self.max_power - self.min_power) / (self.decel_distance ** 2) *
                         (current_encoder - self.total_distance) ** 2 + self.min_power)
            done = 0
        else:
            if self.accel_distance == 0:
                power = self.max_power
            else:
                power = ((self.max_power - self.min_power) / (self.accel_distance ** 2) *
                         current_encoder ** 2 + self.min_power)
            done = 0

        if power < self.min_power:
            power = self.min_power
        elif power > self.max_power:
            power = self.max_power

        if self.is_negative == 1:
            power_output = -power
        else:
            power_output = power

        return power_output, done
