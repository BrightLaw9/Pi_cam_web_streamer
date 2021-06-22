from BrickPi import *
from robot_speed import RobotSpeed

class RobotMove:

    def __init__( self ):

        self.speed = RobotSpeed() 
        BrickPiSetup()

        #Setup - Ports for Motors
        BrickPi.MotorEnable[PORT_A] = 1
        BrickPi.MotorEnable[PORT_D] = 1

        BrickPiSetupSensors()


    def move( self, speed1, speed2 ):
        BrickPi.MotorSpeed[PORT_A] = speed1
        BrickPi.MotorSpeed[PORT_D] = speed2
        BrickPiUpdateValues()

    def move_fwd( self ):
        self.move( self.speed.power, self.speed.power)

    def move_back( self ):
        self.move( -self.speed.power, -self.speed.power)

    def move_left( self ):
        self.move( -self.speed.power, self.speed.power)

    def move_right( self ):
        self.move( self.speed.power, -self.speed.power)





    
