# Import
from passlib.hash import sha512_crypt
import getpass

# Hash function. Salt size and Rounds configured to not occur
hash = sha512_crypt.encrypt(
    getpass.getpass('Password:'),
    salt_size=8,
    rounds=5000,
    implicit_rounds=True,
)
print hash + '\n'
print 'Verification:'
print sha512_crypt.verify(getpass.getpass('Retype password: '), hash)
