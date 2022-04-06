import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(element) for element in bin(val) [2:].zfill(8)]

try:
    while True:
        print("enter num(0-255)")
        val = input()
        if val == 'q':
            break
        try:
            if float(val) % 1 != 0:
                print("invalid input")
                continue
            elif int(val) > 255:
                print("num is too big")
                continue
            elif int(val) < 0:
                print("num is too low")
                continue

            val = int(val)
            GPIO.output(dac, dec2bin(val))

            print("CAP voltage: ", "{:.4f}".format(3.3 * val / 255), "V")
            
        except ValueError:
            print("NaN")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
