#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("hydrom001.db") # Create connection to hydrom001 database

cur = con.cursor() # Open cursor

cur.execute("DELETE FROM temperature WHERE date(tempDate) < DATE('now','-14 day')")
con.commit()
cur.execute("DELETE FROM battery WHERE date(battDate) < DATE('now','-14 day')")
con.commit()
cur.execute("DELETE FROM tilt_sg WHERE date(sgDate) < DATE('now','-14 day')")
con.commit()
con.close()
