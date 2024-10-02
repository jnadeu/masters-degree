from scapy.all import *

def detect_xmas_scan(packet):
    # Check if the packet is a TCP packet
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)

        # Check if FIN, PSH, and URG flags are set (Xmas scan)
        if tcp_layer.flags == "FPU":
            print(f"Xmas scan detected from {packet[IP].src}")

if __name__ == "__main__":
    print("Sniffing for Xmas scans...")
    # Sniff incoming packets and apply the detect_xmas_scan function to each one
    sniff(filter="tcp", prn=detect_xmas_scan)
