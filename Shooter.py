#n is a placeholder
import wpilib
import utilities
#import ctre

class ShooterController():

    def __init__(self, robot):
        #Motor Setup
        '''self.Ultrasonic = wpilib.Ultrasonic(7, 8)
        self.RakeMotor = wpilib.Victor(6)
        self.PivotMotor = wpilib.Victor(5)
        self.ConveyorMotor1 = ctre.WPI_VictorSPX(4)
        self.ConveyorMotor2 = ctre.WPI_VictorSPX(3)
        self.Flywheel = ctre.WPI_VictorSPX(2)
        self.TimedMotor = ctre.WPI_VictorSPX(1)'''
        self.ConveyorMotor1 = wpilib.Victor(4)
        self.ConveyorMotor2 = wpilib.Victor(3)
        self.Flywheel = wpilib.Victor(2)
        self.TimedMotor = wpilib.Victor(1)

        #Timer Setup
        self.ShootTimer = wpilib.Timer()
        self.PrintTimer = wpilib.Timer()
        self.PrintTimer.start()
        self.IndexTimer = wpilib.Timer()
        #self.Encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X)
        
        #Misc Variable Setup:
        self.AutoShoot = False
        self.TimerBegin = False
        self.TimerRunning = False
        self.IndexRunning = False
        
    def teleopPeriodic(self, robot):
        #Shooter Actions
        if robot.gamepad.getRawButton(7):
            self.Flywheel.set(.5)
        else:
            self.Flywheel.set(0)

        if robot.gamepad.getRawButton(8):
            self.ConveyorMotor1.set(.1)
            self.ConveyorMotor2.set(.1)
        else:
            self.ConveyorMotor1.set(0)
            self.ConveyorMotor2.set(0)


        #Auto-Shoot
        if robot.gamepad.getRawButton(9):
            self.AutoShoot = True
            self.ShootTimer.start()
            print("Begun")

        if self.AutoShoot == True:
            utilities.utilities.AutoShoot(self)

        #-----------------------------------------------------------------------
        
        #Timed Button
        if robot.stick1.getRawButton(10):
            self.TimerBegin = True
        
        if self.TimerBegin:
            if self.TimerRunning == False:
                self.Timer.start()
                self.PrintTimer.start()
                self.TimedMotor.set(.1)
            if self.Timer.get() < 5:
                self.TimerRunning = True
                if self.PrintTimer.hasPeriodPassed(1):
                    print(int(self.Timer.get()))
                
            else:
                print(int(self.Timer.get()))
                self.TimedMotor.set(0)
                self.Timer.reset()
                self.TimerBegin = False
                self.TimerRunning = False

        #-----------------------------------------------------------------------

        #Ball Index System
        if robot.gamepad.getRawButton(1):
            self.IndexTimer.start()
            self.IndexRunning = True

        if self.IndexRunning:
            utilities.utilities.BallIndex(self)

        #-----------------------------------------------------------------------
                
        #Encoder Button
        '''if robot.stick1.getRawButton(2) == 1:
            self.EncoderBegin = True
        if EncoderBegin == True:
            self.Encoder.'''

        #Ultrasonic
        if robot.stick1.getRawButton(3) == 1:
            Ultrasonic.ping()
            print(pidGet())