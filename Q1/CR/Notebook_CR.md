**Briefing Document: Cryptography Concepts and Techniques**

**I. Introduction**

This document reviews key concepts in cryptography, drawing from the provided slide excerpts. It covers fundamental definitions, historical ciphers, mathematical foundations, symmetric and asymmetric encryption, message authentication codes, and relevant attack vectors.

**II. Core Principles and Definitions**

- **Cryptography Defined:** The word "cryptography" comes from the Greek words "kryptós" (hidden, secret) and "graphein" (to write). It is a rigorous science that involves specifying a threat model, proposing a construction, and proving that breaking the construction under the threat model will solve a computationally hard problem.
- **Symmetric Ciphers:** These use a single key for both encryption and decryption.
- **Substitution Ciphers:** These replace each letter in the plaintext with a different letter, according to a key. Examples include basic substitution ciphers, where "A B C D E F G H I J K L M" is mapped to "p o i u y t r e w q z x j", and Caesar ciphers, where letters are shifted a fixed number of places in the alphabet.
- **Vigenère Cipher:** A polyalphabetic substitution cipher using a keyword to shift letters. "w o w t h i s l o o k s r e a l l y f u nm" is encrypted with key "MERIT" repeated to give "i s n b a u w c w h w w i m t x p p n n z".
- **Breaking Symmetric Ciphers:** Simple substitution ciphers are broken through frequency analysis. Vigenère can be broken by determining the length of the key through techniques exploiting repeating patterns.
- **Discrete Probability:** Cryptography relies on probability theory.
- **Uniform Distribution:** Each element in a set has an equal probability of being selected: "∀ ∈ 𝑈: Pr[x] = 1 / |𝑈|".
- **Point Distribution:** A distribution where only one element has a probability of 1, and all others have a probability of 0: "P(x0) = 1 ∀ x != x0: P(x) = 0".
- **Random Variables:** Functions that map elements of a set to values. For instance, given U = {0,1}^2 a random variable X(y) = lsb(y), the function would map (00,01) to 0 and (10,11) to 1.
- **Uniform Random Variable:** Denoted by ←U, implies every element has the same probability, which is the same as the identity function r(x) = x.
- **Independence:** Two events A and B are independent if Pr[A ∩ B] = Pr[A] \* Pr[B], or two variables X and Y are independent if ∀𝑎, ∈ 𝑉: Pr[X = 𝑎 ∩ Y = b] = Pr[X = a] \* Pr[Y = b].
- **XOR (⊕):** The bitwise addition modulo 2, often represented as "true if different."

**III. Symmetric Encryption: One-Time Pad & Stream Ciphers**

- **Ciphers Definition:** A cipher is defined by a pair of efficient algorithms, Encryption (E) and Decryption (D), with E: K x M -> C and D: K x C -> M, such that for all messages m and keys k, D(k, E(k,m)) = m.
- **Randomized Encryption:** Some ciphers employ randomness in the encryption algorithm to avoid encrypting the same message to the same ciphertext every time.
- **One-Time Pad (OTP):**
- OTP is a symmetric cipher where the key is a truly random sequence as long as the message.
- Encryption is performed by bitwise XORing the plaintext with the key: c = m ⊕ k.
- Decryption is performed by bitwise XORing the ciphertext with the same key: m = c ⊕ k.
- The OTP achieves **perfect secrecy** (Shannon's definition), meaning a ciphertext reveals no information about the plaintext. The probability of any ciphertext being produced is the same regardless of the plaintext: "∀𝑚0, 𝑚1 ∈ 𝑀, ∀𝑐 ∈ 𝐶: Pr[𝐸(𝑘,𝑚0) = 𝑐] = Pr[𝐸(𝑘,𝑚1) = 𝑐]".
- **Stream Ciphers:**
- Stream ciphers attempt to make OTPs practical by using a Pseudo-Random Generator (PRG) to generate a pseudorandom key from a shorter seed: G: {0,1}^k -> {0,1}^n where n>>k.
- The message is encrypted via c=m ⊕ G(k)
- **Predictability:** A PRG, G is predictable if there exists an algorithm and index such that Pr[A(G(k)\_{1,..,i}) = G(k)\_{i+1}] >= 1/2 + e for some non-negligible e. If it is not predictable, it is considered unpredictable.
- **OTP Weaknesses:**
- Key reuse is critical. Using the same key to encrypt two different messages can reveal information about the messages (Two-Time Pad attack). If m1 ⊕ PRG(k) = c1 and m2 ⊕ PRG(k) = c2, then c1 ⊕ c2 = m1 ⊕ m2,
- OTP is malleable: if you have an encryption c=m⊕k, the encryption of m' = m ⊕ x is c'= c ⊕ x.
- Malleability example: If an attacker has c = Enc(k, "send to bob") then c ⊕ ("bob" ⊕ "boe") = Enc(k, "send to boe")
- **Indistinguishability:** The output of a PRG should be indistinguishable from a truly random string, where the advantage for an adversary A is defined as Adv\_PRG(A, G) = | Pr[A(G(k)) = 1] - Pr[A(r) = 1] | where k ← {0,1}^k and r ← {0,1}^n for a given statistical test A on the strings with length n.
- A secure PRG will have an advantage that is negligible.

**IV. Semantic Security**

- **Semantic Security:** An encryption scheme is semantically secure if the ciphertext reveals no information about the plaintext.
- The formal definition involves a game between a challenger and an adversary, the advantage of the adversary is measured by its ability to guess which message was encrypted. If that advantage is negligible, the cipher is considered semantically secure.
- **Example:** An adversary that can always deduce the least significant bit (LSB) of a plaintext from a ciphertext would mean that the cipher is not semantically secure.
- **OTP Semantic Security:** The OTP, when used correctly, is semantically secure. An adversary A cannot tell if c=m0⊕k or c=m1⊕k because the probability is 0.

**V. Block Ciphers**

- **Block vs Stream Ciphers:** Stream ciphers encrypt bit by bit while block ciphers operate on blocks of bits (e.g. 64 bits, 128 bits).
- **Block Cipher Padding:** Plaintext messages are padded to fit the block size.
- **Examples:3DES:** 64-bit blocks, 168-bit key
- **AES:** 128-bit blocks, 128, 192, or 256-bit keys
- **Key Expansion:** Block ciphers often employ a key expansion algorithm that generates round keys for each round of encryption using a key schedule algorithm.
- **Round Function R:** Block ciphers consist of repeated rounds of operations with a round function R(k, m) in order to obfuscate the input data.
- **Pseudo-Random Functions (PRFs):**A PRF is a function F: K x X -> Y such that there exists an efficient algorithm that can evaluate F(k, x).
- **Secure PRF:** A PRF is secure if it is indistinguishable from a truly random function, Funs[X,Y]
- A random function in Funs[X,Y] should be indistinguishable from a random function in S, a set of functions with a fixed key, k.
- **Feistel Network:**A method for constructing invertible block ciphers from non-invertible functions.
- Divides the input into two halves, applies a function to one half, and XORs it with the other half. The process is repeated over multiple rounds.
- R\_i = F(R\_{i-1}) ⊕ L\_{i-1} , L\_i = R\_{i-1}
- **DES (Data Encryption Standard):** Uses a 16-round Feistel network with a 64-bit block size.
- **AES (Advanced Encryption Standard):** Uses a substitution-permutation network, and has rounds of operations called SubBytes, ShiftRows, MixColumns.
- **Block Cipher Modes of Operation:ECB (Electronic Codebook):** Encrypts each block independently. Identical plaintext blocks result in identical ciphertext blocks.
- **CBC (Cipher Block Chaining):** XORs the plaintext block with the previous ciphertext block before encryption. Requires an initialization vector (IV). c\_i = E(k, m\_i ⊕ c\_{i-1}) where c\_0 = IV.

**VI. Asymmetric (Public-Key) Cryptography**

- **Public-Key Encryption:**Each user has a public key (pk) for encryption and a secret key (sk) for decryption. Keys are mathematically related but it is impossible to derive the secret key given the public key. pk\_A, sk\_A
- Encryption: c = E(pk, m). Decryption m = D(sk, c).
- **Eavesdropping Security:** An attacker that can observe a public key and ciphertext should not be able to learn information about the encrypted plaintext.
- Measured by the adversary's advantage in a game between a challenger and adversary where the attacker tries to identify the encrypted message by a given set of options.
- **Chosen Ciphertext Security (CCA):** Even if an attacker can have access to decryption of chosen ciphertexts, they should not be able to learn information about the plaintext.
- An attacker is allowed to query a decryption oracle (except for a challenge ciphertext).
- **Trapdoor Functions (TDF):**A function that is easy to compute in one direction but hard to invert without a special piece of information, called the trapdoor (private key).
- A trapdoor function is a triple of algorithms (G, F, F^-1)
- G(size) produces a key pair (pk, sk)
- F(pk, x) is deterministic and defines a function X -> Y
- F^-1(sk, y) is deterministic and defines a function Y -> X and computes x if F(pk, x) = y.
- F is a one-way function meaning that it cannot be inverted without the knowledge of the secret key sk.

1. **TDF from Public key encryption:**(G, F, F^-1) a secure TDF X -> Y
2. (E\_s, D\_s) a secure symmetric authenticated encryption defined over (K, M, C)
3. H: X -> K a hash function E(pk, m): x ← X; y ← F(pk, x); k ← H(x); c ← Es(k, m) . Output (y, c) D(sk, (y, c)): x ← F^-1(sk, y); k ← H(x); m ← D\_s(k, c) . Output m.

- **RSA (Rivest-Shamir-Adleman):**Based on the hardness of factoring large numbers.
- Public key: (N, e) where N is a product of two large primes p and q, and e is an integer relatively prime to φ(N).
- Private key: (N, d) where d is the modular multiplicative inverse of e mod φ(N).
- Encryption: c = m^e mod N
- Decryption: m = c^d mod N.
- **RSA and TDF:** G(size) generates large prime numbers p,q such that N=pq and produces (N, e) as public key and (N, d) as secret key, where e \* d = 1 (mod φ(N)). F(pk, x) = x^e mod N and F^-1(sk, y) = y^d mod N.
- The number of invertible elements in Z\_N is φ(N) = (p-1)(q-1).

1. **RSA Public-Key Encryption:**generate RSA parameters pk = (N, e) and sk = (N, d)
2. Randomly generate an integer x < N
3. Compute y = x^e mod N
4. Generate a symmetric key k=H(x)
5. Encrypt the message c = E\_s(k, m) Output (y, c)

- Never use textbook RSA directly; instead, always preprocess the plaintext.
- **PKCS#1:** A set of public key cryptography standards.
- PKCS#1 mode 2 preprocesses messages before encrypting with RSA by adding padding to the message: 02 || random padding || 00 || message
- **Bleichenbacher Attack:** A chosen ciphertext attack that can break PKCS#1. An attacker that has access to a webserver that returns an error if a ciphertext does not have a valid PKCS1 format can recover the secret message by performing multiple queries with crafted messages using malleability properties of RSA.
- The attacker can learn if the most significant 16 bits are 02 in the decrypted plaintext.
- Malleability of RSA: an attacker can choose r and compute c' = r^e \* c (mod N) to obtain a new valid ciphertext based on c.

**VII. Diffie-Hellman Key Exchange**

- **Diffie-Hellman Protocol:** A key exchange protocol allowing two parties to establish a shared secret key over an insecure channel.
- Both parties agree on a large prime p and a generator g.
- Alice computes A = g^a mod p. Bob computes B = g^b mod p.
- Alice sends A to Bob, and Bob sends B to Alice.
- Alice computes s = B^a mod p. Bob computes s = A^b mod p.
- The shared secret is s = g^(ab) mod p
- **Security Against Eavesdropping:** Diffie-Hellman is secure if the discrete logarithm problem is hard. An attacker can observe p, g, g^a mod p and g^b mod p, but without the secret numbers a and b, cannot compute g^(ab) mod p
- **Man-in-the-Middle (MITM) Attack:** An attacker can intercept the key exchange and establish separate keys with both parties. If Eve intercepts g^a and g^b from Alice and Bob and replaces them with g^a' and g^b', then Eve can obtain a shared key with Alice g^(a'a) and with Bob g^(b'b).
- This type of attack requires authentication of the participants in order to prevent.

**VIII. TLS (Transport Layer Security)**

- **TLS 1.2:** A cryptographic protocol used to secure communications over networks.
- **TLS Client Key Exchange:** A key exchange procedure.
- In RSA key exchange, a premaster secret is padded and encrypted with the server's public key.
- The Bleichenbacher attack can be used to attack this.

**IX. Message Integrity**

- **Integrity:** Ensuring data has not been altered in an unauthorized way.
- **Message Authentication Code (MAC):** A cryptographic function that generates a tag based on a message and a secret key.
- MAC is defined as a set of two algorithms, (S, V), where S(k, m) produces a tag, and V(k, m, t) outputs either "yes" or "no", such that V(k, m, S(k,m)) = "yes".
- The key is needed to prevent an attacker to forge a tag.
- **Secure MAC:** A secure MAC is resistant to existential forgery attacks; the adversary should not be able to generate a valid tag for a new message after making queries to the MAC.
- **Existential Forgery:** An attacker should not be able to produce a valid tag for a message without knowing the key.
- **Secure MAC Game:** The advantage of an adversary Adv\_MAC(A, S, V) = Pr[Challenger outputs 1] where:

1. The adversary makes q queries obtaining t\_i ← S(k, m\_i)
2. The adversary outputs a tag t and message m
3. The challenger outputs 1 if V(k, m, t) = "yes" and if m is different from any query m\_i

- **MACs from PRFs:** A MAC can be built from a PRF by setting the tag to be equal to PRF(k, m). However, it's not secure if the PRF output space is too small. For instance a PRF that returns an output of only 5 bits can be easily broken.
- **Hash Functions:** A function H that takes an input of arbitrary length and produces a fixed-length output and is defined over (M, T) with |M| >> |T|.
- Hash functions should be collision-resistant. This means it should be computationally hard to find two messages that produce the same hash output.
- **Merkle-Damgård Paradigm:** A method for building collision-resistant hash functions. It uses a compression function, iterates over blocks of the message, and processes with an IV. It has a vulnerability that makes MACs based on hashing H(k || m) insecure.
- **HMAC (Hash-based Message Authentication Code):** A secure way to create a MAC using a hash function. HMAC(k, m) = H((k ⊕ opad), H((k ⊕ ipad) || m)).

**X. Key Takeaways**

- Cryptography is a rigorous science based on mathematical principles and probability theory.
- Symmetric ciphers, such as OTP and stream ciphers, provide confidentiality but require secure key distribution.
- Block ciphers, such as DES and AES, are essential for practical encryption and come with different modes of operation.
- Asymmetric cryptography uses public and private keys for encryption and digital signatures. RSA is a popular asymmetric cipher.
- Message authentication codes (MACs) ensure data integrity and authentication. HMAC is a popular and secure construction based on hash functions.
- Insecure usage of cryptographic algorithms or protocols can lead to vulnerabilities (Two-time pad, Bleichenbacher attack, etc).

This briefing document provides a foundation for understanding fundamental cryptography concepts. Further exploration is recommended for deeper understanding.


***

# Cryptography Study Guide

## Quiz

1. What is the etymological origin of the word "cryptography," and what does this imply about its fundamental purpose? *Cryptography comes from the Greek words “kryptos,” meaning hidden or secret, and “graphein,” meaning to write. This origin highlights the fundamental goal of cryptography to conceal information through writing and other methods.*
2. In the context of cryptography, what are the three key steps in the rigorous scientific process? *The three key steps in cryptography are specifying the threat model, proposing a construction, and proving that breaking the construction under the threat model will solve a computationally hard problem.*
3. Describe how a substitution cipher operates and provide an example of how a message is encrypted. *A substitution cipher replaces each letter in the plaintext with a corresponding letter from a different alphabet. For example, "hola" could become "egxp" if 'h' is substituted with 'e,' 'o' with 'g,' 'l' with 'x,' and 'a' with 'p'.*
4. Explain the main difference between a Caesar cipher and a Vigenère cipher. *A Caesar cipher is a simple substitution cipher where each letter is shifted by a fixed number of positions in the alphabet, while a Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to shift the letters by different amounts based on the keyword letters.*
5. What is a "uniform distribution" in probability, and what is an example with a set of four elements? *A uniform distribution in probability means that every element in a set has an equal probability of being chosen. For example, in a set like {00, 01, 10, 11}, each has a probability of 1/4.*
6. Define a "random variable" in the context of discrete probability. *A random variable is a function that maps outcomes of a random phenomenon to numerical values. For example, if outcomes are binary strings, a random variable can map a string to its last bit (lsb).*
7. What does it mean for two events to be considered "independent" in probability? *Two events are independent if the occurrence of one does not affect the probability of the other. In terms of their probabilities, this means the joint probability of both events occurring is the product of each individual event's probability.*
8. Explain the concept of the One-Time Pad and how it achieves perfect secrecy. *The One-Time Pad (OTP) is an encryption method where a plaintext is XORed with a random key that is as long as the message, and the key is only used once. This provides perfect secrecy because the ciphertext reveals no information about the plaintext without the key.*
9. What does "malleability" mean in the context of cryptography, and how does it relate to the One-Time Pad? *Malleability means that a ciphertext can be altered in a way that will predictably change the decrypted message without the attacker knowing the key. The OTP is highly malleable. For example, by flipping a bit in the ciphertext, you will predictably flip the corresponding bit in the message.*
10. What is the core concept of semantic security, and provide a simple example of a system that is not semantically secure? *Semantic security means that a ciphertext reveals no useful information about the message, beyond the message's length. For instance, a system that always reveals the least significant bit of the plaintext would not be semantically secure.*

## Answer Key

1. *Cryptography comes from the Greek words “kryptos,” meaning hidden or secret, and “graphein,” meaning to write. This origin highlights the fundamental goal of cryptography to conceal information through writing and other methods.*
2. *The three key steps in cryptography are specifying the threat model, proposing a construction, and proving that breaking the construction under the threat model will solve a computationally hard problem.*
3. *A substitution cipher replaces each letter in the plaintext with a corresponding letter from a different alphabet. For example, "hola" could become "egxp" if 'h' is substituted with 'e,' 'o' with 'g,' 'l' with 'x,' and 'a' with 'p'.*
4. *A Caesar cipher is a simple substitution cipher where each letter is shifted by a fixed number of positions in the alphabet, while a Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to shift the letters by different amounts based on the keyword letters.*
5. *A uniform distribution in probability means that every element in a set has an equal probability of being chosen. For example, in a set like {00, 01, 10, 11}, each has a probability of 1/4.*
6. *A random variable is a function that maps outcomes of a random phenomenon to numerical values. For example, if outcomes are binary strings, a random variable can map a string to its last bit (lsb).*
7. *Two events are independent if the occurrence of one does not affect the probability of the other. In terms of their probabilities, this means the joint probability of both events occurring is the product of each individual event's probability.*
8. *The One-Time Pad (OTP) is an encryption method where a plaintext is XORed with a random key that is as long as the message, and the key is only used once. This provides perfect secrecy because the ciphertext reveals no information about the plaintext without the key.*
9. *Malleability means that a ciphertext can be altered in a way that will predictably change the decrypted message without the attacker knowing the key. The OTP is highly malleable. For example, by flipping a bit in the ciphertext, you will predictably flip the corresponding bit in the message.*
10. *Semantic security means that a ciphertext reveals no useful information about the message, beyond the message's length. For instance, a system that always reveals the least significant bit of the plaintext would not be semantically secure.*

## Essay Questions

1. Compare and contrast the historical cryptographic methods (substitution, Caesar, Vigenère) with modern techniques such as stream ciphers and block ciphers. How have advancements in computational power influenced the evolution of these methods?
2. Discuss the concept of a Pseudo-Random Generator (PRG) and its importance in modern cryptography. Explain the significance of a PRG being unpredictable and the limitations of stream ciphers in achieving perfect secrecy using PRGs.
3. Analyze the security definitions of perfect secrecy and semantic security in cryptography, and explain why perfect secrecy is difficult to achieve in practice. Discuss how semantic security provides a more practical approach to defining security in modern encryption schemes.
4. Explain the concept of a Trapdoor Function and its role in public key cryptography. Then, describe the RSA algorithm, including its key generation process and the mathematical principles that make it a secure trapdoor permutation.
5. Discuss the vulnerabilities of the basic Diffie-Hellman key exchange protocol, specifically the Man-in-the-Middle (MITM) attack. Explain how the MITM is able to break the security of the basic DH method.

## Glossary

- **Cipher:** An algorithm for performing encryption or decryption.
- **Symmetric Cipher:** An encryption method that uses the same key for encryption and decryption.
- **Substitution Cipher:** A method of encryption by which units of plaintext are substituted with ciphertext.
- **Caesar Cipher:** A type of substitution cipher where each letter in the plaintext is shifted a fixed number of places down the alphabet.
- **Vigenère Cipher:** A method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.
- **Plaintext:** The original, unencrypted message.
- **Ciphertext:** The encrypted message.
- **Key:** Secret information used in cryptography to encrypt or decrypt messages.
- **Threat Model:** A description of what an adversary may be capable of doing.
- **Uniform Distribution:** A probability distribution where all outcomes are equally likely.
- **Point Distribution:** A probability distribution where only one outcome has a probability of 1 and all others have a probability of 0.
- **Random Variable:** A function that maps outcomes of a random process to numerical values.
- **Independent Events:** Two or more events are independent if the occurrence of one does not affect the occurrence of the other(s).
- **XOR (Exclusive OR):** A logical operation that outputs true only when inputs differ.
- **One-Time Pad (OTP):** An encryption method that uses a random key that is as long as the message and only used once.
- **Perfect Secrecy:** An encryption method with a ciphertext that provides no information about the plaintext (i.e., it provides the same distribution of ciphertext regardless of the plaintext).
- **Pseudo-Random Generator (PRG):** An algorithm that creates a sequence of bits that appears random.
- **Predictability:** The measure of how easily a sequence of bits can be predicted.
- **Malleability:** The property of a cryptographic scheme such that it is possible to alter a ciphertext to make predictable alterations in the decrypted plaintext.
- **Semantic Security:** The property of a cryptographic scheme such that the ciphertext reveals no information about the plaintext other than its length.
- **Block Cipher:** An encryption method that operates on fixed-size blocks of plaintext.
- **Padding:** The addition of bits to a plaintext message to ensure it meets the size requirements of block ciphers.
- **Round Keys:** Subkeys derived from the main key that are used in different rounds of a block cipher.
- **Pseudo-Random Function (PRF):** A function that takes a key and an input, and produces an output that is indistinguishable from a truly random value.
- **Feistel Network:** A general method of transforming any function into a permutation. It is widely used for block cipher construction.
- **DES (Data Encryption Standard):** An older block cipher, now considered insecure, which uses a Feistel network.
- **AES (Advanced Encryption Standard):** A symmetric block cipher used for encrypting digital data.
- **ECB (Electronic Codebook):** A mode of operation for block ciphers, where each block of plaintext is encrypted independently with the same key.
- **CBC (Cipher Block Chaining):** A mode of operation for block ciphers where each plaintext block is XORed with the previous ciphertext block before encryption.
- **Public Key Encryption:** A method of encryption that uses separate keys for encryption and decryption, where the encryption key is public and the decryption key is private.
- **Eavesdropping Security:** The security property of an encryption scheme in which an attacker cannot learn any information from the ciphertext when the key is unknown.
- **IND-CCA (Indistinguishability under Chosen Ciphertext Attack):** A security standard that measures an encryption method's resistance to chosen ciphertext attacks.
- **Trapdoor Function (TDF):** A function that is easy to compute in one direction, but difficult to reverse without knowing the trapdoor information.
- **RSA:** A public-key cryptosystem widely used for secure data transmission.
- **PKCS1:** A set of standards for public key cryptography, often used with RSA encryption.
- **Bleichenbacher Attack:** A type of chosen ciphertext attack that can be used against implementations of PKCS #1 v1.5.
- **Diffie-Hellman (DH):** A method for establishing a shared secret key over a public channel.
- **MITM (Man-in-the-Middle):** An attack where an attacker intercepts and relays messages between two parties.
- **TLS (Transport Layer Security):** A protocol used to provide secure communications over a computer network.
- **MAC (Message Authentication Code):** A cryptographic code used to verify the integrity and authenticity of a message.
- **Collision Resistance:** The property of a cryptographic hash function that makes it difficult to find two different inputs that produce the same output.
- **Merkle-Damgård:** A technique for constructing cryptographic hash functions by sequentially processing fixed-size blocks of the input.
- **HMAC (Hash-based Message Authentication Code):** A specific type of MAC derived from a hash function.