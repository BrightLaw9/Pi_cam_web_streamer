# BrickPi Keyboard Control for Motors

#Importing BrickPi and curses libraries 

from BrickPi import *

import curses

#Screen and keyboard environment setup and initalization
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


BrickPiSetup()

#Setup - Ports for Motors
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_D] = 1

BrickPiSetupSensors()

#Move function for motor movement
def move(speed1, speed2):
    BrickPi.MotorSpeed[PORT_A] = speed1
    BrickPi.MotorSpeed[PORT_D] = speed2
    BrickPiUpdateValues()

#Variable Intialization for later use
originalP = 200
power = 200
key_2 = ""

try:
    while True:
        #Get key from keyboard
        key = stdscr.getkey()
        #Exit the program if "e" pressed
        if key == "e":
            stdscr.addstr("Exitting...\n")
            break            
    #User increase/decrease speeds
        elif key == "w" and (originalP + 50) > power:
            #Check if power exceeds 250, if so - don't allow b/c max power on NXT Motors is 255
            if power >= 250:
                stdscr.addstr("Max power reached\n")
                continue
            power += 25
            stdscr.addstr("Power: " + str(power) + "\n")
            if (originalP + 50) <= power:
                stdscr.addstr("Must reset, press r\n")
        elif key == "s" and (originalP - 50) < power:
            if power <= -250:
                stdscr.addstr("Min power reached")
                continue
            power -= 25
            stdscr.addstr("Power: " + str(power) + "\n")
            if (originalP - 50) >= power:
                stdscr.addstr("Must reset, press r\n")
    #Reset button
        elif key == "r":
            originalP = power
            stdscr.addstr("Power reset, new range: %s - %s \n" % (originalP - 50, originalP + 50))
    #Motor keyboard control movements
        elif key == "KEY_UP":
            move(power, power)
            #This is checking if previous key was the same - if so, don't print
            if key == key_2:
                continue
            stdscr.addstr("Fwd\n")
            key_2 = stdscr.getkey()
        elif key == "KEY_DOWN":
            move(-power, -power)
            if key == key_2:
                continue
            stdscr.addstr("Back\n")
            key_2 = stdscr.getkey()
        elif key == "KEY_LEFT":
            move(-power, power)
            if key == key_2:
                continue
            stdscr.addstr("Left\n")
            key_2 = stdscr.getkey()
        elif key == "KEY_RIGHT":
            move(power, -power)
            if key == key_2:
                continue
            stdscr.addstr("Right\n")
            key_2 = stdscr.getkey()
            

finally:
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(False)
    curses.endwin()
    print("Original terminal state restored")


    


