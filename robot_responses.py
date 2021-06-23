from keyboard import Keyboard
from robot_actions import Actions

class Responses:

    def __init__( self ):
        self.actions = Actions() 
        self.keys = Keyboard()

    def speed_increase( self ):
        if self.keys.check_key("w"): 
            self.actions.check_change_speed(25)

    def speed_decrease( self ):
        if self.keys.check_key("s"): 
            self.actions.check_change_speed(-25)
            
    def key_fwd( self ):
        if self.keys.check_key("KEY_UP"): 
            self.actions.fwd()

    def key_back( self ):
        if self.keys.check_key("KEY_DOWN"): 
            self.actions.back()

    def key_left( self ):
        if self.keys.check_key("KEY_LEFT"): 
            self.actions.left()

    def key_right( self ):
        if self.keys.check_key("KEY_RIGHT"): 
            self.actions.right()

    
