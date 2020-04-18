import random, string

def translate(message, cipherKey):
    messageComplement = ''

    for character in message:
        if character.isalpha():
            for key, value in cipherKey.items():
                if character == key:
                    messageComplement += value
                elif character == value:
                    messageComplement += key
        else:
            messageComplement += character

    return messageComplement

def generateCipherKey(keyString):
    cipherKey = {}
    for index in range(0, len(keyString), 2):
        cipherKey[keyString[index]] = keyString[index + 1]

    return cipherKey

print('Would you like to encrypt or decrypt?')
process = input().lower()

if process == 'encrypt':
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    alphabet = ''.join(alphabet)

    cipherKey = generateCipherKey(alphabet)

    print('The cipher key is ' + str(cipherKey))

    print('What is the plaintext?')
    plaintext = input().lower()

    ciphertext = translate(plaintext, cipherKey)
    print('The ciphertext is %s' % ciphertext)

elif process == 'decrypt':
    print('Please input the cipher key')
    print('(e.g. pbjkwq... for P <-> B, J <-> K, W <-> Q, etc')

    cipherKey = input().lower()
    cipherKey = generateCipherKey(cipherKey)

    print('What is the ciphertext?')
    ciphertext = input().lower()

    plaintext = translate(ciphertext, cipherKey)
    print('The plaintext is %s' % plaintext)
