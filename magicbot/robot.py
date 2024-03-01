import magicbot
import wpilib
import wpilib.drive
import phoenix5
from components.Drivetrain import Drivetrain
from wpilib import SmartDashboard
import navx
from components.drive_control import DriveControl


class MyRobot(magicbot.MagicRobot):
    drivetrain: Drivetrain
    drive_control: DriveControl

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
        with self.consumeExceptions():
            self.drivetrain.arcadeDrive(
                -self.joy.getY() * float(self.joy.getThrottle()),
                -self.joy.getX() * float(self.joy.getThrottle()),
            )
        if self.joy.getTrigger():
            self.drive_control.turn_to_angle(180)
        SmartDashboard.putNumber("Joystick X value", self.joy.getY())
        SmartDashboard.putNumber("Joystick Y value", self.joy.getX())
        SmartDashboard.putNumber("navx", self.navx.getAngle())
