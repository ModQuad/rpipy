import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 500) #frequency 500Hz
p.start(100)
try:
    while 1:
        for dc in range(1,101,4):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        for dc in range(100, 0, -4):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
except KeyboardInterrupt:
    pass
p.stop
GPIO.cleanup()   
            

