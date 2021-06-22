#from BrickPi import *


class Robot:

    def __init__( self, power = 200, originalP = 200 ):
        self.power = power
        self.originalP = originalP

        BrickPiSetup()

        #Setup - Ports for Motors
        BrickPi.MotorEnable[PORT_A] = 1
        BrickPi.MotorEnable[PORT_D] = 1

        BrickPiSetupSensors()


    def move( self, speed1, speed2 ):
        BrickPi.MotorSpeed[PORT_A] = speed1
        BrickPi.MotorSpeed[PORT_D] = speed2
        BrickPiUpdateValues()

    def move_fwd_back( self ):
        move( self, self.power, self.power)

    def move_left( self ):
        move( self, -self.power, self.power)

    def move_right( self ):
        move( self, self.power, -self.power)





    
