# ElGamal Cipher
from random import randint as rand


def cryption_message(message, key):
    cipher_message = ''
    for i in message:
        k = rand(2, 1107)
        y = 277 ** key % 1109
        a = 277 ** k % 1109
        b = y ** k * ord(i) % 1109
        cipher_message += str(a) + ' ' + str(b) + ' '
    return cipher_message


def decryption_message(cipher, key):
    message = ''
    for j in range(0, len(cipher) - 1, 2):
        a = int(cipher[j])
        b = int(cipher[j + 1])
        message += chr((b * a ** (1109 - 1 - key)) % 1109)
    return message


if __name__ == '__main__':
    mode = input('Select mode:\n1. Encryption\n2. Decryption\n').upper()
    secret_key = int(input('Input secret key: '))
    if mode == '1':
        new_message = input('Input your message: ')
        print('Result of encryption: ' + cryption_message(new_message, secret_key))
    else:
        new_message = input('Input your message:').split()
        print('Result of decryption: ' + decryption_message(new_message, secret_key))
