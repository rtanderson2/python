#counter.py
#buttonInput.py
import RPi.GPIO as  GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleepTime = .1

#GPIO Pin of the comment
lightPin = 4
buttonPin = 17

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin, False)

counter = 0

try:
    while True:
        if GPIO.input(buttonPin) == False:
            x = 0
            counter += 1
            while x < counter:
                GPIO.output(lightPin, True)
                sleep(.5)
                GPIO.output(lightPin, False)
                sleep(.5)
                x += 1
        else:
            GPIO.output(lightPin, False)
finally:
    GPIO.cleanup()