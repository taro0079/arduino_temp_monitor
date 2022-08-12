from cgitb import reset
import serial
import time
import re


def read_temperature():
    ser = serial.Serial("COM5", 57600)
    pattern = '\d+\.+\d{2}'
    result = ser.readline().decode()
    r = re.findall(pattern, result)
    if len(r) > 2:
        temp = r[1]
    else:
        temp = 0

    return temp


def main():
    print(read_temperature())


if __name__ == "__main__":
    main()
