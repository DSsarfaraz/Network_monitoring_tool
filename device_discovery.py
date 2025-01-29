"""
Device Discovery Module
=======================
This module uses ARP scans to discover devices on the network.
"""

from scapy.all import ARP, Ether, srp

def discover_devices(ip_range):
    """
    Discover devices on the network using ARP scans.

    Args:
        ip_range (str): The IP range to scan (e.g., "192.168.1.1/24").

    Returns:
        list: A list of dictionaries containing IP and MAC addresses of discovered devices.
    """
    print(f"Scanning network {ip_range}...")
    arp = ARP(pdst=ip_range)  # Create an ARP request packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address
    packet = ether / arp  # Combine Ethernet and ARP packets

    # Send the packet and receive responses
    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

# Example usage
if __name__ == "__main__":
    ip_range = "192.168.1.1/24"  # Replace with your network range
    devices = discover_devices(ip_range)
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")