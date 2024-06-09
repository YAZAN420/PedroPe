class AccTwoEnc:

    def __init__(self):
        print("__init__")

    def config(self, minPower, maxPower, accelDist, decelDist, totalDist):
        self.min_power = abs(minPower)
        self.max_power = abs(maxPower)
        self.accel_distance = accelDist
        self.decel_distance = decelDist
        self.total_distance = totalDist
        self.is_negative = (minPower < 0)
        self.power = 0

    def calculate(self, encoder_b, encoder_c):
        current_encoder = (abs(encoder_b) + abs(encoder_c)) / 2

        if current_encoder >= self.total_distance:
            done = 1
            power_output = 0
        elif current_encoder > self.total_distance / 2:
            if self.decel_distance == 0:
                self.power = self.max_power
            else:
                self.power = ((self.max_power - self.min_power) / (self.decel_distance ** 2) *
                         (current_encoder - self.total_distance) ** 2 + self.min_power)
            done = 0
        else:
            if self.accel_distance == 0:
                self.power = self.max_power
            else:
                self.power = ((self.max_power - self.min_power) / (self.accel_distance ** 2) *
                         current_encoder ** 2 + self.min_power)
            done = 0

        if self.power < self.min_power:
            self.power = self.min_power
        elif self.power > self.max_power:
            self.power = self.max_power

        if self.is_negative == 1:
            power_output = -self.power
        else:
            power_output = self.power

        return power_output, done
