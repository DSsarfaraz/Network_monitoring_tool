"""
GUI Module
==========
This module provides a user-friendly interface for the Network Monitoring Tool.
"""

import tkinter as tk
from tkinter import messagebox
from device_discovery import discover_devices
from monitoring import monitor_devices
from visualization import plot_metrics

def start_monitoring():
    """
    Start monitoring devices in the specified IP range.
    """
    ip_range = ip_range_entry.get()
    devices = discover_devices(ip_range)
    monitor_devices(devices)
    messagebox.showinfo("Monitoring Complete", "Network monitoring completed successfully.")

def show_metrics():
    """
    Show metrics for a specific device.
    """
    ip_address = ip_address_entry.get()
    plot_metrics(ip_address)

# Create the main window
root = tk.Tk()
root.title("Network Monitoring Tool")

# Add widgets
tk.Label(root, text="IP Range (e.g., 192.168.1.1/24):").grid(row=0, column=0)
ip_range_entry = tk.Entry(root)
ip_range_entry.grid(row=0, column=1)

tk.Label(root, text="IP Address for Metrics:").grid(row=1, column=0)
ip_address_entry = tk.Entry(root)
ip_address_entry.grid(row=1, column=1)

tk.Button(root, text="Start Monitoring", command=start_monitoring).grid(row=2, column=0)
tk.Button(root, text="Show Metrics", command=show_metrics).grid(row=2, column=1)

# Run the GUI
root.mainloop()