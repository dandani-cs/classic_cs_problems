# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase # return function.upper()

#     return wrapper # return function.upper


#     def say_hi():
#     return 'hello there'

# decorate = uppercase_decorator(say_hi) # function.upper("hello there")
# decorate()


from secrets import token_bytes
from typing import Tuple

def random_key(length):
	tb = token_bytes(length)
	return int.from_bytes(tb, "big")

def encrypt_dec(function):
	def encrypt():
		original_data = function
		original_bytes = original_data.encode()
		dummy_key = random_key(len(original_bytes))
		original_key = int.from_bytes(original_bytes, "big")
		encrypted = original_key ^ dummy_key
		return dummy_key, encrypted

	return encrypt

def decrypt(key1, key2):
	original_int = key2 ^ key1
	original_bytes = original_int.to_bytes(original_int.bit_length() + 7, "big")
	return original_bytes.decode()

def say_hi():
	return 'hello there'


if __name__ == '__main__':
	decorate = encrypt_dec(say_hi)
	key1, key2 = decorate()
	result = decrypt(key1, key2)
	print(result)