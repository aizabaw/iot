from gpiozero import DistanceSensor, Buzzer
import picamera
import time

sensor = DistanceSensor(echo=24, trigger=23)
buzzer = Buzzer(3)
time.sleep(5)
print('Waiting for sensor to settle')

while True:
    d = sensor.distance
    print('Sensing...')

    if d <1:
        print('WARNING! Object detected {} meter away'.format(d))
        buzzer.beep(0.08, 0.08, 1)

    time.sleep(2)
