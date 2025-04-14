from rvnlib.aes_cbc_rvn import AES_CBC_RVN
from hashlib import sha256

import json
import zlib


class RVN:

	def __init__(self, user=b"user", password=b"AnRvnDefaultPasswordMakeSureToChangeBeforeDeployingToProduction!", filename="file", size=0):
		self.user = user
		self.password = password
		self.filename = filename
		self.size = size
		self.generate_metadata()

	"""Metadata 
	format : {"size": 0, "filename": "", "user": "", "password_hash": ""}+padding

	(size = 300 bytes and formatted in json)
	
	header ("BRVN") -> 4
	size -> 4
	filename -> 112
	user -> 32
	password_hash -> 64
	json size -> 60
	"""

	def generate_metadata(self):
		
		metadata = {}
		metadata["user"] = self.user.decode()
		metadata["password_hash"] = sha256(self.password).hexdigest()
		metadata["filename"] = self.filename
		metadata["size"] = self.size

		self.metadata = json.dumps(metadata).encode()

		self.padding_len = 300-len(self.metadata)
		self.metadata += self.padding_len*b"\x00"
		
		return self.metadata
	
	def encrypt(self, data):
	
		cipher = AES_CBC_RVN(self.user, self.password)
		self.encrypted = cipher.encrypt(data)
		self.encrypted = zlib.compress(self.encrypted) # gotta keep it small
		
		return self.encrypted

	def decrypt(self, ciphertext):

		cipher = AES_CBC_RVN(self.user, self.password)
		ciphertext = zlib.decompress(ciphertext)
		self.decrypted = cipher.decrypt(ciphertext)
		
		return self.decrypted

	def generate_container(self):
		self.secure_container = b'BRVN' + self.metadata + self.encrypted
		return self.secure_container

	def decrypt_container(self, container):

		self.read_metadata()
		filename = self.parsed_metadata["filename"]
		
		ciphertext = container[304:]

		plaintext = self.decrypt(ciphertext)
		return {"data":plaintext, "filename":filename}

	def read_metadata(self):
		self.parsed_metadata = json.loads(self.secure_container[4:300-self.padding_len+4])
		return self.parsed_metadata	
