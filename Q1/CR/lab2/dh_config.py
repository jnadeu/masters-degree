import os
import shutil
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Set the directory where the shared files will be stored
SHARED_DIR = os.path.join(os.getcwd(), "shared")

def clean_files_directory():
    """Clean up all files in the SHARED_DIR."""
    if os.path.exists(SHARED_DIR):
        shutil.rmtree(SHARED_DIR)
    os.makedirs(SHARED_DIR)

def generate_and_save_dh_parameters(filename):
    """Generate DH parameters and save to a file."""
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    
    # Ensure the SHARED_DIR exists
    if not os.path.exists(SHARED_DIR):
        os.makedirs(SHARED_DIR)
    
    # Save the parameters to a file
    with open(filename, "wb") as f:
        f.write(parameters.parameter_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.ParameterFormat.PKCS3
        ))
    print(f"DH parameters saved to {filename}")
    print(f"DH Parameters (p): {parameters.parameter_numbers().p}")
    print(f"DH Parameters (g): {parameters.parameter_numbers().g}")


if __name__ == "__main__":
    # Clean up shared dir
    clean_files_directory()

    # Specify the file path for saving DH parameters
    param_file = os.path.join(SHARED_DIR, "dh_parameters.pem")
    
    # Generate and save the DH parameters
    generate_and_save_dh_parameters(param_file)






def run_eve():
    """Simulate Eve's behavior as MITM."""
    # Generate two key pairs for Eve (one for each shared key)
    private_key_alice, public_key_alice = generate_dh_keys()
    private_key_bob, public_key_bob = generate_dh_keys()

    while not os.path.exists(os.path.join(SHARED_DIR, "alice_to_bob.pub")):
        time.sleep(1)

    # Eve intercepts Alice's public key and sends her own fake public key to Bob
    alice_public_bytes = read_file("alice_to_bob.pub")
    write_file("bob_to_alice.pub", public_key_bob.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print("Eve: Intercepted Alice's public key and sent Bob's fake key.")

    # Compute shared keys: one with Alice and another with Bob
    shared_key_with_alice = compute_shared_key(private_key_alice, alice_public_bytes)

    while not os.path.exists(os.path.join(SHARED_DIR, "message.enc")):
        time.sleep(1)

    # Eve intercepts the message from Alice to Bob
    encrypted_message = read_file("message.enc")
    print(f"Eve: Intercepted Alice's message.")
    
    try:
        # Decrypt the message sent by Alice using Eve's shared key with Alice
        message = decrypt_message(shared_key_with_alice, encrypted_message)
        print(f"Eve: Intercepted Alice's message: {message}")
    except ValueError as e:
        print(f"Error decrypting message: {e}")

    # Eve can modify the message if needed (for example, change the message)
    modified_message = message.replace("Hello", "Hi")

    # Re-encrypt the modified message to send to Bob
    encrypted_modified_message = encrypt_message(shared_key_with_alice, modified_message)
    write_file("message.enc", encrypted_modified_message)
    print(f"Eve: Modified message sent to Bob.")

    while not os.path.exists(os.path.join(SHARED_DIR, "response.enc")):
        time.sleep(1)

    # Eve intercepts Bob's response (sent back to Alice)
    encrypted_response = read_file("response.enc")
    print(f"Eve: Intercepted Bob's response.")

    # Eve decrypts Bob's response using the shared key with Bob
    shared_key_with_bob = compute_shared_key(private_key_bob, read_file("bob_to_alice.pub"))
    try:
        response = decrypt_message(shared_key_with_bob, encrypted_response)
        print(f"Eve: Intercepted Bob's response: {response}")
    except ValueError as e:
        print(f"Error decrypting response: {e}")

    # Eve can modify the response as well
    modified_response = response.replace("Message received, Alice!", "Message altered by Eve!")
    
    # Re-encrypt the modified response and send it to Alice
    encrypted_modified_response = encrypt_message(shared_key_with_bob, modified_response)
    write_file("response.enc", encrypted_modified_response)
    print(f"Eve: Modified response sent to Alice.")
