#! /usr/bin/env python3

import math

print('Please enter your plaintext message:')
plaintext = input().lower()

print('How many rails would you like to use?')
numberOfRails = int(input())

print('Removing whitespace...')
plaintext = ''.join(plaintext.split(' '))

print('Removing punctuation...')
for character in plaintext:
    if not character.isalnum():
        plaintext = plaintext.replace(character, '')

print(plaintext)

rails = []

for rail in range(numberOfRails):
    rails.append('')

for index in range(len(plaintext)):
    rails[index % numberOfRails] += plaintext[index]

ciphertext = ''

for rail in rails:
    ciphertext += rail

print(ciphertext)

maxRailLength = math.ceil(len(ciphertext) / numberOfRails)

postLocations = []

for i in range(numberOfRails):
    postLocation = maxRailLength * i
 
    if postLocation < len(ciphertext):
        postLocations.append(postLocation)

postLocations.append(len(ciphertext))

encryptedRails = []

for i in range(len(postLocations) - 1):
    encryptedRails.append(ciphertext[postLocations[i]:postLocations[i + 1]])

decryptedCiphertext = ''

for i in range(len(ciphertext)):
    decryptedCiphertext += encryptedRails[i % len(encryptedRails)][i // len(encryptedRails)]

print(decryptedCiphertext)