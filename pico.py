from bme680 import *
from machine import I2C, Pin
import time
scl = 13
sda = 12
bme = BME680_I2C(I2C(0, Pin(scl), Pin(sda)))

while(True):
    with open("out.txt", "a") as f:
        print(f"{time.time()}, {bme.temperature}, {bme.humidity}, {bme.pressure}, {bme.gas};", file = f)
        time.sleep(1)