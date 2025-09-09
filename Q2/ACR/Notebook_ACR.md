**Briefing Document: Cryptography and Security Concepts**

**I. Overview**

This document provides a consolidated overview of cryptographic concepts, including asymmetric cryptography, digital signatures, post-quantum cryptography considerations, and zero-knowledge proofs. It draws from several sources to define key terms, algorithms, and security considerations in modern cryptography.

**II. Asymmetric Cryptography**

- **Core Principle:** Asymmetric cryptography relies on the difficulty of inverting a function without knowing a secret. "it is easy to compute f (x) = y for all x ∈ X it is hard to compute f −1(y) = x for all y ∈ Y there exist a function g such that g(y , sk) = f −1(y) = x is easy to compute, if the secret data sk are known." This allows for public keys to be shared widely, while private keys remain secure.
- **Key Components:** Asymmetric cryptosystems consist of Setup, KeyGen, Enc, and Dec algorithms. "An asymmetric cryptosystem is a tuple of algorithms (Setup,KeyGen,Enc,Dec) such that Setup generates the public parameter pp. KeyGen(pp) generates a private-public key pair (sk, pk). Enc(m, pk) encrypts a message. The ciphertext is ct. Dec(ct, sk) decrypts a ciphertext. We want that Dec((Enc(m, pk), sk) = m."
- **Security Notions:** IND-CPA (Indistinguishability under Chosen Plaintext Attack) and IND-CCA (Indistinguishability under Chosen Ciphertext Attack) are crucial security definitions. The document distinguishes between IND-CCA1 (a weaker form) and IND-CCA2 (adaptive). "We say that (Enc,Dec) is indistinguishable under chosen plaintext attacks if and only if Advind−cpa Enc,A is negligible for every probabilistic polynomial time adversary A."
- *It is important to note the definitions of Expind-cpa Enc,A (λ) and Expind-cca Enc,A (λ) as these are the experiments against which an encryption scheme are judged CPA and CCA secure respectively.*
- **RSA:**
- Based on the hardness of factoring large numbers. "Based on the hardness of the factorization: given n = pq, it is hard to find p, q."
- Key Generation: Involves selecting two large primes, p and q, calculating n=pq, choosing a public exponent e coprime with φ(n), and computing d, the modular multiplicative inverse of e modulo lcm(p-1, q-1). The public key is (n, e), and the private key is d.
- Encryption: ct = me mod n
- Decryption: m = ctd mod n
- **Vulnerability:** Standard RSA is not IND-CPA secure because it is deterministic. "The reason since RSA is not IND-CPA is that it is deterministic: given one public key (n, e) the encryption of m is always the same."
- **ElGamal:**
- Based on the Discrete Logarithm Problem. "Based on the hardness of the discrete logarithm."
- Key Generation: Involves selecting a random integer x and computing h = gx. The public key is h, and the private key is x.
- Encryption: Requires picking a random integer r, computing ct1 = gr and ct2 = mhr. The ciphertext is (ct1, ct2).
- Decryption: Computes s = ctx1 and then m = ct2/s.
- **Security:** ElGamal can be IND-CPA secure if the Decisional Diffie-Hellman (DDH) assumption holds in the group used. "If the DDH assumption holds in the group G, then the ElGamal cryptosystem is IND-CPA secure."

**III. Digital Signatures**

- **Core Function:** Provides integrity, authenticity, and non-repudiation for electronic documents. "A signature scheme is a method of signing a message stored in electronic form."
- **Key Requirements:**
- Binding the signature to the message.
- A publicly verifiable verification algorithm.
- **Security Goals:**
- Infeasibility for others to forge signatures. "Given a message m, it should be computationally infeasible for others than the signer to compute a signature σ such that Ver(m, σ) = ⊤."
- Inability for attackers to derive the private key from the public key and signed messages. "Given pk, an attacker cannot feasibly determine sk, nor can she determine any other private key that produces the same signatures as pk."
- **ElGamal Signature Scheme:**
- KeyGen: let p prime, Z∗ p = ⟨g⟩. Random sk with 1 < sk < p − 2 . Compute pk = gsk. The triple (pk, g , p) is public.
- Sign: let m be the message and let 1 < k < p− 1 random such that gcd(k , p − 1) = 1. Compute r = gk . Compute1 σ = (m− sk · r) · k−1 mod p − 1. The signature is (r , σ). \*Ver: the signature is valid if r , σ ∈ Zq, r , σ ∈ Zp, gm = pkr · rσ.
- **Vulnerability:** Susceptible to existential forgery.
- It is important to keep the random value k secret as knowledge of this value will break the entire system.
- **DSA (Digital Signature Algorithm):**
- A NIST standard, derived from ElGamal.
- Signs the *hash* of the message, improving efficiency and security. "Does not sign the message directly, but the hash. More efficient. Ensures the integrity of the entire message. Prevents Existential Forgery."
- Prevents existential forgery.
- **ECDSA (Elliptic Curve Digital Signature Algorithm):**
- A variant of DSA using elliptic curves.
- Offers shorter keys compared to DSA (e.g., 256 bits vs. 2048 bits). "Much shorter keys: 256 bits vs 2048 bits."
- For both DSA and ECDSA the random parameter k is crucial for security, and it must be both unique and secret.
- The random parameter *k* is crucial for security and must be unique and secret. "For both DSA and ECDSA the random parameter k is crucial for security, and it must be both unique and secret. Reuse or even partial information about k leads to the complete breakdown of the signature." This vulnerability has been exploited in practice.
- **EdDSA (Edwards-curve Digital Signature Algorithm):**
- Aims to prevent vulnerabilities present in ECDSA. "Variant of ECDSA aimed at preventing vulnerabilities."
- Based on Schnorr's signature scheme.
- Uses a deterministic approach to generate the secret parameter *k* using a pseudorandom function. "The secret parameter k is not random but deterministic: A pseudorandom function is used starting with the private key and the message. Ensures different values for each message."
- Uses Twisted Edwards curves for efficiency and enhanced resistance to side-channel attacks. "Uses Twisted Edwards curves: Very efficient. Increased security against side channel attacks."

**IV. Post-Quantum Cryptography**

- **Focus:** Developing cryptographic systems resistant to attacks from quantum computers.
- **Approaches:**Isogeny-Based Cryptography (SQISign)
- Multivariate Cryptography (MAYO)
- Lattice-Based Cryptography (Falcon, Dilithium)
- Symmetric Cryptography (Sphincs, FAEST)
- MPC in the Head (SDitH)

**V. Coding Theory**

- **Core concept** Codes are usually represented through a generator matrix, a full-rank matrix G where the rows form a basis for C over Fq.
- **Purpose:** Used to send data through a noisy channel. "Codes are used to send data through a noisy channel."
- Encoding: c = mG
- Checking: 0 = Hc⊤, where H is the parity check matrix of C and c is the received message.
- Errors: Hc⊤ = H(c ′ + e)⊤ = 0 + He⊤ = s.
- Distance Decoding: finding the codeword closest to the received one.
- Syndrome Decoding: listing all possible error vector e and compute their syndrome, then checking which error correspond to the given syndrome. If multiple error are found, choose the one with the lowest weight.
- **Linear Code Equivalence Problem:** Determining whether two linear codes are linearly equivalent. "Determine whether the two codes are linearly equivalent or not with respect to w , i.e. if there exists an linear invertible map ϕ : C → C ′ such that for all codewords c ∈ C w(c) = w(ϕ(c))" This is related to cryptographic group actions.

**VI. Group Actions**

*Definition* Let X be set, and G a group. A (left) group action is a function ⋆ : G × X → X such that e ⋆ x = x for all x ∈ X and g1 ⋆ (g2 ⋆ x) = (g1g2) ⋆ x for all x ∈ X , g1, g2 ∈ G .

- **Cryptographic Group Actions:** Group actions that are efficiently evaluable but hard to invert. "A group action said to be cryptographic if it satisfy additional properties: Efficiently evaluation; One way : hard to invert."
- **Examples** Isogenies between supersingular elliptic curves (CSIDH and Csi-fish), Code Equivalence (LESS and MEDS), Trilinear form based, Lattice based (Falafl).

**VII. Multi-Party Computation (MPC) in the Head**

- **Technique:** A technique for building signatures based on the principles of multi-party computation. "Multi-Party Computation in the Head is a “techniques” for build signature, rather than a family of assumptions or mathematical objects. The idea is based on multi-party computation..."

**VIII. Threshold Protocols**

- **Function:** Distribute a "privilege" (e.g., signing key) among a group of participants. "Threshold Protocols are methods for distributing a "privilege" among a group of participants."
- **Secret Sharing:** Required to distribute the secret among participants. "They require a secret sharing. Informally speaking, a (t, n)–secret sharing scheme allows one dealer to share a secret among n participants in a way such that every set of at least t participants is able to recover the secret, while any other smaller set does not get any information about the secret."
- **Additive Secret Sharing**Let s be the secret. The dealer picks randomly x2, ..., xn and sets x1 = s − x2 − ...− xn.
- **Shamir Secret Sharing** Lets be the secret. The dealer Picks a random polynomial p(x) of degree t − 1 in Fq[x ], such that p(0) = s. Sends p(i) to party P1 for every i ∈ [1, n].

**IX. Perfect Ciphers and Vernam's Cipher**

\*Definition A cipher is called perfect if there is no leakage of information on the plaintext, given one ciphertext, i.e. ∀m ∈ P, ∀c ∈ C P(m|c) = P(m).

- **Shannon's Theorem:** Provides conditions for a cipher to be perfect. Namely, the keys are equidistributed and the set of encryption functions is a regular set of permutations.

*Vernam's cipher (also called one-time pad):*

- Definition Consider P = K = C = (F2)n for n ∈ N, n ≥ 2. Let m, k, c be strings. Define e(m, k) = m ⊕ k, d(c, k) = c ⊕ k.
- The key must be used only once and that is why it is called One-Time Pad.

**X. Zero Knowledge Proofs**

- **Properties:** Completeness, soundness, and zero knowledge.
- **Use case:** Can be used to create digital signatures. "Let us consider the relation (x ,w) ∈ R if and only if (x ,w) is a valid key pair and then perform a Zero Knowledge Proof for the statement x = pk with witness w = sk."
- **Schnorr Signature:** Based on the hardness of the discrete logarithm problem.

**XI. Groups and Fields (Preliminaries)**

- **Group:** A set with an associative operation, a neutral element, and inverses for every element. Examples include (Z, +).
- **Field:** A set with two operations (addition and multiplication) satisfying certain properties, including being abelian groups under both operations (excluding 0 for multiplication) and distributivity. The Bit Field F2 is a key example.

**XII. Importance of Randomness**

- Several cryptographic schemes rely heavily on randomness for security (e.g. the random value k in the ElGamal signature scheme, DSA and ECDSA). If this randomness is compromised it can lead to a total breakdown of the system.

**XIII. Conclusion**

The sources highlight a range of cryptographic techniques, from classical asymmetric encryption like RSA and ElGamal to more modern post-quantum cryptography and advanced signature schemes like EdDSA. A recurring theme is the importance of mathematical assumptions (e.g., the hardness of factoring, the discrete logarithm problem, DDH), and the need to choose cryptographic parameters and algorithms carefully to resist various attacks.


***

## Cryptography and Post-Quantum Security Study Guide

### Quiz

**Answer each question in 2-3 sentences.**

1. What are the three properties that define a group?
2. Explain the Discrete Logarithm Problem and why it is important in cryptography.
3. What is the difference between IND-CPA and IND-CCA security?
4. Describe how RSA encryption works, including key generation, encryption, and decryption.
5. Explain why RSA is not IND-CPA secure.
6. What is a digital signature and what properties should it provide?
7. Explain how the ElGamal signature scheme works.
8. What is a code's generator matrix and parity check matrix?
9. What is the Vernam cipher and why is it considered a perfect cipher when used correctly?
10. How does EdDSA prevent vulnerabilities found in other digital signature algorithms like ECDSA?

### Quiz Answer Key

1. A group (G, +, e) requires a set G, an associative operation +, and a neutral element e such that a + e = e + a = a for all a in G. Additionally, for every element a in G, there exists an element b in G such that a + b = e.
2. The Discrete Logarithm Problem states that given a cyclic group G with generator g, and an element h in G, it is computationally hard to find an integer x such that gx = h. Its importance lies in its use as the foundation for the security of various cryptographic protocols, such as ElGamal.
3. IND-CPA (Indistinguishability under Chosen Plaintext Attack) ensures that an adversary cannot distinguish between the encryptions of two chosen plaintexts. IND-CCA (Indistinguishability under Chosen Ciphertext Attack) strengthens this by also allowing the adversary to request decryptions of ciphertexts, except for the challenge ciphertext.
4. In RSA, key generation involves choosing two large prime numbers, p and q, calculating n = pq and φ(n) = (p-1)(q-1), selecting a public exponent e coprime to φ(n), and computing the private exponent d such that ed ≡ 1 mod φ(n). Encryption involves computing c = me mod n, where m is the message, and decryption involves computing m = cd mod n.
5. RSA is not IND-CPA secure because it is deterministic; the same message encrypted with the same public key will always produce the same ciphertext, which enables attacks where the adversary can encrypt known messages and compare them to the challenge ciphertext.
6. A digital signature is a cryptographic mechanism used to verify the authenticity and integrity of digital documents. It should provide integrity (ensuring the message hasn't been altered), authentication (verifying the signer's identity), and non-repudiation (preventing the signer from denying their signature).
7. In the ElGamal signature scheme, the signer generates a random integer k, computes r = gk, and then calculates σ = (m - sk \* r) \* k-1 mod (p-1), where m is the message, sk is the private key, and p is a prime. The signature (r, σ) is verified by checking if gm = pkr \* rσ mod p.
8. A generator matrix (G) is a matrix whose rows form a basis for the code C; multiplying a message by the generator matrix encodes the message into a codeword. A parity check matrix (H) is the generator matrix of the dual code C⊥, where C⊥ contains vectors orthogonal to all codewords in C.
9. The Vernam cipher (or One-Time Pad) involves XORing the plaintext with a random key of equal length. It is considered a perfect cipher because, if the key is truly random and used only once, the ciphertext reveals no information about the plaintext, satisfying Shannon's definition of perfect secrecy.
10. EdDSA uses a deterministic approach for generating the secret parameter *k*, derived from a pseudorandom function of the private key and message, as opposed to a random *k*. This prevents key reuse vulnerabilities present in algorithms like ECDSA, where reusing *k* can compromise the entire signature scheme.

### Essay Questions

1. Compare and contrast the RSA and ElGamal cryptosystems, focusing on their underlying mathematical assumptions, key generation, encryption/decryption processes, and security strengths and weaknesses.
2. Explain Shannon's Theorem for perfect ciphers, including the key-independence assumption and equidistributed keys. Discuss how the Vernam cipher satisfies the conditions of Shannon's Theorem and why it is considered perfectly secure.
3. Discuss the different types of digital signature forgery attacks and their implications for the security of digital signature schemes. Analyze how DSA, ECDSA, and EdDSA address the challenges of existential forgery and key reuse.
4. Explain the concept of a group action and its use in post-quantum cryptography. Describe the Linear Code Equivalence Problem and its relevance to code-based cryptographic schemes.
5. Explain the concept of Zero-Knowledge Proofs. Describe the difference between completeness, soundness, and zero-knowledge. Explain how Zero Knowledge Proofs can be used for digital signatures.

### Glossary of Key Terms

- **Asymmetric Cryptography:** Encryption methods that use separate keys for encryption and decryption, also known as public-key cryptography.
- **Symmetric Cryptography:** Encryption methods that use the same key for both encryption and decryption, also known as private-key cryptography.
- **Group:** A set with an associative operation, a neutral element, and an inverse for every element.
- **Cyclic Group:** A group where every element can be generated by repeatedly applying the group operation to a single element (the generator).
- **Elliptic Curve:** A curve defined by an equation of the form y2 = x3 + ax + b, used in cryptography for its group properties.
- **Discrete Logarithm Problem (DLP):** The problem of finding the exponent x such that gx = h in a cyclic group, given g and h. Assumed to be computationally hard in certain groups.
- **IND-CPA:** Indistinguishability under Chosen Plaintext Attack; a security property of encryption schemes where an adversary cannot distinguish between the encryptions of two chosen plaintexts.
- **IND-CCA:** Indistinguishability under Chosen Ciphertext Attack; a stronger security property than IND-CPA, where an adversary can also request decryptions of ciphertexts (except for the challenge ciphertext).
- **RSA:** A widely used public-key cryptosystem based on the difficulty of factoring large numbers.
- **ElGamal:** A public-key cryptosystem based on the difficulty of the discrete logarithm problem.
- **Digital Signature:** A cryptographic mechanism used to verify the authenticity and integrity of digital documents.
- **DSA (Digital Signature Algorithm):** A NIST standard for digital signatures, based on the discrete logarithm problem.
- **ECDSA (Elliptic Curve Digital Signature Algorithm):** A variant of DSA that uses elliptic curves, providing shorter key lengths and improved efficiency.
- **EdDSA (Edwards-curve Digital Signature Algorithm):** A digital signature algorithm that avoids vulnerabilities found in ECDSA, using deterministic nonces and twisted Edwards curves.
- **Vernam Cipher (One-Time Pad):** A symmetric encryption scheme where the plaintext is XORed with a random key of equal length; perfectly secure if the key is truly random and used only once.
- **Perfect Cipher:** A cipher where the ciphertext reveals no information about the plaintext, i.e., P(m|c) = P(m) for all messages m and ciphertexts c.
- **Linear Code:** A code where codewords form a linear subspace of a vector space.
- **Generator Matrix:** A matrix whose rows form a basis for a linear code; used to encode messages into codewords.
- **Parity Check Matrix:** A matrix used to check if a received message is a valid codeword in a linear code.
- **Syndrome:** The result of multiplying a received message by the transpose of the parity check matrix; used to identify and correct errors in decoding.
- **Code Equivalence Problem:** Determining whether two linear codes are linearly equivalent.
- **MPC in the Head:** A technique for building signature schemes based on multi-party computation.
- **Group Action:** A function that defines how a group operates on a set.
- **Additive Secret Sharing:** A simple secret sharing scheme where the secret is split into shares that sum to the secret.
- **Shamir Secret Sharing:** A (t, n)-secret sharing scheme where the secret is the y-intercept of a random polynomial, and shares are points on that polynomial.
- **Unforgeability Under Chosen Message Attack:** A security property of signature schemes where an adversary cannot produce a signature on a new message after seeing signatures of adaptively chosen messages.
- **Zero-Knowledge Proof:** A proof that reveals no information beyond the truth of the statement being proven.
- **Soundness:** A property of a proof system that ensures a dishonest prover cannot convince the verifier of a false statement.
- **Completeness:** A property of a proof system that ensures an honest prover can always convince an honest verifier of a true statement.
- **Sigma Protocol:** A type of three-move protocol used in cryptography, often used in constructing zero-knowledge proofs.
- **Quadratic Residue:** An integer that is a square modulo another integer.