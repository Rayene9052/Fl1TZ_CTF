from rvnlib import rvn
import os
import zlib

with open ("flag", "rb") as f:
	FLAG = f.read()

file = rvn.RVN(b'rvn', os.urandom(16), 'flag', len(FLAG))

file.encrypt(FLAG)

file.generate_container()

with open(f"{file.filename}.rvn", "wb") as f:
	f.write(file.secure_container)
	

