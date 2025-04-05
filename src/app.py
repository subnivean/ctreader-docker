#!/usr/bin/env python
"""Print latest CT readings in JSON format for Home Assistant consumption"""
import datetime

import json
import serial
import sys
import time

# TESTING
#print('{"DateTime": "2025-04-05T03:58:54.311+00:00", "ct0": 24.71, "bosch_range_watts_raw": 239.95, "ct2": 25.51, "heat_pump_watts_raw": 484.29}')
#sys.exit(0)
# END TESTING

DEV = "/dev/ttyAMA0"

ser = serial.Serial(DEV, 38400)

# Loop until we get valid data
n = 0
while (n := n + 1) < 10:
    try:
        response = [
            float(e) for e in ser.readline().decode("utf-8").strip().split()[1:]
        ]
        # print("Got it!")
    except (serial.SerialException, ValueError):
        # print("readline() error, sleeping...")
        time.sleep(1)
        continue

    if len(response) == 8:
        # print("All fields found, breaking...")
        break
    else:
        # print("Not enough fields, sleeping...")
        time.sleep(1)
        continue
else:
    print("Couldn't get a good reading!")
    sys.exit(1)

now = datetime.datetime.now().isoformat(timespec="milliseconds", sep="T")
now += "+00:00"  # UTC
rec = (now, *response[0:4])

recd = dict(
    DateTime=now,
    ct0=response[0],
    bosch_range_watts_raw=response[1],
    ct2=response[2],
    heat_pump_watts_raw=response[3],
)

print(json.dumps(recd))
