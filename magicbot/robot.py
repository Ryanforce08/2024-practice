import magicbot
import wpilib
import wpilib.drive
import phoenix5
from components.drivetrain import Drivetrain


class MyRobot(magicbot.MagicRobot):
    drivetrain: Drivetrain

    def createObjects(self):
        self.frontleftmotor = phoenix5.WPI_TalonSRX(15)
        self.frontrightmotor = phoenix5.WPI_TalonSRX(18)
        self.backleftmotor = phoenix5.WPI_TalonSRX(55)
        self.backrightmotor = phoenix5.WPI_TalonSRX(12)
        self.joy = wpilib.XboxController(0)


    def teleopPeriodic(self):
        self.drivetrain.arcade_drive(
            -self.joy.getLeftX() * 0.5, -self.joy.getLeftY() * 0.5
        )