"""
One time pad encryption with image

"""

from secrets import token_bytes
from typing import Tuple

def random_key(length):
	tb = token_bytes(length)
	return int.from_bytes(tb, "big")

def encrypt(original_data):
	# original_bytes = original_data.encode()
	# no need for encoding to bytes since original_data is passed on as bytes
	original_bytes = original_data
	dummy_key = random_key(len(original_bytes))
	original_key = int.from_bytes(original_bytes, "big")
	encrypted = original_key ^ dummy_key
	return dummy_key, encrypted

def decrypt(key1, key2):
	original_int = key2 ^ key1
	original_bytes = original_int.to_bytes(original_int.bit_length() + 7, "big")
	return original_bytes


if __name__ == '__main__':
	with open("ex4pic.png", "rb") as image:
		img_byte = image.read()
	key1, key2 = encrypt(img_byte)
	result = decrypt(key1, key2)
	print(result)