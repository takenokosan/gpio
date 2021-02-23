import RPi.GPIO as GPIO
import time

PNO = 21 # 抵抗に繋いだ側の、GPIOポート番号

GPIO.setmode(GPIO.BCM)
GPIO.setup(PNO, GPIO.OUT)

for i in range(15):
    GPIO.output(PNO, GPIO.HIGH) # 点灯
    time.sleep(0.4)
    GPIO.output(PNO, GPIO.LOW) # 消灯
    time.sleep(0.4)

GPIO.cleanup()
