#!/usr/bin/env python3
import pandas as pd
import sqlite3
import plotly.express as px
import os
from pathlib import Path
from base64 import b64encode
import time

directory = '/var/www/hydrom/'

if os.path.exists(directory + "index.html"):
    os.remove(directory + "index.html")

f = open(directory + 'index.html', 'a')
f.write('<html><head><title>Hydrom001 Graphs</title></head>\n')
f.write('<body>\n')
f.write('<p align="center">\n')
f.close()

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("~/hydrom/hydrom001.db")

df = pd.read_sql_query("SELECT temperature, tempDate FROM temperature", con)
# Verify that result of SQL query is stored in the dataframe
fig = px.line(df, x = 'tempDate', y = 'temperature', title="Hydrom001 Temperature", width=2000)
fig.update_layout(yaxis_range=[0,25])
img_bytes = fig.to_image(format="png")
encoding = b64encode(img_bytes).decode()
img_b64 = "data:image/png;base64," + encoding
with open(directory + 'index.html', 'a') as f:
    f.write("<img src=" + img_b64 + ">\n")

df = pd.read_sql_query("SELECT tilt_sg, sgDate FROM tilt_sg", con)
# Verify that result of SQL query is stored in the dataframe
fig = px.line(df, x = 'sgDate', y = 'tilt_sg', title="Hydrom001 Specific Gravity", width=2000)
fig.update_layout(yaxis_range=[0.8,1.5])
img_bytes = fig.to_image(format="png")
encoding = b64encode(img_bytes).decode()
img_b64 = "data:image/png;base64," + encoding
with open(directory + 'index.html', 'a') as f:
    f.write("<img src=" + img_b64 + ">\n")

df = pd.read_sql_query("SELECT battery, battDate FROM battery", con)
# Verify that result of SQL query is stored in the dataframe
fig = px.line(df, x = 'battDate', y = 'battery', title="Hydrom001 Battery", width=2000)
fig.update_layout(yaxis_range=[3.7,4.4])
img_bytes = fig.to_image(format="png")
encoding = b64encode(img_bytes).decode()
img_b64 = "data:image/png;base64," + encoding
with open(directory + 'index.html', 'a') as f:
    f.write("<img src=" + img_b64 + ">\n")

con.close()

f = open(directory + 'index.html', 'a')
f.write('</body>\n')
f.write('</html>\n')
f.close()
