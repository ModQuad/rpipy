import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

red = 18
blue = 24

GPIO.setup(red, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

blue = GPIO.PWM(25, 100)    # create object white for PWM on port 25 at 100 Hertz  
red = GPIO.PWM(24, 100)

red.start(0)
blue.start(100)

pause_time = 0.02

try:         
    while True:
       for i in range(0,101):      # 101 because it stops when it finishes 100  
            blue.ChangeDutyCycle(i)  
            red.ChangeDutyCycle(100 - i)  
            sleep(pause_time)  
        for i in range(100,-1,-1):      # from 100 to zero in steps of -1  
            blue.ChangeDutyCycle(i)  
            red.ChangeDutyCycle(100 - i)  
            sleep(pause_time)
        
finally:  
    print("Cleaning up")
    blue.stop()
    red.stop()
    GPIO.cleanup()
