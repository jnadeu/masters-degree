from scapy.all import *
import sys

def syn_scan(target_ip):
    # Scans the first 1024 ports
    ports = range(1, 1025)  
    print(f"Starting SYN scan on {target_ip}")

    for port in ports:
        # Send an SYN packet to the target IP and port
        syn_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        response = sr1(syn_packet, timeout=1, verbose=False)

        # Check if there was a response (SYN/ACK means the port is open)
        if response and response.haslayer(TCP):
            if response[TCP].flags == "SA":  # SYN/ACK received
                print(f"Port {port} is open")
            # If we want to print close port too uncomment the following two lines
            #elif response[TCP].flags == "RA":  # RST/ACK means closed
                #print(f"Port {port} is closed")

if __name__ == "__main__":
    target_ip = sys.argv[1]
    syn_scan(target_ip)
