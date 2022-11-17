#!/usr/bin/env python
"""Insert latest CT readings into a sqlite database
"""
import datetime
import serial
import sqlite3
import sys
import time

LOCS = ('garage', 'house')
loc = sys.argv[1].lower()

if loc not in LOCS:
    print(f"`loc` must be one of {LOCS}")
    sys.exit(1)

DBPATH = "/appdata/heatpumpctdata.db"
TBLNAME = f"{loc}ctdata"
OUTDATAPATH = f"/appdata/{loc}_ct_readings.log"
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
    except (serial.SerialException, ValueError):
        #print("readline() error, sleeping...")
        time.sleep(1)
        continue

    if len(response) == 8:
        # print("Breaking...")
        break
    else:
        #print("Not enough fields, sleeping...")
        time.sleep(1)
        continue
else:
    print("Couldn't get a good reading!")
    1/0

rec = (now, *response[0:4])
sql = f"""INSERT INTO {TBLNAME}(DateTime,ct0,ct1,ct2,ct3)
        VALUES(?,?,?,?,?)"""

with sqlite3.connect(DBPATH) as conn:
    cur = conn.cursor()
    cur.execute(sql, rec)
    conn.commit()
