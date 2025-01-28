FROM kalilinux/kali-rolling

RUN apt update && apt install bettercap iptables sslstrip dsniff -y

COPY redirectIPtables.sh /
COPY ARPspoof.sh /

RUN chmod +x /redirectIPtables.sh /ARPspoof.sh

