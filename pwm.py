import RPi.GPIO as GPIO
import time

PNO = 5 # 抵抗に繋いだ側の、GPIOポート番号

GPIO.setmode(GPIO.BCM)
GPIO.setup(PNO, GPIO.OUT)
pwm = GPIO.PWM(PNO,1000)

for i in range(15):
    pwm.start(20) # 点灯
    time.sleep(0.4)
    pwm.stop()
    time.sleep(0.4)

GPIO.cleanup()
