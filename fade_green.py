import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

p = GPIO.PWM(23, 500) #frequency 500Hz
p.start(0)
try:
    while 1:
        for dc in range(1, 100, 4):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        for dc in range(99, 0, -4):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
except KeyboardInterrupt:
    pass
p.stop
GPIO.cleanup()   
            

