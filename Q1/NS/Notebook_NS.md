**Briefing Document: Network Security Concepts and Defenses**

**Introduction:**

This briefing document consolidates information from five slide decks focusing on network security. It covers topics ranging from the history of the internet to modern defensive technologies and privacy concerns. The key areas include historical context, security properties, the OSI model, vulnerabilities, privacy, and defensive technologies like firewalls, intrusion detection systems, and threat intelligence.

**1. Historical Context (Slides1.pdf, Slides2.pdf):**

- **Internet Origins:** The internet's history is traced back to Joseph Licklider's vision in 1962 of a globally interconnected network, followed by key developments such as packet switching theory (Leonard Kleinrock, 1961), ARPANET (Lawrence Roberts, 1966), the first ARPANET nodes at UCLA and SRI (1969), networked email (Ray Tomlinson, 1972), TCP/IP (Vint Cerf and Bob Kahn, 1973), the OSI Reference Model (ISO, 1980), UDP (David P. Reed, 1980), the World Wide Web (Tim Berners-Lee, 1989), and the official definition of "Internet" (Federal Networking Council, 1995).
- **Early Security Concerns:** The document notes that early internet development did not prioritize security. The first network worms, Creeper (Bob Thomas, 1971) and Reaper (Ray Tomlinson, 1972), marked the beginnings of security concerns.
- **Evolution Towards Security:** Security considerations came into the picture much later as the internet evolved.

**2. Security Properties (Slides1.pdf):**

- **CIA Triad:** Fundamental security properties are defined using the CIA triad:
- **Confidentiality:** "preserving authorized restrictions on information access and disclosure, including means for protecting personal privacy and proprietary information"
- **Integrity:** "guarding against improper information modification or destruction, and includes ensuring information non-repudiation and authenticity"
- **Availability:** "ensuring timely and reliable access to and use of information."
- **Authenticity:** "the property that data originated from its supposed source."
- **Non-repudiation:** "the integrity and origin can be verified and validated by a third party as having originated from a specific entity in possession of the private key (i.e., the signatory)"
- **Privacy:** "The right of a party to maintain control over and confidentiality of information about itself." The document highlights that privacy is related to but distinct from security.

**3. Alice, Bob, and the Foe (Slides1.pdf):**

- **Cryptographic Couple:** Introduces Alice and Bob as "the world’s most famous cryptographic couple", initially mentioned in a paper by Rivest, Shamir, and Adleman (1978). They are used as archetypes in cryptographic scenarios.
- **Focus on Information Sharing:** The document notes they "want to share information," highlighting the fundamental objective of cryptography.

**4. Trust (Slides1.pdf, Slides4.pdf):**

- **Definition:** Trust is defined as "A characteristic of an entity that indicates its ability to perform certain functions or services correctly, fairly and impartially, along with assurance that the entity and its identifier are genuine." (NIST). The document references Ken Thompson's "Reflections on Trusting Trust" (1984).
- **Trust in Protocols:** The document later demonstrates that protocols, such as ARP, are based on trust, and such trust can be exploited, i.e., ARP Poisoning.

**5. The OSI Model (Slides2.pdf):**

- **Layered Architecture:** The slides detail the OSI model, focusing on relevant layers for network security.
- **Level 1 (Physical):** Deals with the physical transmission of data.
- **Level 2 (Data Link):** Includes error control, packet switching, and frame synchronization. Uses MAC addresses. (e.g., "00:1b:63:84:45:e6") Key protocols include ARP and PPP.
- **Level 3 (Network):** Handles routing and logical addressing using IP addresses (e.g., "10.1.1.5"). Related protocols are IPv4, IPv6, ICMP, and IPsec.
- **Level 4 (Transport):** Provides connection-oriented (TCP) or connectionless (UDP) transport of data. TCP is defined in RFC 793 and is for a "reliable, ordered, and error-checked stream of bytes" while UDP is a lightweight protocol.
- **Other Levels:** The document lists Level 5 (Session), Level 6 (Presentation), and Level 7 (Application) but focuses more on the lower layers.
- **ARP and ARP Poisoning:** The Address Resolution Protocol (ARP) is explained as a way to map IP addresses to MAC addresses. The slides demonstrate ARP poisoning and its potential for man-in-the-middle attacks. The document states: "ARP is based on trust!"
- **TCP and Three-Way Handshake:** The TCP three-way handshake (SYN, SYN-ACK, ACK) is described and is followed up with how it can be vulnerable to Denial-of-Service (DoS) attacks.
- **Mitigations:** For TCP handshake based DoS attacks, three mitigation strategies are listed: 1. Increasing backlog queue. 2. Recycling the oldest half-open TCP connection. 3. SYN cookies.

**6. Transport Layer Security (TLS) (Slides2.pdf):**

- **TLS Purpose:** TLS is explained as a protocol providing "1. Authentication 2. Confidentiality 3. Integrity."
- **TLS Handshake:** The TLS handshake process is detailed, including the Client Hello, Server Hello, client certificate (if requested), Client Key Exchange, Certificate Verify, Change Cipher Spec, and Finished messages. This ensures a shared key for the encrypted communication.
- **TLS Vulnerabilities:** The document explains that "You cannot just 'deploy' TLS", you must "choose the versions of TLS you want to offer," "choose the set of available cipher(s)," "set a certificate issued by a trustworthy CA," and "cope with implementation issues."
- **TLS Configurability:** The need for sysadmins to customize TLS deployments (e.g., versions, cipher suites) is emphasized.
- **TLS Attacks:** The document mentions attack vectors, referring to an "Attack Tree for TLS 1.2" and introduces TLSAssistant as a tool for proper configuration and vulnerability detection.
- **TLS Vulnerabilities:** Includes examples such as CRIME and BREACH attacks related to compression weaknesses in TLS and HTTP respectively.

**7. Vulnerabilities (Slides3.pdf):**

- **Definition:** "Weakness in an information system, system security procedures, internal controls, or implementation that could be exploited or triggered by a threat source" (NIST).
- **CVSS:** The Common Vulnerability Scoring System (CVSS) is introduced as a standard for rating the severity of software vulnerabilities. It mentions the various versions, CVSSv1, CVSSv2, CVSSv3, and CVSSv4. CVSSv4 metrics such as Attack Vector (AV), Attack Complexity (AC), and Impact metrics (Confidentiality, Integrity, Availability) are discussed.
- **CVSS v3.1 Example:** The document also shows the scoring for the Heartbleed vulnerability: "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N" which is broken down into its components.
- **MITRE:** MITRE is introduced as a non-profit organization that manages databases of vulnerabilities (CVE) and weaknesses (CWE).
- **CVE (Common Vulnerabilities and Exposures):** Publicly disclosed vulnerabilities or weaknesses in software/hardware.
- **CWE (Common Weakness Enumeration):** Catalog of software and hardware weaknesses that can lead to vulnerabilities.
- **NVD (National Vulnerability Database):** A comprehensive repository by NIST that contains CVSS scores, descriptions, and references for each CVE.
- **OWASP Top Ten:** A list from the Open Web Application Security Project that ranks the most critical security risks to web applications. The document lists the most recent ranking.
- **Responsible Disclosure:** The document states: "You should perform a responsible disclosure" for a discovered vulnerability.

**8. Privacy (Slides4.pdf):**

- **Privacy Definition:** Reiterates: "The right of a party to maintain control over and confidentiality of information about itself."
- **Anonymity:** "Condition in identification whereby an entity can be recognized as distinct, without sufficient identity information to establish a link to a known identity" (NIST).
- **Cookies:** The slides trace the history of cookies, starting with their creation by Lou Montulli in 1994, explaining how they are used for personalization and tracking.
- **EU Regulation:** Notes that the 2009 EU Directive 2009/136/EC regulates cookies.
- **Room 641A and PRISM:** Briefly mentions Room 641A, an AT&T facility involved in mass surveillance and PRISM, a surveillance program revealed by Edward Snowden.
- **Mitigations:** Discusses mitigation strategies for privacy issues, like ad blocking, Virtual Private Networks (VPN), and Tor.
- **VPNs:** Provides an explanation of how VPNs operate by creating a secure tunnel to a VPN server which in turn connects to the final service/website.
- **Tor:** Explains the history of Tor and the onion routing project, including its architecture and relays. The document asks: "Should we trust them?" It mentions Tor hidden/onion services and the use of relays. It then states: "The set of web pages on the World Wide Web that cannot be indexed by search engines... and use encryption to provide anonymity and privacy for users" is the Dark Web.

**9. Defensive Technologies (Slides5.pdf):**

- **Overview:** Introduces various defensive technologies: Hardening, Firewalls, Intrusion Detection and Prevention Systems (IDS/IPS), Security Information and Event Management (SIEM), Honeypots, Anomaly Detection, and Threat Intelligence. The document states: "Enforce best practices and verify alerts" and "Update".
- **Hardening:** "set of tools, methods and best practices... to limit vulnerabilities of systems and their attack surface." It lists hardening practices across Networks, Applications, OS, Servers, and Devices. It also provides Shodan.io and Github links showcasing known exposed systems. It highlights the need to "Understand the requirements and goals," to "Develop a strategy for progressive, incremental changes," to "Prioritize actions according to risks," and to "Leverage automation" The document also contains an example where a Python webserver with various vulnerabilities is created and fixed as a hardening example. A second hardening example involves Mosquitto, an MQTT broker.
- **Firewalls:** "device or software to monitor and control incoming and outgoing network traffic based on predetermined security rules." It explains the various types of firewalls: Packet filtering, Circuit-level, Stateful, Proxy-based and notes that firewalls operate from the network layer (L3). The document details the typical flaws with a firewall (e.g., excessive rules, failure to review). It provides a network firewall example using docker and Ubuntu.
- **IDS/IPS:** "IDS monitors network traffic for suspicious activity and alerts administrators, while IPS takes proactive measures to block or prevent detected threats." The document differentiates between Signature-Based IDS and Anomaly-Based IPS. It explains when and where to deploy IDS/IPS, and how attackers evade network-based IDS/IPS via Fragmentation, Flooding, Obfuscation, and Encryption. SNORT, an open-source IDS/IPS tool, is mentioned as an example. A demonstration of the SNORT IDS system is included using Docker and NMAP.
- **SIEM:** "cybersecurity solution that aggregates and analyzes log and event data from various systems."
- **Honeypots:** The document details the use of Honeypots for cybersecurity: "Different types serve different purpose: e.g., email traps ... decoy database ... malware honeypot ... spider honeypot.". The document describes the interactivity of honeypots from weakly to highly interactive and notes that they should "Emulate but not replicate/use real infrastructure/data" as well as the fact that "You are responsible for its use". Cowrie, an open-source honeypot system, is then given as an example.
- **Anomaly Detection:** "activities to identify patterns in data that do not conform to expected behavior, often indicating potential security threats or system faults." It defines types of anomalies: Point, Contextual, Collective, Temporal, and Spatial and notes that they can be detected via Rule-Based, Machine Learning based (Supervised, Unsupervised, Semi-Supervised), and Statistical Methods.
- **Zero Trust:** "a cybersecurity approach that eliminates implicit trust, requiring continuous verification of every user and device attempting to access resources, regardless of their location." It lists the core principles: "Verify Explicitly," "Least Privilege Access," and "Assume Breach." The Cybersecurity and Infrastructure Security Agency's "Zero Trust Maturity Model v2.0" is also cited and it's five pillars: Identity, Devices, Networks, Applications and Workloads, and Data are listed. The document then details Zero Trust's support at the network layer. The benefits of Zero Trust Segmentation are also detailed. Firezone is introduced as an open-source platform that supports Zero Trust.
- **Threat Intelligence:** It is described as "the process of gathering, analyzing, and sharing information about current and potential threats." The document then lists the different types of Threat Intelligence: Strategic, Tactical, Operational, and Technical, explaining how they interconnect. MISP, an open-source Threat Intelligence Platform, is cited as an example.

**Conclusion:**

These slides provide a comprehensive overview of network security, from its historical underpinnings to current best practices. Key takeaways include the importance of understanding the underlying layers of network communication (OSI model), the fundamental principles of security (CIA triad), and the critical role of defensive technologies in protecting against cyber threats. The document highlights the balance between security and privacy, and the importance of staying vigilant and proactive in the ever-evolving cybersecurity landscape.


***


# Network Security Study Guide

## Quiz

1. What was Joseph Licklider's vision regarding interconnected computers, and what role did he play at DARPA?
2. Explain the significance of Leonard Kleinrock's work and how it influenced Lawrence G. Roberts in the development of the ARPANET.
3. Describe the function of the Address Resolution Protocol (ARP) within a network.
4. What are the three core principles encompassed by the CIA triad in network security?
5. What is the purpose of a three-way handshake in the TCP protocol, and what potential security vulnerability does this process create?
6. Briefly explain what TLS is, and what are some key aspects to its configurability?
7. What is a CVE, and how does it differ from a CWE?
8. Describe the main function of a SIEM system in network security.
9. What are the key differences between signature-based and anomaly-based intrusion detection systems?
10. Describe one common method an attacker might use to evade a network-based IDS/IPS and how that would work.

## Quiz Answer Key

1. Licklider envisioned a globally interconnected set of computers for quick data and program access, and he became the first head of DARPA.
2. Kleinrock published the first paper on packet switching theory, which convinced Roberts of the feasibility of packet-based communication, leading to ARPANET's development.
3. ARP resolves IP addresses to MAC addresses, enabling devices on a local network to communicate by mapping a logical network address to a physical hardware address.
4. The CIA triad stands for Confidentiality, ensuring authorized access restrictions; Integrity, guarding against improper information modification; and Availability, ensuring reliable access and use of information.
5. The three-way handshake establishes a connection between client and server by exchanging SYN, SYN-ACK, and ACK messages, and the resource reservation during the handshake can be exploited in a denial-of-service attack by flooding the server with many SYN requests.
6. TLS is a protocol that provides authentication, confidentiality, and integrity for network communications, and it's configurable with respect to the protocol versions, ciphers, and certificates that can be offered.
7. A CVE is a specific, publicly disclosed vulnerability, while a CWE represents a class or type of software weakness that can lead to such vulnerabilities.
8. A SIEM system aggregates and analyzes log and event data from various systems within an IT environment, providing long-term storage, analysis, and real-time event correlation.
9. Signature-based IDS detects known threats by comparing network traffic against a database of attack signatures, whereas anomaly-based IDS establishes a baseline of normal network behavior and identifies deviations from this norm.
10. Attackers may evade signature-based IDS/IPS by obfuscating their malicious traffic, altering its appearance without changing its functionality so it won’t match the known patterns the IDS/IPS is looking for.

## Essay Questions

1. Trace the historical development of the internet and its security, highlighting key milestones and the evolution of security concerns and solutions.
2. Explain how the OSI model functions and illustrate its significance through the example of the Address Resolution Protocol (ARP). Analyze how vulnerabilities at different levels of the OSI model can be exploited in attacks.
3. Discuss the interrelation of trust, privacy, and anonymity in online communication, and explain how tools like cookies, VPNs, and Tor attempt to impact this relationship.
4. Elaborate on the concept of a "Zero Trust" network architecture and how different defensive technologies (e.g., firewalls, IDS/IPS, segmentation) can be implemented to support this approach.
5. Assess the importance of vulnerability management and describe the processes and tools involved (e.g., CVSS, CVE, CWE, NVD, OWASP) in identifying, categorizing, and mitigating potential security threats.

## Glossary of Key Terms

- **ARPANET:** The precursor to the internet, developed by DARPA, which established the foundations for packet-switched networks.
- **Packet Switching:** A method of data transmission where data is broken into packets that can travel independently across a network and reassembled at the destination.
- **TCP/IP:** A suite of communication protocols used to interconnect network devices on the internet; TCP ensures reliable delivery and IP provides addressing.
- **OSI Model:** A conceptual framework that characterizes and standardizes the communication functions of a telecommunication or computing system without regard to its underlying internal structure and technology; it is divided into seven layers.
- **MAC Address:** A unique identifier assigned to network interface controllers for communications within a network segment.
- **IP Address:** A logical address assigned to a device connected to a computer network that uses the Internet Protocol for communication.
- **ARP (Address Resolution Protocol):** A protocol used to resolve IP addresses to MAC addresses, enabling communication within a local network.
- **CIA Triad:** The core principles of information security: Confidentiality, Integrity, and Availability.
- **Authenticity:** The property of being genuine and originating from its supposed source.
- **Non-repudiation:** Assurance that data's origin and integrity can be verified by a third party and is tied to a specific entity.
- **TLS (Transport Layer Security):** A cryptographic protocol used to secure communication over a computer network by ensuring authentication, confidentiality, and integrity.
- **Cookie:** A small piece of data stored by a web browser, used to track user preferences and activity.
- **VPN (Virtual Private Network):** A network technology that creates a secure and encrypted connection over a less secure network, typically used to ensure private communication or to bypass restrictions.
- **Tor:** A network of virtual tunnels that allows for anonymity by routing traffic through multiple relays before reaching its destination.
- **CVE (Common Vulnerabilities and Exposures):** A publicly disclosed cybersecurity vulnerability or weakness in software or hardware.
- **CWE (Common Weakness Enumeration):** A catalog of software and hardware weaknesses that can lead to security vulnerabilities.
- **CVSS (Common Vulnerability Scoring System):** A standard for assessing the severity of a vulnerability, providing metrics to understand its potential impact.
- **NVD (National Vulnerability Database):** A comprehensive database of publicly known cybersecurity vulnerabilities.
- **OWASP (Open Web Application Security Project):** A non-profit organization focused on improving software security, known for its top ten list of web application security risks.
- **Hardening:** The process of reducing the attack surface of a system or network by limiting vulnerabilities.
- **Firewall:** A network security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules.
- **IDS (Intrusion Detection System):** A system that monitors network traffic for suspicious activity and alerts administrators.
- **IPS (Intrusion Prevention System):** A system that proactively blocks or prevents detected threats in network traffic.
- **SIEM (Security Information and Event Management):** A cybersecurity solution that aggregates and analyzes log and event data from various systems within an IT environment.
- **Honeypot:** A decoy system that attracts attackers to detect and gather information on threats.
- **Anomaly Detection:** The identification of patterns in data that deviate from expected behavior, often indicating potential security threats.
- **Threat Intelligence:** Information on potential threats to an organization, including the tactics, techniques, and procedures (TTPs) of threat actors.
- **Zero Trust:** A cybersecurity approach that eliminates implicit trust, requiring continuous verification of every user and device attempting to access resources.