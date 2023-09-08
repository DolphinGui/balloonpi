from bme680 import *
from machine import SPI, Pin
import time
spi = SPI(sck=Pin(2), mosi=Pin(4), miso=Pin(5))
cs = Pin(3, mode=Pin.OUT, value=1) 
bme = BME680_SPI(spi)

cs(0)
while(True):
    with open("out.txt", "a") as f:
        print(f"{time.time()}, {bme.temperature:.4f} C, {bme.humidity:.4f}, {bme.pressure:.4f} hPa, {bme.gas:.4f} %RH;", file = f)
        f.flush()
        time.sleep(1)