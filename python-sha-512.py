from passlib.hash import sha512_crypt
import random
import string
hash = sha512_crypt.encrypt(
    raw_input('clear-text password: '), 
    salt_size=8,
    rounds=5000,
    implicit_rounds=True,
)
print hash + '\n'
print 'verification\n'
print sha512_crypt.verify(raw_input('clear-text password: '), hash)
