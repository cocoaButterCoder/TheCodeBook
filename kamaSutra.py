#! /usr/bin/env python3

import random, string

def constuctSubstitutionKey(key):
    substitionKey = {}

    for i in range(0, len(key), 2):
        substitionKey[key[i]] = key[i + 1]
    
    return substitionKey

def decrypt(ciphertext, substitionKey):
    substitionKey = constuctSubstitutionKey(substitionKey)
    plaintext = translate(ciphertext, substitionKey)

    print('The plaintext message is:\n%s' % plaintext)

def encrypt(plaintext):
    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)

    substitionKey = constuctSubstitutionKey(alphabet)

    ciphertext = translate(plaintext, substitionKey)

    print('Let the recipient know this is the key:')
    print(substitionKey)

    print('Your ciphertext is:\n%s' % ciphertext)

def translate(startText, substitionKey):
    endText = ''

    for character in startText:
        if character.isalpha():
            for key, value in substitionKey.items():
                if character == key:
                    endText += value
                    break
                elif character == value:
                    endText += key
                    break
        else:
            endText += character

    return endText
    
print('Would you like to encrypt or decrypt?')
process = input().lower()

if process == 'encrypt':
    print('Please input your plaintext message:')
    plaintext = input().upper()

    encrypt(plaintext)
elif process == 'decrypt':
    print('Please input your ciphertext message:')
    ciphertext = input().upper()
    
    print('Please enter your substitution key:')
    print('(E.g. AB CD EF ...)')

    substitionKey = input().upper()
    substitionKey = ''.join(substitionKey.split(' '))

    decrypt(ciphertext, substitionKey)
