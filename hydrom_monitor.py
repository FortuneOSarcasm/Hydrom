#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import sqlite3
from datetime import datetime

con = sqlite3.connect("hydrom001.db") # Create connection to hydrom001 database

TEMP_TOPIC="sensors/office/hydrom001/Hydrom001/temperature"
BATT_TOPIC="sensors/office/hydrom001/Hydrom001/battery"
SG_TOPIC="sensors/office/hydrom001/Hydrom001/tilt_SG"

def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")
    # Subscribe here!
    client.subscribe([(TEMP_TOPIC,2),(BATT_TOPIC,2),(SG_TOPIC,2)])

def on_message(client, userdata, msg):
    cur = con.cursor() # Open cursor
    if msg.topic.lower() == TEMP_TOPIC.lower() :
        cur.execute("INSERT INTO temperature (temperature, tempDate) VALUES (?,?)",(str(msg.payload.decode("utf-8")),datetime.now()))
        con.commit()
    if msg.topic.lower() == BATT_TOPIC.lower() :
        cur.execute("INSERT INTO battery (battery, battDate) VALUES (?,?)",(str(msg.payload.decode("utf-8")),datetime.now()))
        con.commit()
    if msg.topic.lower() == SG_TOPIC.lower() :
        cur.execute("INSERT INTO tilt_sg (tilt_sg, sgDate) VALUES (?,?)",(str(msg.payload.decode("utf-8")),datetime.now()))
        con.commit()

client = mqtt.Client("hydrom_control") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("hydrom", "hydrom")
client.connect('127.0.0.1', 1883)
# client.loop_forever()  # Start networking daemon
while True:
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()
        con.close()
        exit(0)
    except:
        raise
