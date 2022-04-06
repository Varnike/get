import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.OUT)

while True:
    GPIO.output(15, GPIO.input(14))