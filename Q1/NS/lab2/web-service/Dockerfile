# Use the official image as a parent image
FROM ubuntu:latest

# Update the system, install OpenSSH Server, and set up users
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y sudo nano openssh-server iptables ufw iproute2 snort

# Create user and set password for user and root user
RUN useradd -rm -d /home/user -s /bin/bash -g root -G sudo -u 1001 user && \
    echo 'user:password' | chpasswd && \
    echo 'root:password' | chpasswd

# Set up configuration
RUN mkdir /var/run/sshd && \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/LogLevel INFO/LogLevel VERBOSE/' /etc/ssh/sshd_config &&\
    echo 'alert tcp any any -> any 22 (msg:"SSH Brute Force Attempt"; sid:1000001; rev:1;)' >> /etc/snort/rules/local.rules

# Expose the SSH port
EXPOSE 22

# Run SSH
CMD ["/usr/sbin/sshd", "-D"]
