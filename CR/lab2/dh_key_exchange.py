import os
import sys
import time
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Set the directory where the shared files are stored
SHARED_DIR = os.path.join(os.getcwd(), "shared")

def load_dh_parameters(filename):
    """Load DH parameters from a file."""
    with open(filename, "rb") as f:
        parameters = serialization.load_pem_parameters(f.read())
    return parameters
try:
    # Load the DH parameters from the file
    DH_PARAMETERS = load_dh_parameters(os.path.join(SHARED_DIR, "dh_parameters.pem"))
except:
    print("Not found dh_parameters.pem. To fix it, execute: python dh_config.py")
    sys.exit(1)

def generate_dh_keys():
    """Generate DH private and public keys."""
    private_key = DH_PARAMETERS.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def compute_shared_key(private_key, peer_public_bytes):
    """Compute the shared secret from private key and peer's public key."""
    peer_public_key = serialization.load_pem_public_key(peer_public_bytes)
    shared_key = private_key.exchange(peer_public_key)
    return HKDF(algorithm=SHA256(), length=32, salt=None, info=b"dh_shared_key").derive(shared_key)

def encrypt_message(shared_key, plaintext):
    """Encrypt a plaintext message using AES."""
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(shared_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def decrypt_message(shared_key, ciphertext):
    """Decrypt a ciphertext message using AES."""
    iv = ciphertext[:16]
    cipher = Cipher(algorithms.AES(shared_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()
    padded_data = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext.decode()

def write_file(filename, data):
    """Write data to a file."""
    with open(os.path.join(SHARED_DIR, filename), "wb") as f:
        f.write(data)

def read_file(filename):
    """Read data from a file."""
    with open(os.path.join(SHARED_DIR, filename), "rb") as f:
        return f.read()

def send_encrypted_message(shared_key, message, filename):
    """Encrypt a message and write it to a file."""
    encrypted_message = encrypt_message(shared_key, message)
    write_file(filename, encrypted_message)
    #print(f"Encrypted message sent: {message}")

def receive_encrypted_message(shared_key, filename):
    """Read and decrypt a message from a file."""
    encrypted_message = read_file(filename)
    decrypted_message = decrypt_message(shared_key, encrypted_message)
    #print(f"Decrypted message received: {decrypted_message}")
    return decrypted_message

def save_shared_key(role, shared_key):
    """Save the computed shared key to a file."""
    shared_key_file = os.path.join(SHARED_DIR, f"{role}_shared_key.bin")
    write_file(shared_key_file, shared_key)

def compare_shared_keys():
    """Compare shared keys between Alice and Bob to detect MITM."""
    alice_shared_key = read_file("alice_shared_key.bin")
    bob_shared_key = read_file("bob_shared_key.bin")

    if alice_shared_key != bob_shared_key:
        print("MITM Detected: Shared keys do not match!")
        return True
    return False

def delete_all_files_in_shared():
    """Delete all files in shared directory (simulate blocking communication)."""
    for filename in os.listdir(SHARED_DIR):
        file_path = os.path.join(SHARED_DIR, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

##########################################################################
##############################|    ROLES   |##############################
##########################################################################

def run_alice():
    """Simulate Alice's behavior."""
    private_key, public_key = generate_dh_keys()
    write_file("alice_to_bob.pub", public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print("Alice: Public key sent.")

    while not os.path.exists(os.path.join(SHARED_DIR, "bob_to_alice.pub")):
        time.sleep(1)

    bob_public_bytes = read_file("bob_to_alice.pub")
    shared_key = compute_shared_key(private_key, bob_public_bytes)
    print("Alice: Shared key established.")

    # Save Alice's shared key
    save_shared_key("alice", shared_key)

    message = "Hello Bob, this is Alice!"
    send_encrypted_message(shared_key, message,"message.enc")

    #encrypted_message = encrypt_message(shared_key, message)
    #write_file("message.enc", encrypted_message)
    print(f"Alice: Encrypted message sent: {message}")

    while not os.path.exists(os.path.join(SHARED_DIR, "response.enc")):
        time.sleep(1)

    response = receive_encrypted_message(shared_key, "response.enc")
    #encrypted_response = read_file("response.enc")
    #response = decrypt_message(shared_key, encrypted_response)
    print(f"Alice: Received response: {response}")

def run_bob():
    """Simulate Bob's behavior."""
    private_key, public_key = generate_dh_keys()

    while not os.path.exists(os.path.join(SHARED_DIR, "alice_to_bob.pub")):
        time.sleep(1)

    alice_public_bytes = read_file("alice_to_bob.pub")
    write_file("bob_to_alice.pub", public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print("Bob: Public key sent.")

    shared_key = compute_shared_key(private_key, alice_public_bytes)
    print("Bob: Shared key established.")

    # Save Bob's shared key
    save_shared_key("bob", shared_key)

    while not os.path.exists(os.path.join(SHARED_DIR, "message.enc")):
        time.sleep(1)

    message = receive_encrypted_message(shared_key, "message.enc")

    #encrypted_message = read_file("message.enc")
    #message = decrypt_message(shared_key, encrypted_message)
    print(f"Bob: Received message: {message}")

    response = "Message received, Alice!"
    send_encrypted_message(shared_key, response, "response.enc")
    
    #encrypted_response = encrypt_message(shared_key, response)
    #write_file("response.enc", encrypted_response)
    print(f"Bob: Encrypted response sent: {response}")

def run_eve():
    """Simulate Eve's behavior as MITM."""

    # Eve generates her own key pairs (one for Alice and one for Bob)
    private_key_alice, public_key_alice = generate_dh_keys()
    private_key_bob, public_key_bob = generate_dh_keys()

    # Wait for Alice's public key
    while not os.path.exists(os.path.join(SHARED_DIR, "alice_to_bob.pub")):
        time.sleep(1)
    
    # Wait for Bob's public key
    while not os.path.exists(os.path.join(SHARED_DIR, "bob_to_alice.pub")):
        time.sleep(1)

    # Eve intercepts Alice's public key and sends Bob her own public key
    alice_public_bytes = read_file("alice_to_bob.pub")
    write_file("bob_to_alice.pub", public_key_bob.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print("Eve: Intercepted Alice's public key and sent Bob her fake key.")

    # Eve computes the shared key with Alice
    shared_key_with_alice = compute_shared_key(private_key_alice, alice_public_bytes)
    # Save Eve's shared key generate for Alice
    save_shared_key("alice", shared_key_with_alice)
    print("Eve: Shared key with Alice computed.")

    # Eve intercepts Bob's public key and sends Alice her own public key
    bob_public_bytes = read_file("bob_to_alice.pub")
    write_file("alice_to_bob.pub", public_key_alice.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print("Eve: Intercepted Bob's public key and sent Alice her fake key.")

    # Eve computes the shared key with Bob
    shared_key_with_bob = compute_shared_key(private_key_bob, bob_public_bytes)
    # Save Eve's shared key generate for Bob
    save_shared_key("bob", shared_key_with_bob)
    print("Eve: Shared key with Bob computed.")

    time.sleep(1)

    print("Eve: Impersonate Alice's message.")
    message = "Hi Bob, this is Alice! ^_^"
    send_encrypted_message(shared_key_with_bob, message, "message.enc")

    encrypted_message = read_file("message.enc")

    # Decrypt the message sent by Alice
    modified_message = decrypt_message(shared_key_with_bob, encrypted_message)
    print(f"Eve: Message from Alice: {modified_message}")
    time.sleep(1)
    print("Eve: Modified message forwarded to Bob.")


    time.sleep(1)

    print("Eve: Impersonate Bob's message.")
    response = "Message received, Alice! ^_^"
    send_encrypted_message(shared_key_with_alice, response, "response.enc")
    
    encrypted_response = read_file("response.enc")

    # Decrypt the response from Bob
    modified_response = decrypt_message(shared_key_with_alice, encrypted_response)
    print(f"Eve: Message from Bob: {response}")

    # Encrypt the modified response and forward it to Alice
    encrypted_modified_response = encrypt_message(shared_key_with_alice, modified_response)
    write_file("response.enc", encrypted_modified_response)
    time.sleep(1)
    print("Eve: Modified response forwarded to Alice.")

def run_angel():
    """Simulate Angel's behavior (monitoring for MITM)."""
    print("Angel: Monitoring communication...")

    # Wait for both Alice's and Bob's shared keys to be saved
    while not (os.path.exists(os.path.join(SHARED_DIR, "alice_shared_key.bin")) and os.path.exists(os.path.join(SHARED_DIR, "bob_shared_key.bin"))):
        time.sleep(1)

    # Read the shared keys for Alice and Bob
    alice_shared_key = read_file("alice_shared_key.bin")
    bob_shared_key = read_file("bob_shared_key.bin")

    # Compare the shared keys to detect MITM
    if alice_shared_key != bob_shared_key:
        print("Angel: MITM detected! Shared keys do not match!")
        
        # Block communication by deleting all files in the shared directory
        delete_all_files_in_shared()
        print("Angel: All files deleted. Communication blocked.")
    else:
        print("Angel: Shared keys match. No MITM detected.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [alice|bob|eve]")
        sys.exit(1)

    role = sys.argv[1]
    if role == "alice":
        run_alice()
    elif role == "bob":
        run_bob()
    elif role == "eve":
        run_eve()
    elif role == "angel":
        run_angel()
    else:
        print("Invalid role. Use 'alice', 'bob', 'eve' or 'angel'.")
