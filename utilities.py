import wpilib
# from wpilib import RobotDrive

class Utilities():
    def TimedButton(robot, motor, direction, speed, num, initTime):
        time = robot.timer.getMsClock() / 1000
        if time - initTime < num:
            motor.set(speed * direction)
            return False
        else:
            motor.set(0)
            return True