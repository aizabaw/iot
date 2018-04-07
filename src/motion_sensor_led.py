from gpiozero import MotionSensor, LED
import time

led = LED(25)
sensor = MotionSensor(4)

print("Starting...")

#sensor.wait_for_inactive()

print("Ready")

while True:
    led.off()
    time.sleep(2)
    print("{0} Motion detected".format(time.strftime("%B %d, %H:%M:%S")))
    led.on()
    time.sleep(1)
