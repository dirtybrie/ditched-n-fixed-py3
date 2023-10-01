#This script I learned from a class I took. It allows to run a very basic
#dictionary attack on a MD5 hash.
#Through the Hashlib module you can add more options like SHA, 
#go check it out at https://docs.python.org/3/library/hashlib.html
#to create hash: echo -n yourpassword | md5sum
#yours truly, db

import hashlib

pass_found=0

i_hash = input("Enter the hashed password:")
p_doc = input("\nEnter password filename including path:")

p_file = open(p_doc, 'r')
	
for word in p_file:
	enc_word = word.encode('utf-8')
	hash_word = hashlib.md5(enc_word.strip())
	digest = hash_word.hexdigest()
	
	if digest == i_hash:
		print("Password found:", word)
		pass_found=1
		break
if not pass_found:
	print("Can't find Password :(")
