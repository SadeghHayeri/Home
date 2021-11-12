from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    sleep(12 * 3600)
    led.on()
    sleep(6 * 3600)
    led.off()
    sleep(6 * 3600)
