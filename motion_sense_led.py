from gpiozero import MotionSensor
import time

pir = MotionSensor(4)

print('Waiting for PIR to settle')
pir.wait_for_no_motion()

while True:
    print('Ready')
    pir.wait_for_motion()
    print('{0} Motion detected'.format(time.strftime("%B %d, %H:%M:%S")))
    time.sleep(3)