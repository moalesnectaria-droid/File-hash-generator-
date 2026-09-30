import hashlib
import sys

if len(sys.argv) != 2:
    print("Usage: python hash_generator.py <file>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, "rb") as file:
        file_data = file.read()

    sha256_hash = hashlib.sha256(file_data).hexdigest()
    sha512_hash = hashlib.sha512(file_data).hexdigest()

    print("File:", file_path)
    print()
    print("SHA-256:", sha256_hash)
    print("SHA-512:", sha512_hash)

except FileNotFoundError:
    print(f"Error: File '{file_path}' was not found.")
    sys.exit(1)