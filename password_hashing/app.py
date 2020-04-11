from passlib.hash import sha256_crypt

password = sha256_crypt.encrypt("test")
print(password)
print(sha256_crypt.verify("test", password))
