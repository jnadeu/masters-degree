FROM nginx:latest

# Copy NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy certificates
COPY certs /etc/nginx/certs

# Copy HTML files
COPY html /usr/share/nginx/html
