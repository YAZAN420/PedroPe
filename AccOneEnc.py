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
        cls.minPower = minPower
        cls.maxPower = maxPower
        cls.accelDist = accelDist
        cls.decelDist = decelDist
        cls.totalDist = totalDist
    
    
    @classmethod
    def calculate(cls, encoder):
        """
        Calculate the power output based on the encoder reading.
        
        :param encoder: The current encoder reading (distance covered).
        :return: Tuple containing power_output and done status.
        """
        if encoder < cls.accelDist:
            # Accelerating phase
            power_output = cls.minPower + (cls.maxPower - cls.minPower) * (encoder / cls.accelDist)
        elif encoder > cls.totalDist - cls.decelDist:
            # Decelerating phase
            remaining_dist = cls.totalDist - encoder
            power_output = cls.minPower + (cls.maxPower - cls.minPower) * (remaining_dist / cls.decelDist)
        else:
            # Constant speed phase
            power_output = cls.maxPower
        
        # Clamp power_output between minPower and maxPower
        power_output = max(cls.minPower, min(cls.maxPower, power_output))
        
        # Determine if the target distance has been reached
        done = encoder >= cls.totalDist

        return power_output, done
