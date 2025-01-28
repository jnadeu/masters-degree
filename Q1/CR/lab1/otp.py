# One Time Pad script

# Function to encrypt a list of plaintexts using the OTP (XOR with the same key)
def encrypt_all(plaintext_list, key):
    ciphertext_list = []
    
    for plaintext in plaintext_list:
        # Perform XOR operation between plaintext and key
        ciphertext = bytes([p ^ k for p, k in zip(plaintext, key[:len(plaintext)])])
        ciphertext_list.append(ciphertext)
    
    return ciphertext_list

# Function to decrypt a list of ciphertexts using the OTP (XOR with the same key)
def decrypt_all(ciphertext_list, key):
    plaintext_list = []
    
    for ciphertext in ciphertext_list:        
        # Perform XOR operation between ciphertext and key to recover the plaintext
        plaintext = bytes([c ^ k for c, k in zip(ciphertext, key[:len(ciphertext)])])
        plaintext_list.append(plaintext.decode())  # Convert bytes back to string
    
    return plaintext_list

# Example usage:
plaintext_list = [
        "knowledge is freedom",
        "life itself is pretty",
        "simplicity is a way",
        "the sky is blue today",
        "coding is rewarding",
        "the world is beautiful",
        "practice make perfect",
        "nature is beautiful",
        "stars shine at night",
        "study is a privilege",
        "never stop dreaming"   
]  # List of plaintext messages

key = bytes.fromhex("bff11b789b01519df3002c4ab16002d0eecdfe60ed8b")

# Encrypt all plaintexts
ciphertext_list = encrypt_all(plaintext_list, key)
print("Encrypted ciphertexts (in hex):\n")
for ciphertext in ciphertext_list:
    print(ciphertext.hex())

# Decrypt all ciphertexts
decrypted_list = decrypt_all(ciphertext_list, key)
print("\nDecrypted plaintexts:\n")
for decrypted in decrypted_list:
    print(decrypted)
