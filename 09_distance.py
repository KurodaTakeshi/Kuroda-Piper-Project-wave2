#! /usr/bin/python
import RPi.GPIO as GPIO
import time

def checkdist():
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(16, GPIO.LOW)
    while not GPIO.input(18):
        pass
    t1 = time.time()
    while GPIO.input(18):
        pass
    t2 = time.time()
    return (t2-t1)*340/2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.IN)
time.sleep(5)
try:
    while True:
        temp = float(checkdist())
        print(temp)
        if temp <= 0.1:
            import os
            os.system("python3 Record_form.py")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()



