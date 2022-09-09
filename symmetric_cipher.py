def alphabet_encryption():
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    key = input("Input encryption key\n").upper()
    code_alphabet = list(alphabet)
    try:
        for i in range(len(key)):
            code_alphabet.remove(key[i])
            code_alphabet.insert(i, key[i])
        return alphabet, code_alphabet
    except:
        print('Incorrect key')
        return alphabet, code_alphabet


def message_cryption(regime):
    alphabet, code_alphabet = alphabet_encryption()
    message = input("Enter your message\n").upper()
    new_string = ''
    if regime == '1' or regime == 'ENCRYPTION':
        for i in message:
            if i.isalpha():
                i = code_alphabet[alphabet.index(i)]
            new_string += i
    else:
        for i in message:
            if i.isalpha():
                i = alphabet[code_alphabet.index(i)]
            new_string += i
    print('Result:\n', new_string, sep='')
    return 0


if __name__ == '__main__':
    mode = input('Select mode:\n1. Encryption\n2. Decryption\n').upper()
    message_cryption(mode)
