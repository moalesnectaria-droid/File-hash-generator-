import hashlib
import sys


def calculate_sha256(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()

    return hashlib.sha256(file_data).hexdigest()


def calculate_sha512(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()

    return hashlib.sha512(file_data).hexdigest()


def verify_hash(actual_hash, expected_hash):
    expected_hash = expected_hash.lower()

    if len(expected_hash) != 64:
        print("Error: SHA-256 hash must contain 64 hexadecimal characters.")
        return False

    if not all(character in "0123456789abcdef" for character in expected_hash):
        print("Error: Invalid SHA-256 hash format.")
        return False

    return actual_hash == expected_hash


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage:")
        print("  python hash_generator.py <file>")
        print("  python hash_generator.py <file> <expected_sha256>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        sha256_hash = calculate_sha256(file_path)
        sha512_hash = calculate_sha512(file_path)

        print("File:", file_path)
        print()
        print("SHA-256:", sha256_hash)
        print("SHA-512:", sha512_hash)

        if len(sys.argv) == 3:
            expected_hash = sys.argv[2]

            if verify_hash(sha256_hash, expected_hash):
                print()
                print("✓ File integrity verified.")
            else:
                if len(expected_hash) == 64 and all(
                    character.lower() in "0123456789abcdef"
                    for character in expected_hash
                ):
                    print()
                    print("⚠ WARNING: File has been modified.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
        sys.exit(1)


if __name__ == "__main__":
    main()