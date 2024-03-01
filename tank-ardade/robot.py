#pure robotpy i think so not very useful

import wpilib
import wpilib.drive
import phoenix5


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """Robot initialization function"""

        self.frontleftmotor = phoenix5.WPI_TalonSRX(15)
        self.frontrightmotor = phoenix5.WPI_TalonSRX(18)
        self.backleftmotor = phoenix5.WPI_TalonSRX(55)
        self.backrightmotor = phoenix5.WPI_TalonSRX(12)

        self.xbox = wpilib.XboxController(0)
        self.rightmotor = wpilib.MotorControllerGroup(
            self.frontrightmotor, self.backrightmotor
        )
        self.leftmotor = wpilib.MotorControllerGroup(
            self.frontleftmotor, self.backleftmotor
        )
        self.rightmotor.setInverted(True)
        self.robotDrive = wpilib.drive.DifferentialDrive(
            self.leftmotor, self.rightmotor
        )
        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.

    def teleopPeriodic(self):
        self.robotDrive.arcadeDrive(
            -self.xbox.getLeftY() * 0.5, -self.xbox.getLeftX() * 0.5
        )
