#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("hydrom001.db") # Create connection to hydrom001 database

cur = con.cursor() # Open cursor

cur.execute("CREATE TABLE temperature(tempId INTEGER PRIMARY KEY AUTOINCREMENT, temperature INT, tempDate TEXT)")
cur.execute("CREATE INDEX idx_temp ON temperature(tempDate)")
cur.execute("CREATE TABLE battery (battId INTEGER PRIMARY KEY AUTOINCREMENT, battery INT, battDate TEXT)")
cur.execute("CREATE INDEX idx_batt ON battery(battDate)")
cur.execute("CREATE TABLE tilt_sg (sgId INTEGER PRIMARY KEY AUTOINCREMENT, tilt_sg INT, sgDate TEXT)")
cur.execute("CREATE INDEX idx_tilt ON tilt_sg(sgDate)")

con.commit()
con.close()
