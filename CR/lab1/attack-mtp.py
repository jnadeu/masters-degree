# Attack Many Time Pad (MTP) Script

import binascii
from collections import Counter

# Provided ciphertexts (hex-encoded)
ciphertexts = [
    "8302a583715c1d413fb67478fead09fc9510cb23e6243096fe6d190ac30ce8e7478059d76744584b249125839e8e8a47aa967743bc1cf2d8b2043a8608001d97ae32b4",
    "8a03e983245b1b0c23b66563f8a91ffc99109f38ae2463d4ee700c0ad01fefa2468e17d46f525c193b9a30838d938e4befd26255ad13fbd8be1674801e540ad6b728bc",
    "881fa091255613423fb66364e4ad16b89f43d63fe6352bd3ab611d59c75efbed4a951bc66a5a191b3e952ec68fc19340eb863258be06b4cfa51268c31e0c11c4b724b7",
    "8708ab903e51524631fb7478aaa509fc840bda6ca42430c2ab73144bca1befa24c8f59c56745520e269636cf91c18f41f9867d42a655fac5f3137f811a001d97ab2cbe",
    "8802a7943e53075839f97f6ae6ec16bd8906cd3fe62031d3ab600a5fd017fcee058716d526464b04319124d0948f8008e39f7357ba06b48ab6117c8a181d1dd9b72daa",
    "9b1fa685235e1f4139f8762be3a25aac8917d723a8612ac5ab62584dc11bfcf6059618de2642564b219b3bd598c18447e7827e55a755e4d8bc157686160758d1a232a7",
    "8802af84345a524d3ef23168f8a313af8302d138b5612ed7e066584b935eede757871cc472161909209136c89b80945caa9d7c10be55e7dfbd1963c3161b0ad9aa2fb4",
    "8e01ac81254d1b4f70f57079f9ec1cb9950f9f3faa2e3496ea6d1c0adf1ffee9059511c226535404269d38cddd8e8108fe807354b601fdc5bd1676c31e1a1fdead24a0",
    "881fa691221f174224e47e7bf3ec16b383109f25b56134dfef661453930beee741c110c92655550a21873ec59482865ce39d7c10b110e1d8b21b3a8d1e000fd8b12aa0",
    "9b01ac83225a524e22ff7f6caaae1bbf9b43c96cb22426d8f8231944d75eeba251961ccb70534a4b269d25c699c1884eaa867a55ac10b4cfbf127997121758d4a233a0",
    "830cbf8771461d5970f4746ee4ec1bbe9c069f38a96127d3e86a0842d60cbde3498d59ca7f16540e218736c49892c740eb9a7358be1df5c2b25773c3131b08d2e332bc"
]

# Convert ciphertexts from hex to bytes
ciphertexts_bytes = [bytes.fromhex(ct) for ct in ciphertexts]

# Determine the length of the ciphertexts, all are the same length
ciphertext_length = len(ciphertexts_bytes[0])

# XOR two byte strings
def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

# Attempt to decrypt ciphertexts by analyzing XOR results
def analyze_ciphertexts(ciphertexts):
    num_ct = len(ciphertexts)
    guessed_plaintexts = [" " * ciphertext_length for _ in range(num_ct)]
    
    # Convert guessed plaintexts to mutable bytearrays
    guessed_plaintexts = [bytearray(pt.encode()) for pt in guessed_plaintexts]
    
    for i in range(num_ct):
        for j in range(i + 1, num_ct):
            xor_result = xor_bytes(ciphertexts[i], ciphertexts[j])
            
            for k, byte in enumerate(xor_result):
                # Check if XORing with ' ' gives a valid lowercase letter or space
                if 0x20 <= (ciphertexts[i][k] ^ 0x20) <= 0x7a:
                    guessed_plaintexts[i][k] = ciphertexts[i][k] ^ 0x20
                if 0x20 <= (ciphertexts[j][k] ^ 0x20) <= 0x7a:
                    guessed_plaintexts[j][k] = ciphertexts[j][k] ^ 0x20

    # Only allow lowercase letters and spaces in the result
    for i in range(num_ct):
        for k in range(ciphertext_length):
            # Convert to lowercase English letters or space, discard invalid ones
            if not (0x61 <= guessed_plaintexts[i][k] <= 0x7a or guessed_plaintexts[i][k] == 0x20):
                guessed_plaintexts[i][k] = 0x20  # Replace with space if invalid

    # Convert bytearrays back to strings
    return [pt.decode("ascii") for pt in guessed_plaintexts]

# Perform the attack
recovered_plaintexts = analyze_ciphertexts(ciphertexts_bytes)

# Output the results
print("\nExtracted Plaintexts:\n")
for i, plaintext in enumerate(recovered_plaintexts):
    print(f"Plaintext {i + 1}: {plaintext}")
