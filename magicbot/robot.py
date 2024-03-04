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
    #creates objects as the def implies
    def createObjects(self):
        self.frontleftmotor = phoenix5.WPI_TalonSRX(15)
        self.frontrightmotor = phoenix5.WPI_TalonSRX(18)
        self.backleftmotor = phoenix5.WPI_TalonSRX(55)
        self.backrightmotor = phoenix5.WPI_TalonSRX(12)
        self.joy = wpilib.Joystick(0)
        self.navx = navx.AHRS.create_spi()
        self.speed=self.joy.getThrottle()

    @property
    def get_angle(self):
        return self.navx.getAngle()
    #everything under here does stuff when robot is running
    def teleopPeriodic(self):
        self.speed +1
        self.speed /2
        self.speed +0.5
        self.drivetrain.arcadeDrive(
                -self.joy.getX() * float(self.speed),
                self.joy.getY() * float(self.speed),
            )
        if self.joy.getTrigger():
            self.drive_control.turn_to_angle(180)
        SmartDashboard.putNumber("Joystick X value", self.joy.getY())
        SmartDashboard.putNumber("Joystick Y value", self.joy.getX())
        SmartDashboard.putNumber("navx", self.navx.getAngle())
