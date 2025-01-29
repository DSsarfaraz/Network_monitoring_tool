"""
Network Monitoring Module
=========================
This module monitors devices by pinging them and logs their availability, latency, and packet loss.
"""

from ping3 import ping
import time
from database import log_to_db
from alerts import send_alert

def ping_device(ip_address):
    """
    Ping a device to check its availability and measure latency.

    Args:
        ip_address (str): The IP address of the device to ping.

    Returns:
        tuple: A tuple containing:
            - status (bool): True if the device is reachable, False otherwise.
            - latency (float): The latency in milliseconds if reachable, None otherwise.
    """
    response = ping(ip_address, timeout=2)  # Ping with a 2-second timeout
    if response is not None:
        return True, response * 1000  # Return latency in milliseconds
    else:
        return False, None

def monitor_devices(devices, interval=5, count=10):
    """
    Monitor a list of devices by pinging them repeatedly.

    Args:
        devices (list): A list of devices (each device is a dictionary with 'ip' and 'mac' keys).
        interval (int): Time interval between pings in seconds (default: 5).
        count (int): Number of pings to send per device (default: 10).
    """
    for device in devices:
        ip = device['ip']
        print(f"Monitoring {ip}...")
        successful_pings = 0
        total_latency = 0

        for i in range(count):
            status, latency = ping_device(ip)
            if status:
                successful_pings += 1
                total_latency += latency
                print(f"Ping {i+1}: Success. Latency: {latency:.2f} ms")
            else:
                print(f"Ping {i+1}: Failed.")
            time.sleep(interval)

        # Calculate packet loss and average latency
        packet_loss = ((count - successful_pings) / count) * 100
        avg_latency = total_latency / successful_pings if successful_pings > 0 else 0

        print(f"\nPacket Loss: {packet_loss:.2f}%")
        print(f"Average Latency: {avg_latency:.2f} ms")

        # Log results to the database
        log_to_db(ip, "Success" if successful_pings > 0 else "Failed", avg_latency, packet_loss)

        # Send an alert if the device is unreachable
        if successful_pings == 0:
            send_alert("recipient@example.com", "Network Alert", f"Device {ip} is unreachable!")