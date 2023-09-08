from bme680 import *
from machine import SPI, Pin
import time
spi = SPI(sck=Pin(2), mosi=Pin(4), miso=Pin(5))
cs = Pin(3, mode=Pin.OUT, value=1) 
bme = BME680_I2C(spi)

cs(0)
while(True):
    with open("out.txt", "a") as f:
        print(f"{time.time()}, {bme.temperature}, {bme.humidity}, {bme.pressure}, {bme.gas};", file = f)
        time.sleep(1)