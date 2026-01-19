from machine import Pin
from time import sleep

button = Pin(15, Pin.IN, Pin.PULL_UP)
button2 = Pin(18, Pin.IN, Pin.PULL_UP)
button3 = Pin(19, Pin.IN, Pin.PULL_UP)
button4 = Pin(21, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        print("pressed")
    elif button2.value() == 0:
        print("two")
    elif button3.value() == 0:
        print("three")
    elif button4.value() == 0:
        print("four")
    else:
        print("released")
    sleep(0.05)
