"""
Visualization Module
====================
This module visualizes network metrics using Matplotlib.
"""

import sqlite3
import matplotlib.pyplot as plt

def plot_metrics(ip_address):
    """
    Plot latency and packet loss over time for a specific device.

    Args:
        ip_address (str): The IP address of the device to visualize.
    """
    conn = sqlite3.connect("network_monitor.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, latency, packet_loss FROM monitoring_logs WHERE ip_address = ?", (ip_address,))
    data = cursor.fetchall()
    conn.close()

    timestamps = [row[0] for row in data]
    latency = [row[1] for row in data]
    packet_loss = [row[2] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, latency, label="Latency (ms)")
    plt.plot(timestamps, packet_loss, label="Packet Loss (%)")
    plt.xlabel("Time")
    plt.ylabel("Metrics")
    plt.title(f"Network Metrics for {ip_address}")
    plt.legend()
    plt.show()