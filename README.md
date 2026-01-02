# 🔐 SHA-256 Hash Checker & Multi-Hash Generator

> **Secure. Simple. Lightweight.**
> A Python-based utility suite designed for interactive cryptographic hashing and data verification.

---

## 🛠️ Tools Included

* 🐍 **hashing.py (Verification Tool)** — An interactive script to hash a string and perform a comparison check to verify data integrity.
* 🧩 **multi_hash.py (Generator Tool)** — A multi-algorithm engine that simultaneously generates **MD5, SHA1, SHA256, and SHA512** hashes for any given text.

---

## ⚙️ Technical Setup

### Prerequisites
* **Python 3.x** — The scripts utilize the built-in `hashlib` library (no external pip installations required).

### Installation & Usage
```bash
# Clone the repository
git clone [https://github.com/nandhana-dev/hash-checker.git](https://github.com/nandhana-dev/hash-checker.git)

# Navigate to the directory
cd hash-checker

# Run the tools
python hashing.py
python multi_hash.py

---

#example output

Enter the data to hash: hello
MD5 hash: 5d41402abc4b2a76b9719d911017c592
SHA1 hash: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA256 hash: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
SHA512 hash: 9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72...
