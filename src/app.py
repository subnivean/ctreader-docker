#!/usr/bin/env python
"""Insert latest CT readings into a sqlite database
"""
import datetime
import serial
import sqlite3
import time

DBPATH = "/appdata/heatpumpctdata.db"
TBLNAME = "housectdata"
OUTDATAPATH = "/appdata/house_heat_pump_ct_readings.log"
DEV = "/dev/ttyAMA0"

now = datetime.datetime.now().isoformat(timespec='milliseconds', sep='T')
now += '+00:00'  # UTC
ser = serial.Serial(DEV, 38400)

n = 0
while (n := n + 1) < 10:
    try:
        response = [float(e)
                    for e in ser.readline() \
                                .decode('utf-8') \
                                .strip() \
                                .split()[1:]]
        # print("Got it!")
        break
    except (serial.SerialException, ValueError):
        # print("Error, sleeping...")
        time.sleep(1)

with open(OUTDATAPATH, 'a') as fh:
    ct1, ct2, ct3, ct4, *temps = response
    line = f"{now}, {ct1:7.2f}, {ct2:7.2f}, {ct3:7.2f}, {ct4:7.2f}"
    fh.write(f"{line}\n")
    #print(line)

rec = (now, *response[0:4])
sql = f"""INSERT INTO {TBLNAME}(DateTime,ct0,ct1,ct2,ct3)
        VALUES(?,?,?,?,?)"""

with sqlite3.connect(DBPATH) as conn:
    cur = conn.cursor()
    cur.execute(sql, rec)
    conn.commit()