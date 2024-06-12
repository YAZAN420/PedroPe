class AccOneEnc:

    @classmethod
    def config(cls, minPower, maxPower, accelDist, decelDist, totalDist):
        """
        Configure the motor encoder parameters.
        
        :param minPower: Minimum power to be applied.
        :param maxPower: Maximum power to be applied.
        :param accelDist: Distance over which the motor accelerates.
        :param decelDist: Distance over which the motor decelerates.
        :param totalDist: Total distance the motor needs to cover.
        """
        controller = cls()
        controller.minPower = minPower
        controller.maxPower = maxPower
        controller.accelDist = accelDist
        controller.decelDist = decelDist
        controller.totalDist = totalDist
        return controller

    def calculate(self, encoder):
        """
        Calculate the power output based on the encoder reading.
        
        :param encoder: The current encoder reading (distance covered).
        :return: Tuple containing power_output and done status.
        """
        if encoder < self.accelDist:
            # Accelerating phase
            power_output = self.minPower + (self.maxPower - self.minPower) * (encoder / self.accelDist)
        elif encoder > self.totalDist - self.decelDist:
            # Decelerating phase
            remaining_dist = self.totalDist - encoder
            power_output = self.minPower + (self.maxPower - self.minPower) * (remaining_dist / self.decelDist)
        else:
            # Constant speed phase
            power_output = self.maxPower
        
        # Clamp power_output between minPower and maxPower
        power_output = max(self.minPower, min(self.maxPower, power_output))
        
        # Determine if the target distance has been reached
        done = encoder >= self.totalDist

        return power_output, done
