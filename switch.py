import RPi.GPIO as GPIO
import time

PNO = 12 # 抵抗に繋いだ側の、GPIOポート番号

GPIO.setmode(GPIO.BCM)
GPIO.setup(PNO, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(PNO):
        print("switchon")

GPIO.cleanup()
