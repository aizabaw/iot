from gpiozero import DistanceSensor, Buzzer
import time

sensor = DistanceSensor(echo=24, trigger=23)
buzzer = Buzzer(14)

print('Waiting for sensor to settle...')
time.sleep(2)

while True:
    d = sensor.distance #distance in meters
    #print("{a} Detected object {b} meter(s) away".format(a=time.strftime("%B %d, %H:%M:%S"), b=str(d)))

    #alarm
    if d < 0.25:
        #set off alarm
        print('{a} WARNING! Detected object {b} meters away'.format(a=time.strftime('%B %d, %H:%M:%S'), b=d))
        buzzer.beep(0.08, 0.08, 1)

    time.sleep(1)
