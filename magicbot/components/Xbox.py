import wpilib
import wpilib.drive


class Xbox:
    def setup(self):
        self.xbox = wpilib.XboxController(0)
