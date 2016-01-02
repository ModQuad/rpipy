import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

led_red = 18
led_green = 23
led_blue = 24

GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)

try:         
    while True:
        GPIO.output(led_red, True)  # LED on
        GPIO.output(led_green, True)  # LED on
        GPIO.output(led_blue, True)  # LED on
        time.sleep(0.5)             # delay 0.5 seconds
        GPIO.output(led_red, False) # LED off
        GPIO.output(led_green, False) # LED off
        GPIO.output(led_blue, False) # LED off
        time.sleep(0.5)             # delay 0.5 seconds
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()
