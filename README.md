# Hydrom

This is the result of my fun little side project to automate and track fermentation using my Hydrom floating hydrometer.

The project is broken up into a few different scripts.

- sqlite.setup.py
This script creates the SQLite DB that is the core of the project including all tables and indexes

- hydrom_monitor.py
This script captures the MQTT messages the Hydrom sends to the mosquitto server and writes them to the appropriate tables in SQLite

- hydrom_control.py
This script reads the most recent data and controls the P100 smart plug to turn a heating device on or off

- hydrom_control.sh
This is a wrapper script to make it a little easier to create a cron entry for the corresponding python script.

- hydrom_graph.py
This script graphs the Specific Gravity, Temperature and Battery into an html file so it can be viewed on my internal network

- hydrom_graph.sh
This is a wrapper script to make it a little easier to create a cron entry for the corresponding python script.

- hydrom_cleanup.py
This script removes entries older than 14 days to prevent the DB getting too big

- hydrom_cleanup.sh
This is a wrapper script to make it a little easier to create a cron entry for the corresponding python script.