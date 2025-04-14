from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sys

ciphertext = bytes.fromhex("f90b3e346936ed44f68451df44120e867a1408afea54f0fb824d5a10ff78a511")
iv = b"0000000000000000"

with open("rockyou.txt", "r", encoding="latin-1") as f:
    for line in f:
        password = line.strip()
        try:
            padded_password = pad(password.encode("latin-1"), 16)
            key = padded_password[:16]
            cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            decrypted = cipher.decrypt(ciphertext)
            unpadded = unpad(decrypted, 16)
            if unpadded.startswith(b'FL1TZ{'):
                print(f"Password Found: {password}")
                print(f"Flag: {unpadded.decode('latin-1')}")
                sys.exit(0)
        except (ValueError, Exception):
            continue

print("Failed to find the correct password.")
