#! /usr/bin/env python3
import math

def decrypt(ciphertext):
    middle = math.ceil(len(ciphertext) / 2)

    topRail = ciphertext[:middle]
    bottomRail = ciphertext[middle:]

    plaintext = ''

    for index in range(len(ciphertext)):
        if index % 2 == 0:
            plaintext += (topRail[index // 2])
        else:
            plaintext += (bottomRail[index // 2])

    print('Your plaintext message is %s' % plaintext)

def encrypt(plaintext):
    for character in plaintext:
        if not character.isalnum():
            plaintext = plaintext.replace(character, '')

    plaintext = ''.join(plaintext.split(' '))

    topRail = ''
    bottomRail = ''

    for index in range(len(plaintext)):
        if index % 2 == 0:
            topRail += plaintext[index]
        else:
            bottomRail += plaintext[index]

    ciphertext = topRail + bottomRail

    print('Your ciphertext message is %s' % ciphertext)

print('Would you like to encrypt or decrypt a message?')
process = input().lower()

if process == 'decrypt':
    print('Please enter your ciphertext message')
    ciphertext = input().lower()

    decrypt(ciphertext)
elif process == 'encrypt':
    print('Please enter your plaintext message')
    plaintext = input().lower()

    encrypt(plaintext)