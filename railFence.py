#! /usr/bin/env python3

import math

def decrypt(ciphertext):
    plaintext = ''
    middle = math.ceil(len(ciphertext) / 2)
    
    upper = ciphertext[:middle]
    lower = ciphertext[middle:]

    for index in range(len(ciphertext)):
        if index % 2 == 0:
            plaintext += upper[index // 2]
        else:
            plaintext += lower[index // 2]

    print('Your plaintext is:\n%s' % plaintext)

def encrypt(plaintext):
    print('Removing whitespace...')
    plaintext = ''.join(plaintext.split())

    print('Removing punctation...')
    plaintext = removePunctuation(plaintext)

    upper = ''
    lower = ''

    for index in range(len(plaintext)):
        currentCharacter = plaintext[index]
        if index % 2 == 0:
            upper += currentCharacter
        else:
            lower += currentCharacter

    ciphertext = upper + lower
    print('Your ciphertext is:\n%s' % ciphertext)

def removePunctuation(plaintext):
    for character in plaintext:
        if not character.isalnum():
            plaintext = plaintext.replace(character, '')

    return plaintext

print('Would you like to encrypt or decrypt?')
process = input().lower()

if process == 'encrypt':
    print('Please input your plaintext message:')
    plaintext = input().lower()

    encrypt(plaintext)
elif process == 'decrypt':
    print('Please input your ciphertext message:')
    ciphertext = input().lower()
    
    decrypt(ciphertext)