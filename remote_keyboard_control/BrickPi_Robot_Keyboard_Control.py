from robot_responses import Responses
from keyboard import Keyboard


class Robot:

    def __init__( self ):
        self.responses = Responses()
        self.keyboard = Keyboard()

    def implement( self ):
        self.responses.speed_increase()
        self.responses.speed_decrease()
        self.responses.key_fwd()
        self.responses.key_back()
        self.responses.key_left()
        self.responses.key_right()

    def get_key( self ):
        self.keyboard.key = keyboard.stdscr.getkey()

    def restore_env( self ):
        keyboard.curses.nocbreak()
        keyboard.curses.echo()
        keyboard.stdscr.keypad(False)
        keyboard.curses.endwin()
        print("Original terminal state restored")

    def check_exit( self ):
        if self.keyboard.check_key("e"):
            keyboard.stdscr.addstr("Exitting...\n")
            return True

robo = Robot()

def main(): 
    while True:
        robo.extract_key()
          if check_exit:
            break
        robo.implement()   

try: 
    if __name__ == '__main__': 
        main() 
        
finally:
    robo.reset_env() 


    




    
