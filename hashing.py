import hashlib

data = input("Enter the data to hash: ")
hash_object = hashlib.sha256(data.encode())
hex_dig = hash_object.hexdigest()
print("The SHA-256 hash of your data is:", hex_dig)

data2 = input("Enter the data again for verification: ")
hash_object2 = hashlib.sha256(data2.encode())
hex_dig2 = hash_object2.hexdigest()

if hex_dig == hex_dig2:
    print("The hashes match! The data is unchanged.")
else:
    print("The hashes do not match! The data has been modified.")



