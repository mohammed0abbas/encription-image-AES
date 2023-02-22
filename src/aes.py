from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes


def encrypt(input_file, output_file, key):
    # Create AES object
    cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
    # Read data from original file
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    # Encrypt data and get IV
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    iv = cipher.iv
    # Save IV and encrypted data in new file
    with open(output_file, 'wb') as f:
        f.write(iv)
        f.write(ciphertext)


def decrypt(input_file, output_file, key):
    # Open encrypted file and read IV and encrypted data
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    # Create AES object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt data and remove added bytes to make data size multiple of block size
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    # Save decrypted data in new file
    with open(output_file, 'wb') as f:
        f.write(plaintext)