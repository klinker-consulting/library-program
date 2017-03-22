import time
import random
import RPi.GPIO as GPIO

light_pins = [12, 7, 36]

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

def setup_pin(pin):
    GPIO.setup(pin, GPIO.OUT)

def turn_on_light(pin):
    GPIO.output(pin, GPIO.HIGH)

def turn_off_light(pin):
    GPIO.output(pin, GPIO.LOW)

for pin in light_pins:
    setup_pin(pin)

setup_pin(36)
turn_on_light(36)

current_pin = light_pins[0]
while(True):
    turn_off_light(current_pin)
    time.sleep(1)

    current_pin = light_pins[random.randint(0, len(light_pins) - 1)]
    turn_on_light(current_pin)
    time.sleep(1)

