from gpiozero import MotionSensor, Buzzer
import time

pir = MotionSensor(4)
bz = Buzzer(3)

print("{} Waiting for PIR to stabilize".format(time.strftime("%B %d, %H:%M:%S")))
pir.wait_for_inactive()

while True:
    print("Ready")
    pir.wait_for_active()
    print("{0} Motion detected".format(time.strftime("%B %d, %H:%M:%S")))
    bz.beep(0.25, 0.5, 4)
    time.sleep(1)
