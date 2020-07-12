#Limpia la salida de todos los pines 

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24,
        25, 8, 7, 12, 16, 20, 21]

for i in pins:
   GPIO.setup(i, GPIO.OUT)

GPIO.cleanup()

print('[DONE]---GPIO pins are clear.')
