import hashlib

# List of algorithms we want to try
algorithms = ["md5", "sha1", "sha256", "sha512"]

# Take input from user
data = input("Enter the data to hash: ")

# Loop through each algorithm and generate hash
for algo in algorithms:
    hash_object = hashlib.new(algo)   # create new hash object
    hash_object.update(data.encode()) # encode and hash
    hex_digest = hash_object.hexdigest()
    print(f"{algo.upper()} hash: {hex_digest}")
