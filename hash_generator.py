import hashlib
import sys

if len(sys.argv) not in (2, 3):
    print("Usage:")
    print("  python hash_generator.py <file>")
    print("  python hash_generator.py <file> <expected_sha256>")
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

    if len(sys.argv) == 3:
        expected_hash = sys.argv[2].lower()

        if len(expected_hash) != 64:
            print()
            print("Error: SHA-256 hash must contain 64 hexadecimal characters.")
            sys.exit(1)

        if not all(character in "0123456789abcdef" for character in expected_hash):
            print()
            print("Error: Invalid SHA-256 hash format.")
            sys.exit(1)

        if sha256_hash == expected_hash:
            print()
            print("✓ File integrity verified.")
        else:
            print()
            print("⚠ WARNING: File has been modified.")

except FileNotFoundError:
    print(f"Error: File '{file_path}' was not found.")
    sys.exit(1)