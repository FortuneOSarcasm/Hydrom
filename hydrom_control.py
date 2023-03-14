#!/usr/bin/env python3
import sqlite3
from PyP100 import PyP100
from datetime import datetime

controlTemp = 22
controlAge = 3600
currentTime = datetime.now()

con = sqlite3.connect("hydrom001.db") # Create connection to hydrom001 database

cur = con.cursor() # Open cursor
cur.execute("SELECT * FROM temperature ORDER BY tempDate DESC LIMIT 1")
latestTemp = cur.fetchall()
for row in latestTemp:
    rowID = str(row[0])
    rowTemp = str(row[1])
    rowTS = row[2]
con.close()

lastRecordinS = (currentTime-datetime.strptime(rowTS, '%Y-%m-%d %H:%M:%S.%f')).total_seconds()

# if block for comparisons
if float(rowTemp) > controlTemp:
    p100 = PyP100.P100("<P100 IP Address>", "<YOUR EMAIL>", "<YOUR PASSWORD>")
    p100.handshake()
    p100.login()
    p100.turnOff()
    print("Temperature exceeds Max : Turning Heating Off : "  + str(rowTemp) + " : " + rowTS)
elif float(rowTemp) < controlTemp:
    p100 = PyP100.P100("<P100 IP Address>", "<YOUR EMAIL>", "<YOUR PASSWORD>")
    p100.handshake()
    p100.login()
    p100.turnOn()
    print("Temperature below Max : Turning Heating On : "  + str(rowTemp) + " : " + rowTS)
elif lastRecordinS > controlAge :
    p100 = PyP100.P100("<P100 IP Address>", "<YOUR EMAIL>", "<YOUR PASSWORD>")
    p100.handshake()
    p100.login()
    p100.turnOff()
    print("No Record recieved in 3600s Turning Heating Off")
else :
    print("All Systems Nominal : "  + str(rowTemp) + " : " + rowTS)