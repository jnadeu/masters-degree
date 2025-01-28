#!/bin/bash

# Redirect HTTP/HTTPS traffic using iptables
iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 80
iptables -t nat -A PREROUTING -p tcp --dport 80 -j ACCEPT

iptables -t nat -L PREROUTING
