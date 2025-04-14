from pwn import *
from Crypto.Util.Padding import unpad
import sys

def main():
    r = remote('tramway.proxy.rlwy.net', 43425)

    r.recvuntil(b'Encrypted flag: ')
    encrypted_flag_hex = r.recvline().strip().decode()
    encrypted_flag = bytes.fromhex(encrypted_flag_hex)
    iv = encrypted_flag[:16]
    ciphertext = encrypted_flag[16:]
    ciphertext_blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    print(f"[*] Encrypted into {len(ciphertext_blocks)} blocks")

    plaintext_blocks = []

    for block_idx in reversed(range(len(ciphertext_blocks))):
        current_ct = ciphertext_blocks[block_idx]
        original_prev = iv if block_idx == 0 else ciphertext_blocks[block_idx - 1]
        print(f"[*] Attacking block {block_idx}")

        modified_prev = bytearray(16)
        d_block = bytearray(16)

        for byte_pos in reversed(range(16)):
            pad_length = 16 - byte_pos
            for j in range(byte_pos + 1, 16):
                modified_prev[j] = d_block[j] ^ pad_length

            found = False
            for guess in range(256):
                modified_prev[byte_pos] = guess
                crafted_ct = bytes(modified_prev) + current_ct
                r.sendlineafter(b'scared: ', crafted_ct.hex().encode())
                response = r.recvline()

                if b'valid padding, valid life choices' in response:
                    d_block[byte_pos] = guess ^ pad_length
                    found = True
                    print(f"[+] Block {block_idx} byte {byte_pos}: 0x{d_block[byte_pos]:02x}")
                    break

            if not found:
                print(f"[-] Failed to find byte {byte_pos} in block {block_idx}")
                sys.exit(1)

        plaintext_block = bytes([d_block[j] ^ original_prev[j] for j in range(16)])
        plaintext_blocks.insert(0, plaintext_block)
        print(f"[+] Decrypted block {block_idx}: {plaintext_block}")

    full_plaintext = b''.join(plaintext_blocks)
    flag = unpad(full_plaintext, 16).decode()
    print(f"\n[+] Flag: {flag}")

    r.close()

if __name__ == "__main__":
    main()
