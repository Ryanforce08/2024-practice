import wpilib
import wpilib.drive
import phoenix5
from magicbot import will_reset_to

class Drivetrain:
    frontleftmotor: phoenix5.WPI_TalonSRX
    frontrightmotor: phoenix5.WPI_TalonSRX
    backleftmotor: phoenix5.WPI_TalonSRX
    backrightmotor: phoenix5.WPI_TalonSRX

    forward = will_reset_to(0)
    turn = will_reset_to(0)

    
    def setup(self):
        self.rightmotor = wpilib.MotorControllerGroup(
            self.frontrightmotor, self.backrightmotor
        )
        self.leftmotor = wpilib.MotorControllerGroup(
            self.frontleftmotor, self.backleftmotor
        )
        self.robotDrive = wpilib.drive.DifferentialDrive(
            self.frontleftmotor, self.frontrightmotor,self.
            backleftmotor, self.backrightmotor)
    
    def arcade_drive(self, forward, turn):
        self.forward = forward
        self.turn = turn
        
    def execute(self):
        self.robotDrive.arcadeDrive(self.forward, self.turn)

