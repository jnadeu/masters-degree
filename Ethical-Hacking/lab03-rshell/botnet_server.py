import socketserver

# Define BotServer to handles each incoming client connection.
class BotServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall("Welcome to the bot server!\n".encode())

        while True:
            # Receive command from the client
            self.command = self.request.recv(4096).strip()

            # Echo the received command
            print(f"Received from {self.client_address}: {self.command.decode()}")
            # Send back a confirmation response
            self.request.sendall('Command received\n!'.encode())

# Allows reuse of address/port immediately
class ThreadedBotServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 4242

    # Allows multiple clients to connect simultaneously with ThreadingTCPServer
    server = socketserver.ThreadingTCPServer((HOST, PORT), BotServer)
    print(f"Bot server running on {HOST}:{PORT}")
    server.serve_forever()
