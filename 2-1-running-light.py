import RPi.GPIO as GPIO
import time
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
i = 0
while i < 3:
    for number in leds:
        GPIO.output(number, 1)
        time.sleep(0.2)
        GPIO.output(number, 0)
        time.sleep(0.2)
    i += 1
   
GPIO.output(leds, 0)
GPIO.cleanup()
