
class RobotSpeed:

    def __init__( self, power = 200, originalP = 200 ):
        self.power = power
        self.originalP = originalP

    def check_out_range_speed( self, difference1 = 50 ):
        if abs(self.originalP - self.power) >= difference1:
            return True;

     def check_in_range_speed( self, difference2 = 50 ):
        if abs(self.originalP - self.power) <= difference2:
            return True;

    def check_max( self ):
        if self.power >= 250:
            return True 

    def check_min( self ):
        if self.power <= -250:
            return True 

    def power_reset( self ):
        self.originalP = self.power

    def change_speed( self, amt ):
        self.power += amt

    def reset_power( self ):
        self.originalP = self.power
