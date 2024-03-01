import wpilib
import wpilib.drive
import phoenix5
from magicbot import will_reset_to
from magicbot import feedback


class Drivetrain:
    #Sets what the motors controllers are
    frontleftmotor: phoenix5.WPI_TalonSRX
    frontrightmotor: phoenix5.WPI_TalonSRX
    backleftmotor: phoenix5.WPI_TalonSRX
    backrightmotor: phoenix5.WPI_TalonSRX

    forward = will_reset_to(0)
    turn = will_reset_to(0)
    #sets up the motor groups
    def setup(self):
        self.rightmotor = wpilib.MotorControllerGroup(
            self.frontrightmotor, self.backrightmotor
        )
        self.leftmotor = wpilib.MotorControllerGroup(
            self.frontleftmotor, self.backleftmotor
        )
        self.robotDrive = wpilib.drive.DifferentialDrive(
            self.leftmotor, self.rightmotor
        )
    #sets drive type 
    def arcadeDrive(self, forward, turn):
        self.forward = forward
        self.turn = turn

    def execute(self):
        self.robotDrive.arcadeDrive(self.forward, self.turn)
