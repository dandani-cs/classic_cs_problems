"""
One time pad encryption

"""

from secrets import token_bytes
from typing import Tuple

def random_key(length):
	tb = token_bytes(length)
	return int.from_bytes(tb, "big")

def encrypt(original_data):
	original_bytes = original_data.encode()
	dummy_key = random_key(len(original_bytes))
	original_key = int.from_bytes(original_bytes, "big")
	encrypted = original_key ^ dummy_key
	return dummy_key, encrypted

def decrypt(key1, key2):
	original_int = key2 ^ key1
	original_bytes = original_int.to_bytes(original_int.bit_length() + 7, "big")
	return original_bytes.decode()


if __name__ == '__main__':
	key1, key2 = encrypt("This is awesome, dude")
	result = decrypt(key1, key2)
	print(result)