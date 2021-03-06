#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11 --- led
BtnPin = 12    # pin12 --- button

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off

def loop():
    while True:
        if GPIO.input(BtnPin) == GPIO.HIGH: # Check whether the button is pressed or not.
            time.sleep(0)
            if GPIO.input(BtnPin) == GPIO.HIGH:
                #status = not status
                #GPIO.output(LedPin, status)
                import os
                os.system("python3 csv_send.py")
                #print 'The status of led is toggled !'
            while(not not GPIO.input(BtnPin)):
                pass

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

