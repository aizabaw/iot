from gpiozero import LED
from time import sleep

red = LED(25)
green = LED(8)

print("Starting")

while True:

    print("RED")
    red.on()
    green.off()
    sleep(2)

    print("GREEN")
    red.off()
    green.on()
    sleep(2)