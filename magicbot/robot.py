import magicbot
import wpilib
import wpilib.drive
import phoenix5
from components import Drivetrain
from components import Xbox



class MyRobot(magicbot.MagicRobot):
    drivetrain: Drivetrain
    xbox: Xbox

    def createObjects(self):
        self.frontleftmotor = phoenix5.WPI_TalonSRX(15)
        self.frontrightmotor = phoenix5.WPI_TalonSRX(18)
        self.backleftmotor = phoenix5.WPI_TalonSRX(55)
        self.backrightmotor = phoenix5.WPI_TalonSRX(12)
        self.xbox = wpilib.XboxController(0)


    def teleopPeriodic(self):
        self.drivetrain.arcadeDrive(
            -self.xbox.getLeftY() * 0.5, -self.xbox.getLeftX() * 0.5
        )