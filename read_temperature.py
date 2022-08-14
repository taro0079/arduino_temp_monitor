import serial
import time
import re


def read_temperature(ser):
    # ser = serial.Serial("COM5", 57600)
    pattern = '\d+\.+\d{2}'
    result = ser.readline().decode()
    r = re.findall(pattern, result)
    if len(r) > 2:
        temp = r[1]
    else:
        temp = 0

    return temp
