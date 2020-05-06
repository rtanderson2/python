#pushBlinker.py
import RPi.GPIO as  GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleepTime = .25

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
                sleep(sleepTime)
                GPIO.output(lightPin, False)
                sleep(sleepTime)
                x += 1
        else:
            GPIO.output(lightPin, False)
finally:
    GPIO.cleanup()
