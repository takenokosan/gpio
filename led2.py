import RPi.GPIO as GPIO
import time

pins = [17,27,22,5,6,13,19,26] # 抵抗に繋いだ側の、GPIOポート番号

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins,GPIO.HIGH)

for i in range(8):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW) # 点灯
        time.sleep(0.02)
        GPIO.output(pin, GPIO.HIGH) # 消灯
        time.sleep(0.02)

GPIO.cleanup()
