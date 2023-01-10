# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:24:50 2022

@author: namam
"""
#https://pinout.xyz/pinout/i2c
#https://libraries.io/pypi/smbus2

"""
import smbus
DEVICE_BUS = 1 # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
DEVICE_ADDR = 0x15   #7 bit address (will be left shifted to add the read write bit)
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
"""

"""
import PAC1720

test = PAC1720.PPAC1720()
current = test.ReadCurrent()
print(current)
"""


import i2c1

test = i2c1.I2C1(0xaa)
test.WRITE_BYTE(0x01,0xbb)

