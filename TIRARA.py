#!/usr/bin/env python3

def decrypt(ciphertext: bytes, key: bytes = b"TIRARA") -> str:
    """
    Given the ciphertext as bytes, this function performs the reverse of the binary's
    transformation: it XORs each byte with the repeating key and then reverses the 
    resulting byte array to recover the original flag.
    
    The binary encryption process is:
       encrypted = XOR(reverse(user_input), key_repeating)
       
    Therefore, decryption is:
       user_input = reverse( XOR(encrypted, key_repeating) )
    """
    # XOR decryption: XOR each byte with the repeating key
    xored = bytearray()
    for i, byte in enumerate(ciphertext):
        xored.append(byte ^ key[i % len(key)])
    
    # Reverse the result to get the original flag
    original = xored[::-1]
    
    try:
        return original.decode('utf-8')
    except UnicodeDecodeError:
        return repr(original)

if __name__ == "__main__":
    # The ciphertext extracted from DAT_00102010 (28 bytes)
    # Provided in hex: 
    # 29 24 61 25 33 74 0b 2d 61 36 28 72 19 16 3e 72 05 1e 60 25 63 0d 29 1b 00 78 1e 07
    ciphertext_hex = (
        "29" "24" "61" "25" "33" "74" "0b" "2d"
        "61" "36" "28" "72" "19" "16" "3e" "72"
        "05" "1e" "60" "25" "63" "0d" "29" "1b"
        "00" "78" "1e" "07"
    )
    
    try:
        ciphertext = bytes.fromhex(ciphertext_hex)
    except ValueError:
        print("Error parsing the ciphertext hex!")
        exit(1)
    
    if len(ciphertext) != 28:
        print(f"Expected 28 bytes but got {len(ciphertext)} bytes.")
        exit(1)
    
    flag = decrypt(ciphertext)
    print("Recovered flag:", flag)
