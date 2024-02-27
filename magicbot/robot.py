import magicbot
import wpilib
import wpilib.drive
import phoenix5
from components.drivetrain import Drivetrain
from wpilib import SmartDashboard
import navx


class MyRobot(magicbot.MagicRobot):
    drivetrain: Drivetrain

    def createObjects(self):
        self.frontleftmotor = phoenix5.WPI_TalonSRX(15)
        self.frontrightmotor = phoenix5.WPI_TalonSRX(18)
        self.backleftmotor = phoenix5.WPI_TalonSRX(55)
        self.backrightmotor = phoenix5.WPI_TalonSRX(12)
        self.joy = wpilib.Joystick(0)
        self.navx = navx.AHRS.create_spi()

    @property
    def get_angle(self):
        return self.navx.getAngle()

    def teleopPeriodic(self):
        self.drivetrain.arcadeDrive(
            -self.joy.getX() * 0.5, -self.joy.getY() * -0.5
        )
        SmartDashboard.putNumber("Joystick X value", self.joy.getY())
        SmartDashboard.putNumber("Joystick Y value", self.joy.getX())
        SmartDashboard.putNumber("navx", self.navx.getAngle())

        

