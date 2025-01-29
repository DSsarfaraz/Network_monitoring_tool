"""
Database Module
===============
This module logs monitoring results to an SQLite database.
"""

import sqlite3
from datetime import datetime

def log_to_db(ip_address, status, latency, packet_loss):
    """
    Log monitoring results to the database.

    Args:
        ip_address (str): The IP address of the device.
        status (str): The status of the device ("Success" or "Failed").
        latency (float): The average latency in milliseconds.
        packet_loss (float): The packet loss percentage.
    """
    conn = sqlite3.connect("network_monitor.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS monitoring_logs
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       ip_address TEXT,
                       status TEXT,
                       latency REAL,
                       packet_loss REAL,
                       timestamp DATETIME)''')
    cursor.execute('''INSERT INTO monitoring_logs (ip_address, status, latency, packet_loss, timestamp)
                      VALUES (?, ?, ?, ?, ?)''',
                   (ip_address, status, latency, packet_loss, datetime.now()))
    conn.commit()
    conn.close()