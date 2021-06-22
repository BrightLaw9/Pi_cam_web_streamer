import curses

class Keyboard:

    def __init__( self, key = "", key2 = ""):
        self.key = key
        self.key2 = key2
        self.stdscr = curses.initscr()

        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)

    def get_key2( self ):
        self.key_2 = stdscr.getkey()

    def check_key( self, key_check ):
        if self.key == key_check:
            return True

    def compare_key_print( self, command ):
        if self.key != self.key2:
            self.stdscr.addstr(command + "\n")
            self.get_key2() 

    def print_line( self, line ):
        self.stdscr.addstr(line + "\n")
