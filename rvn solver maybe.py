import zlib
import hashlib
from Crypto.Cipher import AES

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def decrypt_custom(ciphertext_full, key):
    iv = ciphertext_full[:16]
    ciphertext = ciphertext_full[16:]
    ecb_cipher = AES.new(key=key, mode=AES.MODE_ECB)
    plaintext = b""
    len_ct = len(ciphertext)
    
    for pos in range(0, len_ct, 16):
        chunk = ciphertext[pos:pos+16]
        next_chunk = ciphertext[pos+16:pos+32]
        if len(next_chunk) == 0:
            if len_ct <= 16:
                prev = iv
            else:
                prev_start = pos - 16
                if prev_start < 0:
                    prev = iv
                else:
                    prev = ciphertext[prev_start:pos]
            prev_encrypted = ecb_cipher.encrypt(prev)
            plaintext_block = xor(prev_encrypted[:len(chunk)], chunk)
            plaintext += plaintext_block
        else:
            if pos == 0:
                xored = ecb_cipher.decrypt(chunk)
                plaintext_block = xor(xored, iv)
            else:
                xored = ecb_cipher.decrypt(chunk)
                prev_ciphertext = ciphertext[pos-16:pos]
                plaintext_block = xor(xored, prev_ciphertext)
            plaintext += plaintext_block
    return plaintext

with open('flag.rvn', 'rb') as f:
    data = f.read()

encrypted_compressed = data[4 + 300:]

encrypted = zlib.decompress(encrypted_compressed)
iv = encrypted[:16]
ciphertext_full = encrypted
password_part1 = iv[3:16]
target_hash = '55de3b89a19367d3bf7cef3233b145b016c41f98e2943552c6b11901b0ca2905'

found = False
for i in range(0x1000000):
    suffix = i.to_bytes(3, 'big')
    password = password_part1 + suffix
    h = hashlib.sha256(password).hexdigest()
    if h == target_hash:
        print(f"Found password: {password.hex()}")
        found = True
        break

if not found:
    print("Password not found")
    exit()

key = hashlib.sha256(password).digest()[:16]

plaintext = decrypt_custom(ciphertext_full, key)

print("Decrypted plaintext:", plaintext)
print("Flag:", plaintext.decode())
