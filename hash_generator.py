import hashlib
import sys

if len(sys.argv) != 2:
    print("Usage: python hash_generator.py <file>")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, "rb") as file:
    file_data = file.read()

file_hash = hashlib.sha256(file_data).hexdigest()

print("File:", file_path)
print("SHA-256:", file_hash)