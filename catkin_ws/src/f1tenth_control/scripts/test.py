#!/usr/bin/env python
import rospy

import tty
import sys
import termios

orig_settings = termios.tcgetattr(sys.stdin)

tty.setraw(sys.stdin)
x = 0
y = 0
while x != chr(27) or y != chr(27): # ESC
    ch=sys.stdin.read(2)
    x = ch[0]
    y = ch[1]
    print("You pressed", x,y)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)    
