# Use a minimal image with curl installed
FROM debian:bullseye-slim

# Install curl and necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
nmap \
hydra \
openssh-client \
net-tools

# Copy passwords list
COPY passwords.txt /