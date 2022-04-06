import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(element) for element in bin(val) [2:].zfill(8)]

try:
    print("T = ")
    T = float(input())

    while 1:
        var = 0

        while var < 255:
            GPIO.output(dac, dec2bin(var))
            time.sleep(T/512)
            var += 1
        while var > 0:
            GPIO.output(dac, dec2bin(var))
            time.sleep(T/512)
            var -= 1
except  KeyboardInterrupt:
    print("END")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
