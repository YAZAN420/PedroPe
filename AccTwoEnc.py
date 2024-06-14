class AccTwoEnc:

    def config(cls, minPower, maxPower, accelDist, decelDist, totalDist):
        cls.min_power = abs(minPower)
        cls.max_power = abs(maxPower)
        cls.accel_distance = accelDist
        cls.decel_distance = decelDist
        cls.total_distance = totalDist
        cls.is_negative = (minPower < 0)
        cls.power = 0

    @classmethod
    def calculate(cls, encoder_b, encoder_c):
        current_encoder = (abs(encoder_b) + abs(encoder_c)) / 2
        if current_encoder >= cls.total_distance:
            done = 1
            power_output = 0
        elif current_encoder > cls.total_distance / 2:
            if cls.decel_distance == 0:
                cls.power = cls.max_power
            else:
                cls.power = ((cls.max_power - cls.min_power) / (cls.decel_distance ** 2) *
                             (current_encoder - cls.total_distance) ** 2 + cls.min_power)
            done = 0
        else:
            if cls.accel_distance == 0:
                cls.power = cls.max_power
            else:
                cls.power = ((cls.max_power - cls.min_power) / (cls.accel_distance ** 2) *
                             current_encoder ** 2 + cls.min_power)
            done = 0
        if cls.power < cls.min_power:
            cls.power = cls.min_power
        elif cls.power > cls.max_power:
            cls.power = cls.max_power
        if cls.is_negative == 1:
            power_output = -cls.power
        else:
            power_output = cls.power
        return power_output, done
