from scapy.all import sniff

def packet_callback(packet):
    """Callback function to process each captured packet."""
    print(packet.summary())  # Print a summary of the packet

def start_sniffing(interface=None, count=10):
    """Start sniffing packets on the specified interface."""
    print(f"[*] Sniffing on {'all interfaces' if interface is None else interface}...")
    sniff(iface=interface, prn=packet_callback, count=count)

if __name__ == "__main__":
    # You can specify an interface, like 'eth0', or leave it as None to sniff on all interfaces
    interface = 'eth0'  # Change to your network interface, e.g., 'eth0'
    
    # Number of packets to capture; set to 0 for infinite
    packet_count = 0  # Change to a number for limited packets

    start_sniffing(interface, packet_count)