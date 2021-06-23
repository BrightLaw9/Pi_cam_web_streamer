from robot.robot_movement import RobotMove
from robot.robot_speed import RobotSpeed
from keyboard import Keyboard 

class Actions:

    def __init__( self ):
        self.motion = RobotMove() 
        self.speed = RobotSpeed()
        self.keys = Keyboard()


    def check_change_speed( self, speed ):
        if not self.speed.check_max():
            self.speed.change_speed(speed)
            self.keys.print_line("Power: " + str(self.speed.power))
            if check_out_range_speed():
                self.keys.print_line("Must reset, press r")

        else: 
            self.keys.print_line("Max power reached")


    def reset_speed( self ):
        self.speed.power_reset()
        self.keys.print_line("Power reset, new range: %s - %s \n" % (originalP - 50, originalP + 50))
            
    def fwd( self ):
        self.motion.move_fwd()
        compare_key_print("Fwd")

    def back( self ):
        self.motion.move_back()
        compare_key_print("Back")

    def left( self ):
        self.motion.move_left()
        compare_key_print("Left")

    def right( self ):
        self.motion.move_right()
        compare_key_print("Right")

    

    
