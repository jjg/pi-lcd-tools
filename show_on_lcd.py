#!/usr/bin/python
import Adafruit_CharLCD as LCD
import sys

def white():
    lcd.set_color(1.0,1.0,1.0)

def red():
	lcd.set_color(1.0,0.0,0.0)

def green():
    lcd.set_color(0.0,1.0,0.0)

def yellow():
    lcd.set_color(1.0,1.0,0.0)

# init color options
colors = {'white': white,
			'red': red,
			'green': green,
			'yellow': yellow}

# init lcd library for pi plate
lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1.0, 1.0, 1.0)

lcd.message(sys.argv[1])

if len(sys.argv) > 2:
	colors[sys.argv[2]]()
