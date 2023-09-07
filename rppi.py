#!/usr/bin/env python

import bme680

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)


while True:
    if sensor.get_sensor_data():
        with open("out.txt", "a") as f:
            print(f"{time.time()}s, {sensor.data.temperature:.4f} C, {sensor.data.pressure:.4f} hPa, {sensor.data.humidity:.4f} %RH;", file = f)
