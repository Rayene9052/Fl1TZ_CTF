import socket
from binascii import hexlify, unhexlify

original_pt0 = b"I forgot to do i"
desired_pt0 = b"My dog ate it :)"

def main():
    host = 'trolley.proxy.rlwy.net'
    port = 45004
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    data = s.recv(1024).decode().strip()
    print("Received:", data)
    
    prefix = "Did you do your homework? : "
    if not data.startswith(prefix):
        print("Unexpected initial message format")
        return
    iv_ciphertext = data[len(prefix):]
    iv_hex = iv_ciphertext[:32]
    ciphertext_hex = iv_ciphertext[32:]
    
    iv_static = unhexlify(iv_hex)
    iv_new = bytes([a ^ b ^ c for a, b, c in zip(original_pt0, iv_static, desired_pt0)])
    iv_new_hex = hexlify(iv_new).decode()
    
    user_input = iv_new_hex + ciphertext_hex
    s.sendall(user_input.encode() + b'\n')
    
    response = s.recv(1024).decode()
    print("Response:", response)
    
    s.close()

if __name__ == "__main__":
    main()
