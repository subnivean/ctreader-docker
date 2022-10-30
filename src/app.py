#!/usr/bin/env python

import datetime
import serial
import time

OUTDATAPATH = "/appdata/house_heat_pump_ct_readings.log"
DEV = "/dev/ttyAMA0"

now = datetime.datetime.now().isoformat(timespec='milliseconds', sep='T')
now += '+00:00'  # UTC
ser = serial.Serial(DEV, 38400)
response = [float(e) for e in ser.readline().decode('utf-8').strip().split()[1:]]
with open(OUTDATAPATH, 'a') as fh:
    ct1, ct2, ct3, ct4, *temps = response
    line = f"{now}, {ct1:7.2f}, {ct2:7.2f}, {ct3:7.2f}, {ct4:7.2f}"
    fh.write(f"{line}\n")
    #print(line)
